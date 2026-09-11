# Tom Klootwijk — Unified Field Theory V2

**Author:** Tom Klootwijk  
**Identifier:** NL200678942  
**Date of birth:** 10-07-1990  
**Edition:** 2.0.0 — 11 September 2026

## Read the volume

Open `report/unified_field_theory_v2.pdf`. Its editable LaTeX source and generated figures are included in the same directory.

The primary V2 source is the supplied 18-page document *devoid the dark SDF definition where*. V2 centers its **UU ID / Double Set Operator**, **Agnostic Boundary Horizon**, **Chronotemporal Absorbing Field**, **Theseus identity**, **Genesis Horizon** and **Monotheistic Union** terminology. The 36-operator referential substrate and complete Gambit numerical transition are retained from the two earlier supplied PDFs.

The source equation is preserved exactly:

```text
UU_ID((d1,T1),(d2,T2)) = min(abs(d1-T1), abs(d2-T2))
```

The volume includes the source's different conventions and the explicit V2 constructions used to connect them. `spec/source_variants.json` records these bindings, including the integral/minimum distinction, the two one-bit conventions, the source conceptual bit map, the canonical C11 word, the unsigned decoder and the layered log-polar lift.

## Run the verification

The runtime and tests require Python 3.10 or later and use the standard library.

```sh
python tools/verify.py
python examples/run_demo.py --out demo_run --steps 64
```

The verifier checks the release manifest, author record, all 34 sealed definitions, the complete Dutch profile, experience lineage, 126 test methods and a fresh deterministic demonstration. Exact integer and state/capsule comparisons are byte-for-byte. Explicit floating geometric/statistical outputs use a 1e-12 comparison tolerance.

Optional schema validation and figure regeneration use the packages in `requirements-dev.txt`:

```sh
python -m pip install -r requirements-dev.txt
python tools/verify.py --schema
```

## What is formalized

The PDF gives nine V2 derivations, UU1–UU9, and the combined **UF2** theorem. They cover the minimum algebra, finite horizon union, exact unsigned boundary distance, retained component identities, temporal segment recurrence, complete unsigned decoding, the relational engine hinge, the layered spatial encoding and the correspondence between historical state horizons and Boolean OR.

The original **U4** and supporting proofs **C1–C16** are retained. The runtime implements the original integer transition and a complete unsigned-field conjugate wrapper. The Boolean arithmetic module supplies executable digit-array constructions rather than claiming a separately executed complete Boolean engine backend.

The source's weighted time integral and historical minimum shader remain separate observables. The source-centered and horizon-centered one-bit conventions also remain separate. The author's ontological vocabulary is retained as named identity postulates, while formal theorem statements give their own exact signatures and assumptions.

## Executed records

The declared `TKUFT-integer-chart-v2` fixture has 64 cells and two levels. Across 64 updates, direct and unsigned-field execution agree at every step, material stays at **18,677**, and the engine emits **2,258** ones. All 64 local segment certificates pass. The state has **7,579 bits**, stored in **948 bytes**. Half-run restart and uninterrupted execution give the same final state.

Final operative-payload SHA-256:

```text
77f7cdbf7ce5f76029d5d6c27900187b7edbdf12f0ecbbe664db21f3fd6b9d8b
```

The history envelope includes the initial state and 64 completed updates. It retains 4,262 active bit positions and changes strictly 57 times. Its file is a history projection, distinct from the current-state capsule.

A one-read intervention at cell 7, tick 3, first changes operative state at tick 3 and the pulse plane at tick 9. The source's own verification-XY example has a different seed and a different first-output tick; both are identified in the manuscript rather than conflated.

`verification/demo/` contains start/end capsules, the exact final binary word, packed output planes, summaries, pulse certificates, unsigned state parameters, the historical envelope, sample UU ID queries, the eight-bit decoding example, synthetic experience records, retained-integral calculations, lineage and all 7,579 spatial bit addresses.

## Source and data files

`spec/` contains two JSON Schemas, 36 retained operators, 20 pattern recipes, 16 UU ID mechanisms, the proof register, source variants and both named bit-layout views.

`data/` contains the exact author record and the complete edition Dutch profile. The profile has 100 entries and 28 pulse/Hamming-weight matches.

`sources/source_register.json` contains the exact filenames, page counts, roles and SHA-256 digests of all three uploaded source PDFs. Page citations in the manuscript refer to physical PDF pages or original source section numbers.

## Continue from a capsule

```python
from pathlib import Path
import sys
sys.path.insert(0, "src")
from tkuft.codec import decode_capsule, encode_capsule
from tkuft.engine import tick

seed, state = decode_capsule(Path("verification/demo/final.tku").read_bytes())
for _ in range(64):
    state, summary = tick(seed, state)
Path("continued.tku").write_bytes(encode_capsule(seed, state))
print(summary)
```

## Rebuild the report

```sh
python tools/build_data.py
python tools/build_figures.py
cd report
latexmk -pdf -interaction=nonstopmode -halt-on-error unified_field_theory_v2.tex
```

The LaTeX package declarations specify the font and layout dependencies; no font files are distributed. Generated tables and figures are already present.

`checksums/SHA256SUMS.txt` lists every delivered file except itself. The verifier writes fresh examples to a temporary directory and compares them against the frozen results. For an edited working copy, use `python tools/verify.py --skip-manifest`; this does not modify the original expected records.
