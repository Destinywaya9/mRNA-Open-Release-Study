# mRNA Public Release accessibility corrections

Status: Prepared and verified locally; NOT applied publicly. GitHub rejected the repository write with HTTP 403, “Resource not accessible by integration.” The connector has no release-asset upload action. The published tag and research ZIP remain unchanged.

## Apply the minimal repository correction

Apply the following exact patch to the default branch (`main`). It modifies only README.md and PUBLICATION_METADATA.json. Do not move or recreate the published `mRNAstudy` tag. The README replaces nonexistent repository paths with the verified download and exact extraction paths. The single JSON change fills the permanent release URL; release_DOI remains null.

Save the diff as `mrna-accessibility.patch`, then run in a clean repository checkout:

```bash
git apply --check mrna-accessibility.patch
git apply mrna-accessibility.patch
git diff --check
git add README.md PUBLICATION_METADATA.json
git commit -m "Fix public release download guidance and repository URL"
git push origin main
```

```diff
diff --git a/PUBLICATION_METADATA.json b/PUBLICATION_METADATA.json
index 3383861..1435c53 100644
--- a/PUBLICATION_METADATA.json
+++ b/PUBLICATION_METADATA.json
@@ -32,7 +32,7 @@
     "terms_status": "Exact source attribution/use terms retained"
   },
   "release_DOI": null,
-  "release_repository_URL": null,
+  "release_repository_URL": "https://github.com/Destinywaya9/mRNA-Open-Release-Study/releases/tag/mRNAstudy",
   "related_publication": {
     "DOI": "10.67272/qtet-monograph-2026",
     "relation": "Governing framework source",
diff --git a/README.md b/README.md
index 895f300..080c6a0 100644
--- a/README.md
+++ b/README.md
@@ -9,9 +9,13 @@ Lei A While Research Center is the publication entity; it holds no research IP.
 
 ## Read first
 
+[Download the complete v1.0.0 research archive (10.8 MB)](https://github.com/Destinywaya9/mRNA-Open-Release-Study/raw/refs/tags/mRNAstudy/QTET_RNA_Public_Release_v1.0.0_20261008.zip).
+Extract it and open `QTET_RNA_Public_Release_v1.0.0_20261008/`.
+The `study/` and `framework_source/` paths below are inside that extracted directory.
+
 1. [Release summary](RELEASE_SUMMARY.md): methods, all eight lanes, complete falsifier counts, and evidence mapping.
-2. [Executed correspondence notebook](study/QTET_RNA_Source_Correspondence_20261008.ipynb) or [HTML preview](study/QTET_RNA_Source_Correspondence_20261008.html).
-3. [Detailed correction report](study/QTET_RNA_Source_Correspondence_20261008.md).
+2. Executed correspondence notebook: `study/QTET_RNA_Source_Correspondence_20261008.ipynb`; HTML preview: `study/QTET_RNA_Source_Correspondence_20261008.html` (open locally after extraction).
+3. Detailed correction report: `study/QTET_RNA_Source_Correspondence_20261008.md` (inside the extracted archive).
 4. [Source rights and use terms](LICENSE.txt) and [citation metadata](CITATION.cff).
 
 ## Verify offline
@@ -69,7 +73,7 @@ outputs and use a separate working copy for any new observation.
 Suggested citation: Machwaya, D. (2026). QTET Tensor P2/P3 mRNA Intervention-Reversion: Source-Aligned Computational Release. Version 1.0.0.
 Lei A While Research Center. Public release, 2026-10-08.
 
-This release has no assigned DOI or public repository URL in its metadata.
+This release has no assigned DOI. Its permanent [GitHub release URL](https://github.com/Destinywaya9/mRNA-Open-Release-Study/releases/tag/mRNAstudy) is recorded in PUBLICATION_METADATA.json.
 DOI 10.67272/qtet-monograph-2026 identifies the related governing monograph.
 The full research attribution and use terms are in LICENSE.txt.
 Software preparation, validation, documentation, and packaging used AI
```

## Attach the existing archive to the published release

Attaching the identical ZIP improves accessibility by placing the complete research package directly under release Assets. It creates an additional download location for the same bytes, not a revised study or new scientific content. Do not unpack, rebuild, rename, or edit the research archive.

1. Download the existing archive from:
   https://github.com/Destinywaya9/mRNA-Open-Release-Study/raw/refs/tags/mRNAstudy/QTET_RNA_Public_Release_v1.0.0_20261008.zip
2. Confirm its size is 10,816,640 bytes and SHA-256 is:
   `acc178f25c90082df40de6264a35bbf1fb8ede2ba48a31ab8207edfb4b7f9156`
3. Open https://github.com/Destinywaya9/mRNA-Open-Release-Study/releases/edit/mRNAstudy
4. Attach `QTET_RNA_Public_Release_v1.0.0_20261008.zip` in the release attachment area. Keep the tag, release title, version, existing description, scientific claims, attribution, and licensing unchanged.
5. Append the access note below to the existing release description, then save the update. The repository download works before attachment; after attachment the identical ZIP will also be under Assets.
6. Download the attached asset and compare its size and SHA-256 with step 2. Its expected URL after successful attachment is:
   https://github.com/Destinywaya9/mRNA-Open-Release-Study/releases/download/mRNAstudy/QTET_RNA_Public_Release_v1.0.0_20261008.zip
   This asset URL is prospective; it has not been created or verified yet.

### Access note to append

Download the complete v1.0.0 research archive from [the repository](https://github.com/Destinywaya9/mRNA-Open-Release-Study/raw/refs/tags/mRNAstudy/QTET_RNA_Public_Release_v1.0.0_20261008.zip). Extract it and open `QTET_RNA_Public_Release_v1.0.0_20261008/`. The executed correspondence notebook, HTML preview, and detailed correction report are in `study/`, named `QTET_RNA_Source_Correspondence_20261008.ipynb`, `.html`, and `.md`. The [current repository README](https://github.com/Destinywaya9/mRNA-Open-Release-Study/blob/main/README.md) provides access instructions. Use remains governed by LICENSE.txt.

## Verification and preservation

- The tagged repository has no study/ directory; all three documents exist inside the original ZIP at the extraction paths above.
- The repository download returned HTTP 200, 10,816,640 bytes, and the matching SHA-256 above.
- All remaining relative Markdown links resolve to existing root files.
- Only release_repository_URL differs in the JSON; release_DOI remains null.
- The local ZIP is byte-identical to the tagged ZIP. No scientific result, mathematics, data, provenance, authorship, ownership, licensing, or restrictions were changed.
- The historical tagged README and embedded ZIP metadata remain as originally published. The default-branch correction and release access note provide current access guidance without rewriting that record. Existing checksum/provenance files describe the original package; do not regenerate them to disguise the documentation correction.

## Social media post

My mRNA Public Release v1.0.0 is now available on GitHub for medical teams and researchers to use, reproduce, and evaluate.

Across eight authentic pathogenic mRNA variant lanes, all eight computational lanes returned to their reference sequence, fold, and minimum free energy. The release includes 40 native full-transcript folding computations and 42,853 source and validation comparisons with zero disagreements.

The complete package makes the evidence available for examination: research data, raw outputs, executed notebooks, source code, validation records, provenance, and reproducibility checks. It also retains the cell → tissue-fold → organoid continuation protocol and measurement templates.

Medical teams and researchers: download the archive, examine the results, and reproduce the study under the published license, including its attribution, non-weaponization, and non-surveillance terms.

Published through Lei A While Research Center. Research by Destiny Machwaya.

https://github.com/Destinywaya9/mRNA-Open-Release-Study/releases/tag/mRNAstudy

#mRNA #MedicalResearch #ReproducibleResearch #QTET
