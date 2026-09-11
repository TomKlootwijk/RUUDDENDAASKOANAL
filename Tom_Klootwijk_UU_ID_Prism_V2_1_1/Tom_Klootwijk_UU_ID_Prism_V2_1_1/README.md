# Tom Klootwijk — Unified Field Theory V2.1.1
## UU ID Prism · Rainbow Facets and the Personal Data Passport

This subversion adds **Appendix I** to the supplied V2.1.0 corpus: **seven rainbow bands, 35 named facets, a timestamped personal archive view, and a usable local metadata-migration prototype**. The integrated PDF has **68 pages**; the 20-page addendum begins on physical PDF page **49**.

The previous body pages 2–48 are preserved without text or rendered-pixel changes. The cover and PDF navigation identify the new edition. The original V2.1 PDF and V2 executable archive are retained unchanged under `baseline/`.

## Open the passport viewer

Open **`app/index.html`** in a browser. It is a self-contained HTML file with no external resources or upload endpoint. It starts with an explicitly synthetic example; it is not a live sensor connection.

Use **Replay synthetic updates** or **Next update** to inspect the finite example. **Import snapshot** displays a local `snapshot.json` produced by this package. **Conceal private details** hides the displayed counts and timestamps; it is a presentation control, not encryption. **Save snapshot** exports the current JSON view.

Every facet retains a color, text label, stable facet ID, current record count and timestamp status. The rainbow bands classify **record types**, not people. No sexuality, religion, intent or other sensitive identity trait is inferred from gaze, biometric data, symbols or usage patterns. Voluntary identity declarations use a separate self-report facet.

## Migrate a selected folder

The initial workflow is **index-and-link**, not a payload backup: source files remain in place. The tool reads only the local folder you explicitly name, skips symlinks, applies a per-file byte budget, and writes a private inventory of relative names, lengths and SHA-256 digests.

```sh
python tools/inventory.py --root /path/to/my-selected-export --out private_inventory.json
```

Review `private_inventory.json`. For each item you choose to include, replace `"facet_id": null` with a facet such as `"F01"` for still imagery or `"F26"` for authored work. The names and definitions are in `spec/facets.csv` and the PDF. Unassigned rows remain unmapped. Map only records whose subject is you and whose use you are authorized to permit; another person's presence in one of your files is not an automatic subject link.

```sh
python tools/migrate.py --inventory private_inventory.json \
  --holder holder:my-local-archive --out private_passport \
  --confirm-authorized --confirm-holder-links
```

On Windows, enter the command on one line or use your shell's continuation syntax. The output directory contains:

- `passport.json`: the complete local metadata view, registry, correction/withdrawal log and restore inputs.
- `snapshot.json`: the current 35-facet display view; load this file into the HTML viewer.
- `migration_receipt.json`: assigned, unmapped and quarantined counts.

The migration generates opaque record links and does not copy filenames into the passport view. A missing original observation time is retained as **time unknown**, not invented from the import time. Inventory timestamps are not evidence of the time an experience occurred.

These JSON files are plain local files. Keep private inventories, snapshots and backups in storage you control; the package does not supply encryption, remote access control, signing keys or a government credential. A checksum checks bytes against an expected value and is not a proof of authorship or an authentication token.

## Rainbow registry

| Band | Facets | Data family |
|---|---|---|
| Red | F01–F05 | Vision and visual context |
| Orange | F06–F10 | Sound and language |
| Yellow | F11–F15 | Touch, motion and orientation |
| Green | F16–F20 | Body, chemical senses and environment |
| Blue | F21–F25 | Place, activity and time |
| Indigo | F26–F30 | Expression, learning and relationships |
| Violet | F31–F35 | Identity, rights and provenance |

Acquisition is disabled by default for every facet. A registered facet is a vocabulary entry, not evidence that a sensor exists or a record has been collected. The explicit states are **missing, fresh, stale, withdrawn, time unknown and clock conflict**. Freshness describes the most recent admitted record under the facet's declared interval; it is not a completeness or truth score.

## UU ID and the complete vector

The retained UU ID operator is the minimum of absolute threshold deviations. In this edition's migration example, a planned facet has coverage `min(1, active_count / target_count)`, represented by an exact rational number. The minimum deviation is zero when **at least one** planned facet reaches its target. **Whole-plan completeness is a separate conjunction.** A single scalar, color, Hamming weight or parity bit cannot replace the complete facet vector, source records or audit lineage.

“All data” in the operational workflow means the explicitly selected, authorized inventory and declared metadata plan. The uploaded dialogue's NSA/PRISM, Pride-symbol and population-control scenario is documented in `spec/source_concordance.json` and the addendum. It is kept distinct from historical sources, mathematical results and implemented capabilities. The package has no NSA interface, covert collector, person-matching service or population-scoring system.

## Verify and replay

The runtime and the **66 new test methods** use Python 3.10 or later and the standard library:

```sh
python tools/verify.py
python tools/demo.py --out demo_run
```

The verifier checks the manifest, facet registry, tests and byte-for-byte synthetic replay. It leaves all shipped comparison records unchanged. For optional schema checks and the original **126-test V2 suite**:

```sh
python tools/verify.py --schema --baseline
```

`--schema` requires the separately installed `jsonschema` package. `--baseline` safely extracts the unchanged original ZIP to a temporary directory and invokes its verifier. Use `--skip-manifest` when deliberately testing an edited working copy rather than the shipped release.

The recorded synthetic example has **16 initial links**, one exact retry, four quarantined attempts, one correction and one withdrawal. The final view has **15 active links**, **14 unique linked objects**, **667 referenced bytes**, and **18 audit events**. It contains 10 fresh, 3 stale, 1 unknown-time and 1 clock-conflict active facets. Its whole plan is incomplete despite a UU ID minimum of zero. Exact restoration reproduces the snapshot.

Final synthetic snapshot SHA-256:

```text
5119d9587e7b91c48040a21d32d96982a27ccc470382adb0a21e1185696f7ace
```

Optional browser checks use Playwright and an installed Chromium:

```sh
python tools/check_viewer.py --chromium /path/to/chromium
```

The recorded browser check loaded the exact HTML using `set_content`; direct local-file navigation was blocked by the execution environment's browser policy. It checked all 35 rows, local snapshot import, concealment and replay controls with no JavaScript errors or HTTP requests. This check does not constitute a full accessibility or application-security evaluation.

## Edit or rebuild

`report/prism_addendum.tex` and `report/cover.tex` are the editable LaTeX sources. Their compiled PDFs and the screenshot used by the report are included.

```sh
python tools/build_viewer.py
cd report
latexmk -pdf -interaction=nonstopmode -halt-on-error prism_addendum.tex
latexmk -pdf -interaction=nonstopmode -halt-on-error cover.tex
cd ..
python tools/assemble_pdf.py
```

PDF assembly requires PyMuPDF. It compares the retained parent pages' extracted text and rendered pixels with the supplied baseline. Screenshot regeneration is optional through `tools/check_viewer.py --capture /path/to/screenshot.png`.

## Contents and source records

`report/` contains the integrated volume and editable addendum. `app/` contains the viewer and its template. `src/uu_prism/` contains exact metadata and UU ID operations. `spec/` contains two JSON Schemas, the 35-facet registry and the 15-point source concordance. `verification/` contains executed test results, browser checks, parent-page checks and synthetic replay records. `sources/` identifies the parent and supplied dialogue by digest, and records the narrowly used PCLOB, W3C and IETF sources. `checksums/SHA256SUMS.txt` covers every delivered file except itself.

The corpus includes the author attribution requested for the project. The demonstration contains no real sensor readings, passwords, access tokens or personal-history payloads.
