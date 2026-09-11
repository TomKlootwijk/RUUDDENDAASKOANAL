# Gambit Closure 4.0.1 - CUDA repair revision

This directory is a separate revision of the original frozen 4.0 release at
`C:\RUUDDENDAASKOANAL\Tom_Klootwijk_Gambit_Closed_Engine_4.0\Tom_Klootwijk_Gambit_Closure_4.0`.
The original was verified against all 196 manifest entries before copying.
`provenance/release_4.0_SHA256SUMS.txt` preserves its exact original manifest.

The numerical transition, Boolean arithmetic, capsule format, LUT assets, all
frozen expected output files, the 24 SMT obligations, and the original model
manuscript are unchanged. New source hashes describe the repaired revision;
they do not replace numerical golden results. `REVISION.json` records original
and revised hashes, and `REVISION.patch` shows the textual source changes.

Changes:

- Replace the CUDA macro's local error variable with an inline function. The
  original local name `e` shadowed the engine argument during evaluation and
  caused seven NVCC compilation errors. Function arguments evaluate the CUDA
  call exactly once without introducing a variable into its caller's scope.
- Report the actual zero-based segment update on GPU/CPU mismatch. The prior
  code always passed update zero to the cell comparison.
- Select the same static MSVC runtime for native and CUDA objects, resolving
  the mixed-runtime linker warning observed during the initial repair build.
- Add explicit Windows CUDA toolset selection to the verifier and resolve
  plain NVIDIA batch forwarding launchers to their real executables.
- Preserve requested verification stages, exact command failures, and blocked
  solver status in machine-readable reports.
- Add a production-source CUDA error-helper regression, four verification
  coordinator regressions, and an extra GPU boundary/error verification tool.

Current validation results are under `validation/`. The final PDF is
`output/pdf/Gambit_Closure_4.0.1_Verification.pdf`. Existing `evidence/` files
remain historical 4.0 evidence; they are not relabeled as new executions.

The user approved revision-local Z3 setup. The existing cached Z3 4.15.4.0 wheel
was validated against its RECORD and extracted to `local_tools/z3-4.15.4.0`.
There were no downloads, global installations, driver changes, or GPU setting
changes. The tool directory includes provenance and package metadata.

Reproduce the full checks from this directory with unused output paths:

```powershell
$env:PATH = (Join-Path (Get-Location) 'local_tools/z3-4.15.4.0/bin') + ';' + $env:PATH
python tools/verify.py --cpu-only --formal --out validation/cpu
python tools/verify.py --hardware --formal --sanitizers --profile --cmake-cuda-toolset cuda=12.8 --out validation/full
python tools/verify_gpu_edges.py --cpu validation/full/build/Release/gambit.exe --gpu validation/full/cuda_build/Release/gambit_cuda.exe --contract validation/full/cuda_build/Release/gambit_cuda_contract.exe --out validation/gpu_edges
```

The CPU and GPU commands retain all frozen golden checks. The SMT checks prove
their submitted obligations under Z3; runtime checks provide finite execution
evidence. Neither is an exhaustive proof of the entire compiled implementation.
