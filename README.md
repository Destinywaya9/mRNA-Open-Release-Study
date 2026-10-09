# QTET Tensor P2/P3 mRNA Intervention-Reversion: Source-Aligned Computational Release

**Destiny Machwaya · Version 1.0.0 · 2026-10-08**

This public release preserves the full molecular intervention-reversion result,
the original research packet, native measurements, and corrected source
correspondence. Destiny Machwaya is the sole research author and rights holder.
Lei A While Research Center is the publication entity; it holds no research IP.

## Read first

1. [Release summary](RELEASE_SUMMARY.md): methods, all eight lanes, complete falsifier counts, and evidence mapping.
2. [Executed correspondence notebook](study/QTET_RNA_Source_Correspondence_20261008.ipynb) or [HTML preview](study/QTET_RNA_Source_Correspondence_20261008.html).
3. [Detailed correction report](study/QTET_RNA_Source_Correspondence_20261008.md).
4. [Source rights and use terms](LICENSE.txt) and [citation metadata](CITATION.cff).

## Verify offline

Extract the ZIP and open a terminal in this release directory. Python 3.10 or
later is sufficient for file integrity and the software replay; no third-party
package or network connection is required.

    python verify_release.py
    python verify_release.py --replay

The first command checks every manifest entry. The second also runs the corrected
acceptance and source comparisons in a temporary copy, then compares all
regenerated audit outputs with the released outputs. The released files stay
unchanged. Neither command imports a folding engine or performs a new RNA fold.

The saved notebook and HTML may be viewed directly. To execute the correspondence
notebook in a separate working copy, use study/ as the working directory with
pandas and IPython available. Saved outputs are already included.

## Included evidence

| Location | Contents |
| --- | --- |
| study/rna_run/ | All 112 members of the supplied native rerun, including frozen inputs, 40 raw fold frames, eight lane records, source code, figures, and executed notebook |
| study/cancer_packet/ | All 20 original cancer-packet members plus four byte-identical recovered notebook dependencies |
| study/inherited_v2/ | All 26 original intervention-reversion v2 members |
| study/correspondence_outputs/ | Complete source mapping, 48 endpoint comparisons, 192-row source-compatible ledger, corrected tests and fault regressions |
| framework_source/ | Complete supplied QTET/QTL-Sphere monograph; governing source and exact attribution/use terms |
| RELEASE_VALIDATION.json | Actual public-release verification result |
| RELEASE_PROVENANCE.json | File preservation, framework source identity, and packaging scope |
| SHA256SUMS.txt | SHA-256 for every released payload file |

## Scientific and software status

The canonical P2 traversal, full P3 embedding, authentic variants, transcript
versions, measured outcomes, null results, and original falsifiers are preserved.
The original measurement producer is retained byte-identically. The corrected
study entry point is study/source_aligned_runner.py; the earlier validator remains
an explicitly historical artifact. See [release notes](RELEASE_NOTES.md).

Forty measurements are native full-transcript folds. The 1,600 Delay records
include stored invariance checks and fresh endpoint observations as documented
in the native run; they are not 1,600 independent RNA folds. The 42,853 source
comparisons are software/audit vectors. The original biological continuation
retains empty templates for actual cell, tissue-fold, and organoid measurements.

For reproducing a native observation, use the exact frozen inputs and recorded
settings in study/rna_run/environment.json with ViennaRNA 2.7.2. The optional
requirements-native.txt pins the folding-engine dependency. Preserve original
outputs and use a separate working copy for any new observation.

## Citation and disclosure

Suggested citation: Machwaya, D. (2026). QTET Tensor P2/P3 mRNA Intervention-Reversion: Source-Aligned Computational Release. Version 1.0.0.
Lei A While Research Center. Public release, 2026-10-08.

This release has no assigned DOI or public repository URL in its metadata.
DOI 10.67272/qtet-monograph-2026 identifies the related governing monograph.
The full research attribution and use terms are in LICENSE.txt.
Software preparation, validation, documentation, and packaging used AI
assistance. The research and governing mathematics are Destiny Machwaya's;
no AI system is listed as an author or rights holder.
