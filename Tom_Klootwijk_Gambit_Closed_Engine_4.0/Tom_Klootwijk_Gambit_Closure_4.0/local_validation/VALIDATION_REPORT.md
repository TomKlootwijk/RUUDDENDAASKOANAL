# Kernel validation — 11 September 2026

**Verdict: CPU validation passed; the frozen CUDA source fails compilation; a fresh formal solver run is blocked by missing Z3. The release cannot currently be certified for GPU execution.**

Validated directory: `C:\RUUDDENDAASKOANAL\Tom_Klootwijk_Gambit_Closed_Engine_4.0\Tom_Klootwijk_Gambit_Closure_4.0`. The path supplied in the request did not exist literally; this is the matching extracted 4.0 release.

| Scope | Result | Evidence |
|---|---|---|
| Frozen release integrity | PASS | All 196 manifest entries matched before and after validation. |
| Native C++ build and suite | PASS | MSVC Release build; 338,184 checks, including exhaustive 8-bit pairs, randomized 64-bit arithmetic, and 10,000 continuation ticks. |
| Python suite | PASS | All 24 existing test methods passed. |
| Native frozen output profiles | PASS | All five consensus files matched the frozen hashes for all six profiles. |
| Native / Boolean / independent Python | PASS | All five consensus files matched for micro_xx, micro_xy, verify_xx, and verify_xy, each over 64 updates. |
| Laptop-scale native runs | PASS | Two 131,072-cell, 256-update profiles matched frozen outputs and passed the independent pulse, parity, event, and endpoint-count audits. |
| Checkpoint continuation | PASS | A 17-update segment followed by a standalone 47-update resume matched the continuous 64-update final capsule and pulse trace. |
| Invalid CLI cases | PASS | All four coordinator cases were rejected. |
| Additional boundary probes | PASS | Twenty native/Boolean executions from ten valid boundary capsules matched Python final capsules. |
| Additional malformed input probes | PASS | Thirty-five malformed capsules with freshly recomputed SHA-256 digests were rejected by both native and Python loaders. |
| Feedback intervention witness | PASS | Independent Python execution reproduced all 40 archived trace rows; first state difference at tick 3 and first pulse difference at tick 7. |
| CUDA configuration with explicit toolkit | PASS | CUDA 12.8.61, MSVC 19.44, sm_120 and compute_120 selected successfully. |
| CUDA source compilation | FAIL | Seven NVCC errors caused by the CU macro variable shadowing the engine argument. |
| GPU execution / sanitizers / profiling | NOT RUN | No CUDA executable was produced. |
| Fresh SMT solver execution | BLOCKED | Neither a Z3 executable nor libz3 was available to the verifier. |

**Finding 1 — P1: the CUDA error-checking macro prevents compilation.**

At [src/cuda.cu:10](C:/RUUDDENDAASKOANAL/Tom_Klootwijk_Gambit_Closed_Engine_4.0/Tom_Klootwijk_Gambit_Closure_4.0/src/cuda.cu:10), `CU(call)` declares `const auto e=(call)`. The constructor also names its `Engine` argument `e`. C++ makes the macro's new `e` visible inside its initializer, so the `e.cells`, `e.words`, and `e.asset` expressions at lines 44, 45, 48, and 53 refer to the undeduced macro variable. NVCC reports: `a variable declared with an auto type specifier cannot appear in its own initializer`.

This is a confirmed source defect, independent of toolkit discovery. Explicitly selecting the installed CUDA 12.8 toolkit successfully configured the project, then compilation of the unchanged source failed with seven errors. NVCC exited with code 2; the build exited with code 1.

Recommended separate revision: make the error checker an inline function receiving the completed CUDA result and expression text, or give the macro temporary a distinct name. An isolated C++ reproduction confirmed that renaming the macro temporary resolves that reproduction. No revised engine was built or validated here.

**Finding 2 — P3: CUDA mismatch diagnostics always report update zero.**

At [src/cuda.cu:84](C:/RUUDDENDAASKOANAL/Tom_Klootwijk_Gambit_Closed_Engine_4.0/Tom_Klootwijk_Gambit_Closure_4.0/src/cuda.cu:84), the per-update check passes the constant `0` to `compare_states`. A mismatch at a later update would be incorrectly attributed to step zero. Track the segment update index in a separate revision. This finding concerns diagnostics; no runtime mismatch was observed because compilation failed.

**Environment and workflow limitations.**

This machine reports an NVIDIA GeForce RTX 5070 Ti Laptop GPU, compute capability 12.0, driver 591.59, and 12,227 MiB memory. Validation used Python 3.13.11, CMake 4.3.2, MSVC 19.44.35221.0, and CUDA 12.8.61 on Windows.

Both required invocations with `--formal` completed CPU checks and then reported `BLOCKED` because Z3 was unavailable. Their top-level status must not be described as an overall pass. A supplemental hardware invocation omitting `--formal` reached CUDA configuration; default toolkit discovery failed. A new build directory with `-T cuda=12.8` resolved discovery and exposed the source compilation defect. No tools, drivers, or dependencies were installed; no GPU settings were changed.

Reproduction commands, run from the validated directory (choose new output paths for subsequent runs):

```powershell
python tools/verify.py --cpu-only --formal --out local_validation/20260911_cpu_formal
python tools/verify.py --hardware --formal --sanitizers --profile --out local_validation/20260911_hardware_formal
python tools/verify.py --hardware --sanitizers --profile --out local_validation/20260911_hardware
cmake -S . -B local_validation/cuda128 -G "Visual Studio 17 2022" -A x64 -T cuda=12.8 -DGAMBIT_ENABLE_CUDA=ON
cmake --build local_validation/cuda128 --config Release --parallel 2
```

**Formal review boundary.**

Review found no concrete contradiction in the stated finite-state theorem and its supporting written proofs. The 24 packaged solver logs are consistent with 22 expected UNSAT results and two intentional SAT counterexamples, but those are historical Linux/Z3 results, not a fresh solver run on this machine. The SMT targets are selected algebraic obligations, not an extracted model of the complete C++, capsule loader, CUDA backend, compiler, or hardware. For example, restoring division is checked at eight bits while the Boolean implementation also uses wider division. Tests and written arguments provide separate evidence; they are not exhaustive implementation proofs.

No arithmetic or capsule-loader defect was found in the bounded CPU executions and source review. Finite execution evidence does not establish correctness for every admitted state. Trace auditing verifies the disclosed pulse/event/count identities; it does not reconstruct every historical activity input.

**Saved evidence.**

- [CPU coordinator report](C:/RUUDDENDAASKOANAL/Tom_Klootwijk_Gambit_Closed_Engine_4.0/Tom_Klootwijk_Gambit_Closure_4.0/local_validation/20260911_cpu_formal/verification.json), with full subprocess logs and output profiles in the same directory.
- [Formal prerequisite report](C:/RUUDDENDAASKOANAL/Tom_Klootwijk_Gambit_Closed_Engine_4.0/Tom_Klootwijk_Gambit_Closure_4.0/local_validation/20260911_cpu_formal/formal/report.json).
- [Hardware coordinator report](C:/RUUDDENDAASKOANAL/Tom_Klootwijk_Gambit_Closed_Engine_4.0/Tom_Klootwijk_Gambit_Closure_4.0/local_validation/20260911_hardware/verification.json).
- [Successful explicit CUDA configuration log](C:/RUUDDENDAASKOANAL/Tom_Klootwijk_Gambit_Closed_Engine_4.0/Tom_Klootwijk_Gambit_Closure_4.0/local_validation/cuda128_configure.txt) and [failed CUDA build log](C:/RUUDDENDAASKOANAL/Tom_Klootwijk_Gambit_Closed_Engine_4.0/Tom_Klootwijk_Gambit_Closure_4.0/local_validation/cuda128_build.txt).
- [Additional probe results](C:/RUUDDENDAASKOANAL/Tom_Klootwijk_Gambit_Closed_Engine_4.0/Tom_Klootwijk_Gambit_Closure_4.0/local_validation/cpu_review/probe_results.json) and [reproduction script](C:/RUUDDENDAASKOANAL/Tom_Klootwijk_Gambit_Closed_Engine_4.0/Tom_Klootwijk_Gambit_Closure_4.0/local_validation/cpu_review/probe.py).
- [Final integrity check](C:/RUUDDENDAASKOANAL/Tom_Klootwijk_Gambit_Closed_Engine_4.0/Tom_Klootwijk_Gambit_Closure_4.0/local_validation/integrity.json).

The frozen source, assets, manuscript, expected output hashes, and delivered evidence were not changed. New validation artifacts are under `local_validation/`.
