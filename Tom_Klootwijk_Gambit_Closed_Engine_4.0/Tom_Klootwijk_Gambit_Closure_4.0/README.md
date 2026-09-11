# Tom Klootwijk Gambit — Closed Engine 4.0

**Unified Seed–Field Theorem and Theory of Consciousness — Formal Closure Edition**  
Author attribution: **Tom Klootwijk · NL200678942 · 10-07-1990**

A deterministic, self-referential, seed-based numerical engine. Its previous output
is read back into field sampling; bounded recurrent memory and binary latches
influence subsequent transport. Its complete state has a canonical binary encoding.
The closure theorem concerns this finite mathematical machine, not proof of
subjective consciousness, universal biology or energy-free operation.

## Start here

Read `Tom_Klootwijk_Gambit_Closed_Engine_4.0.pdf` for the normative equations,
Unified Closure Theorem U4, sixteen supporting proofs and the evidence boundary.
`AGENTS.md` is the entry point for Codex or another automated verifier.

```sh
python tools/verify.py --cpu-only --formal
```

Prerequisites: Python 3.11+, CMake 3.24+, a C++17 compiler; Z3 executable or installed
libz3 is needed only for `--formal`. No script downloads dependencies or changes
frozen expected hashes. A successful CPU run reports `CPU_PASS_GPU_NOT_RUN`.
Use an unused output path with `--out`; default results go to `local_verification/`.

## Build and run

```sh
cmake -S . -B build -DGAMBIT_ENABLE_CUDA=OFF -DCMAKE_BUILD_TYPE=Release
cmake --build build --config Release --parallel 2
ctest --test-dir build -C Release --output-on-failure
./build/gambit --asset assets/verify_xy.gblut --steps 64 --out run_a
./build/gambit --resume run_a/final.gbc --steps 64 --out run_b
python tools/audit_trace.py run_a
```

For a Visual Studio build, use `build/Release/gambit.exe`. Each output path must be
new. Logging is limited to 4096 updates per segment; this is not a semantic halt.
Resume further segments without resetting any causal state. `final.gbc` embeds its
LUT and parameters, so it does not need an external asset file.

Use `--backend gates` for the explicit one-bit Boolean arithmetic realization:

```sh
./build/gambit --asset assets/micro_xy.gblut --backend gates --steps 64 --out gate_run
python tools/reference.py --asset assets/micro_xy.gblut --steps 64 --out python_run
python tools/state_sdf.py 01011001
```

The native path is the practical CPU engine. The gates path expresses arithmetic
with Boolean digits, carries, borrows and a restoring divider; host addressing,
loops and I/O still run on a normal computer. A one-bit output symbol is not the
whole state: the operational payload contains `118*N+27` bits. A new seed can use
`--feedback 0` for the specific pulse-feedback ablation; other recurrent mechanisms
remain active. The XX and XY configurations are symbolic seeds.

## RTX 5070 Ti Laptop / CUDA

CUDA source is included but **was not compiled or executed in the delivery
environment**. There is no precompiled GPU binary or measured cache claim.
The local verification workflow targets the actual requested RTX 5070 Ti Laptop,
using `sm_120` and a `compute_120` PTX path:

```sh
python tools/verify.py --hardware --formal --sanitizers --profile
```

This requires a compatible NVIDIA driver/device, CUDA Toolkit 12.8+ with the
selected architecture target, `nvidia-smi`, `cuobjdump`, Compute Sanitizer and Nsight
Compute CLI when requested. The workflow compares texture and global LUT fetches,
block sizes, forced PTX JIT and checkpoint continuation. Missing prerequisites
report `BLOCKED`; failed checks report `FAIL`. Hardware success cannot be inferred
from CPU success. Consult `docs/VERIFICATION.md` for scope and trust assumptions.

## What is delivered

- `src/`, `include/`: native C++, Boolean ALU and conditional CUDA source.
- `tools/`, `tests/`: independent Python model, replay/audit/verification tools.
- `assets/`: frozen paired log-polar LUTs, manifests and expected output digests.
- `formal/`: U4, written proofs, 24 SMT obligations (22 expected UNSAT, two expected SAT).
- `evidence/`: executed CPU traces, solver logs, tests and intervention witness.
- `manuscript/`, `docs/`: editable manuscript, binary contract and source audit.
- `provenance/`: unchanged latest corpus and unchanged original 3.1 archive,
  which recursively preserves previous theory and kernel releases.

The capsule count certificate is `65536*Q + r_end = r_start + K`. The independent
trace auditor verifies emitted pulses, parity/events and the endpoint certificate;
only replay checks the entire historical sequence of input activity values.
SHA-256 binds exact bytes to a trusted expected digest, not authorship or intent.

## Privacy and application boundary

This private-attribution release contains the author details above and the original
corpus. Review before public sharing. It is an offline numerical research program,
with no audio, transducer, amplifier, laser, human-targeting or actuator interface.
Historical source claims are recorded and audited, not silently endorsed.

No font files, credentials, drivers or third-party compiled libraries are included.

## Rebuild the manuscript

With Pandoc and pdfLaTeX already installed, run:

```sh
python tools/build_pdf.py
```

This deliberately rebuilds the PDF and editable LaTeX from
`manuscript/Closure_4.0.md` and `manuscript/preamble.tex`. It changes a frozen release
file, so perform it in a working copy, not before integrity verification. The two
frozen figure PDFs are included. Their optional regeneration script requires
Matplotlib (`python tools/make_figures.py`). Re-baking LUTs is a separate optional
operation and requires NumPy; exact replay uses the delivered frozen bytes instead.
