# Verification task: Tom Klootwijk Gambit native CUDA 3.1

Author attribution: Tom Klootwijk, NL200678942, 10-07-1990.
This is an engineering specialization of Edition 3.0, NOT an empirically validated consciousness model.

Read README.md, docs/MODEL_AND_PROOFS.md, docs/MIGRATION.md and docs/CODEX_VERIFY.md before editing.
The task is verification on the user's actual RTX 5070 Ti Laptop GPU (12 GB), not replacement by an unrelated engine.

Run from a local shell with physical GPU access:

    python tools/verify.py --hardware --sanitizers --profile

Use a suitable CUDA-supported C++ compiler environment (Windows: the matching Visual Studio developer shell;
Linux: a host compiler supported by the installed CUDA toolkit). Obtain user approval for any missing tool installation.
Do not use an administrator shell by default. Do not alter clocks, voltage, TDR, driver permissions or profiler security policy.
No network, API key or Codex integration is required by the kernel itself. A cloud-only workspace without GPU access is insufficient.

Never regenerate or overwrite assets, golden hashes, provenance or delivered evidence to make a failed test pass.
Never change formulas, endianness, tie rules, shift amounts or feedback order silently. Document proposed changes first.
If verification fails, preserve the original, save the failing command and raw log, and propose a minimal separate patch.

Required evidence: package hashes; local device identification; nvcc version and sm_120 support; successful native build;
C++ and independent Python references; exhaustive texture readback; exact CPU/GPU state, samples, control and words;
XX/XY seeds; different block sizes; texture/global equality; one-bit intervention; repeat run and forced PTX run;
Compute Sanitizer logs; PTX and SASS; Nsight Compute texture/global reports. Report limited instrumentation scopes precisely.
GPU absence or nvcc absence means BLOCKED, not PASS. A CPU-only run may only be called CPU_PASS_GPU_NOT_RUN.
An emitted binary word is not the entire state, the complete seed, a proof of sentience or a physical law.

After completion, report the actual hardware, command, output folder, hashes, passed/failed/blocked checks and any remaining review.
Do not assert guaranteed cache residency, texture superiority, zero latency, driverless execution or a consciousness proof.
