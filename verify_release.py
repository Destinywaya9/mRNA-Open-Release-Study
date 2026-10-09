"""Verify public release bytes and optionally replay corrected software checks.

No RNA folding engine is imported or invoked. Replay writes only to a temporary
copy and leaves the released evidence unchanged.
"""
from pathlib import Path
import argparse
import hashlib
import json
import os
import re
import shutil
import subprocess
import sys
import tempfile


def digest(path):
    value = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            value.update(block)
    return value.hexdigest()


def check_manifest(root):
    checked = 0
    for line in (root / "SHA256SUMS.txt").read_text().splitlines():
        expected, relative = line.split("  ", 1)
        path = Path(relative)
        if not re.fullmatch(r"[0-9a-f]{64}", expected) or path.is_absolute() or ".." in path.parts:
            raise ValueError("Invalid manifest entry: " + relative)
        actual = root / path
        if not actual.is_file() or digest(actual) != expected:
            raise ValueError("File missing or changed: " + relative)
        checked += 1
    return checked


def replay_checks(root):
    expected = root / "study/correspondence_outputs"
    with tempfile.TemporaryDirectory(prefix="qtet-rna-release-") as temporary:
        working = Path(temporary) / "study"
        shutil.copytree(root / "study", working)
        environment = os.environ.copy()
        environment["PYTHONDONTWRITEBYTECODE"] = "1"
        for script in ("source_aligned_runner.py", "verify_source_correspondence.py"):
            result = subprocess.run([sys.executable, str(working / script)], cwd=working,
                                    env=environment, capture_output=True, text=True)
            if result.returncode:
                raise RuntimeError(script + " failed:\n" + result.stdout + result.stderr)
        output = working / "correspondence_outputs"
        compared = 0
        for saved in sorted(expected.iterdir()):
            if saved.is_file():
                regenerated = output / saved.name
                if not regenerated.is_file() or saved.read_bytes() != regenerated.read_bytes():
                    raise ValueError("Replay differs from released result: " + saved.name)
                compared += 1
        summary = json.loads((output / "Correspondence_Summary.json").read_text())
        if not summary["corrected_validator_rejects_all_five"]:
            raise ValueError("Demonstrated validator faults were not rejected")
        if any(row["mismatches"] for row in summary["source_falsifier_gate_replays"]):
            raise ValueError("Source falsifier correspondence mismatch")
        return {"output_files_identical": compared,
                "intact_lanes_accepted": summary["matched_primary_lanes"],
                "deliberate_faults_rejected": 5,
                "source_gate_comparisons": sum(row["vectors_checked"] for row in summary["source_falsifier_gate_replays"]),
                "source_gate_disagreements": 0, "new_RNA_folds": 0}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--replay", action="store_true", help="Replay corrected software checks in a temporary copy")
    args = parser.parse_args()
    root = Path(__file__).resolve().parent
    result = {"file_hashes_verified": check_manifest(root), "file_integrity_pass": True}
    if args.replay:
        result["replay"] = replay_checks(root)
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
