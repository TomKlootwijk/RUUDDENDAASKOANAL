# Tom Klootwijk Gambit - Native CUDA Kernel 3.1
## Engineering companion to Unified Seed-Field Theorem and Theory of Consciousness, Edition 3.0

**Author: Tom Klootwijk · NL200678942 · 10-07-1990**

This package contains actual C++17/CUDA source, a bit-exact CPU implementation, an independent Python specification, pre-baked XX/XY log-polar field textures, integer-state/one-bit trace certificates, and a local verification workflow. The native executable has no Python, tensor-framework, network or cloud dependency. Python coordinates verification; NumPy is needed only to rebuild geometric assets.

**Delivery status:** the CPU builds and tests were executed. No NVIDIA GPU, NVIDIA driver tooling or CUDA compiler was available in the delivery environment. The `.cu` file has **not** been compiled with nvcc or executed here. There is no precompiled GPU binary, fabricated GPU benchmark, cache-hit result or consciousness certificate. The device-specific work is explicit in `AGENTS.md` and `docs/CODEX_VERIFY.md`.

## Start on the laptop

Install/use a CUDA Toolkit that lists `sm_120` (12.8 or newer), its supported host C++ compiler, CMake 3.24+, and Python 3.10+. The device must have a compatible NVIDIA driver. Full instrumentation also needs Compute Sanitizer and Nsight Compute CLI (`ncu`) on PATH. Windows users should run from the matching Visual Studio developer environment. The package does not install or change any of these tools.

From the extracted project root:

```text
python tools/verify.py --hardware --sanitizers --profile
```

This is also the command in `AGENTS.md`. The shell wrappers are `tools/verify_local.ps1` and `tools/verify_local.sh`. Verification creates a new timestamped `local_verification/` folder, records raw commands and logs, compiles the sources, checks the actual laptop GPU, compares all states and output words, and collects hardware evidence. Missing hardware or tools produces `BLOCKED` (exit 2); a failed check produces `FAIL` (exit 1). Neither is replaced by a CPU pass.

To check only the CPU portion:

```text
python tools/verify.py --cpu-only
```

A successful CPU-only run is labelled `CPU_PASS_GPU_NOT_RUN`.

## Manual native build and run

```text
cmake -S . -B build -DGAMBIT_ENABLE_CUDA=ON -DCMAKE_BUILD_TYPE=Release
cmake --build build --config Release --parallel 2
```

Linux / single-configuration build:

```text
./build/gambit_cuda --asset assets/laptop_xy.gblut --out run_xy --verify
```

Windows / Visual Studio multi-configuration build:

```text
.\build\Release\gambit_cuda.exe --asset assets/laptop_xy.gblut --out run_xy --verify
```

Select a new output directory for each run. `--verify` performs a full LUT fetch/readback and compares every sample, cell, control state, report and packed word against the native CPU reference at every step. The independent Python implementation is checked separately by the verification coordinator.

## What the model executes

The finite seed includes the LUT bytes, all header parameters, versioned source and run options. XX and XY retain `[X][X]` and `[X][Y]` axioms and parallel rules `X -> X[+X]Y`, `Y -> Y[-Y]X`. Geometry is compiled offline for levels 0 through 4. Device-side pulse feedback selects the next level; the GPU does not perform unbounded string rewriting.

The closed loop is:

```text
previous packed pulse -> log-polar lookup / memory deformation
  -> hysteretic gates -> conservative integer transport and reaction
  -> local material + field observation -> fast state -> memory
  -> exact pulse-density bit -> packed feedback for the next step
```

The runtime uses an immutable unsigned-32-bit texture with point sampling, unnormalized exact texel-center addresses and integer element reads. It also provides an ordinary global-memory fetch path for equality and profiling comparisons. “Native” does not mean driverless: CUDA still uses the NVIDIA driver/runtime, launches and synchronization. Texture access does not imply guaranteed cache residence or superiority over global loads.

## Main files

| Path | Purpose |
|---|---|
| `src/gambit_cuda.cu` | Native texture/global CUDA backend, warp packing, reductions and checks |
| `include/gambit/model.hpp` | The finite integer transition law shared by C++ and CUDA |
| `src/host.cpp`, `src/cpu_main.cpp` | Strict binary loader, reference, canonical little-endian writer |
| `tools/reference.py` | Independent Python specification, not a native-code wrapper |
| `tools/verify.py`, `AGENTS.md` | Fail-closed laptop/Codex verification procedure |
| `assets/*.gblut`, `assets/*.json` | Complete XX/XY verification and laptop seeds / packed field atlases |
| `assets/golden_traces.json` | Immutable CPU-derived canonical trace hashes |
| `evidence/` | Actual delivery-time tests and CPU traces; hardware status remains NOT_RUN |
| `docs/MODEL_AND_PROOFS.md` | Equations, assumptions and U3-D proof family |
| `docs/MIGRATION.md` | Explicit differences from Edition 3.0 |
| `provenance/*original.zip` | Unmodified Edition 3.0 archive, including its earlier kernel and corpus |

The laptop asset has 512 angular bins, 256 radial bins and 256 steps. It emits 33,554,432 **pulse bits** per run, plus separately packed hinge/event/occupancy planes and parity records. A cell state has multiple integer fields; one output bit is not a lossless encoding of the entire state.

**Scope:** computational self-reference here means causal re-use of the engine's own output. It is neither source-code self-modification nor evidence of sentience, biological identity, universal physical determinism or a spiritual ontology. The broader theory remains in the preserved manuscript. This companion implements a finite integer specialization, not a claimed numerical-equivalence port of the floating-point Edition 3.0 simulation.

**Privacy:** this release contains the supplied author identifier/date and the preserved historical archive. Review before public redistribution.
