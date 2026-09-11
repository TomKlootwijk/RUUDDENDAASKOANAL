# Codex / local hardware verification contract

## Required environment

The task must run in a shell with access to the user's **physical NVIDIA GeForce RTX 5070 Ti Laptop GPU**. A hosted workspace without that device is insufficient. NVIDIA lists the laptop model with 12 GB GDDR7; its device memory actually available to a process is measured at launch, not assumed from the label. The GeForce RTX 5070 Ti family is in compute-capability 12.0, and CUDA Toolkit 12.8.1's nvcc documentation explicitly lists `compute_120` / `sm_120` [H1-H3].

Use CMake 3.24+, Python 3.10+ and a CUDA-supported C++17 host compiler. The package's native runtime does not require Python. The verifier does. CUDA still needs the NVIDIA driver/runtime [H4]. A number printed as “CUDA Version” by a driver utility is not used as proof that nvcc is installed: the script separately executes `nvcc --version` and `nvcc --list-gpu-code`.

On Windows, use the matching Visual Studio developer shell. On Linux, use a CUDA-supported host compiler and the native driver. The scripts do not install dependencies, contact an API, change privileged settings or upload data. Never silently fall back to emulation while reporting GPU success.

## One local command

```text
python tools/verify.py --hardware --sanitizers --profile
```

Open the extracted project directory as the local Codex workspace and ask it to follow `AGENTS.md`. OpenAI documents `AGENTS.md` as repository guidance read before work [H7]. The supplied file asks for verification before edits, preservation of evidence and precise reporting of blocked stages. It does not grant extra access to a GPU that the workspace cannot reach.

Suggested instruction to Codex:

> Read AGENTS.md and verify this release on my RTX 5070 Ti Laptop GPU. Run the prescribed hardware command, preserve the original assets and goldens, and report the raw evidence path. Do not regenerate references to hide failures or claim consciousness from passing software tests.

## What is run

The coordinator checks all files indexed in `SHA256SUMS.txt` before compiling. It builds/tests the CPU code, runs the independent Python tests and native negative-path tests, and recreates the supplied canonical goldens. Every verification-sized trace is compared byte-for-byte with a fresh Python scalar execution. Laptop-sized traces have native expected hashes and exact GPU/CPU state comparisons; the independent scalar Python run is intentionally restricted to the smaller cases.

The GPU stage checks actual device identity, compiler version and architecture target. It builds native `sm_120` code plus a `compute_120` PTX path. Each `--verify` GPU run first reads every LUT texel back through the selected fetch path. It then checks every prepared sample, every cell field, each packed plane, the complete control state and integer summary at every timestep against the C++ reference.

Both XX and XY verification assets run with block sizes 32, 128, 256 and 512. Their N = 2112 cells leave padded thread blocks in the larger launches, while the bit words remain complete. A global-memory fetch backend is compared with the texture backend. Separate checks cover pulse-feedback ablation, a one-bit intervention, both 512-by-256 laptop assets, a fresh-process repeated run and the forced PTX-JIT route.

Compute Sanitizer is invoked with memcheck, racecheck, initcheck and synccheck on the disclosed eight-step XY verification case, with nonzero error exits [H5]. This is finite test coverage, not a proof that every possible input has no defect. Racecheck principally checks shared-memory hazards; absence of its warnings cannot substitute for the old/new global-buffer dependency argument. The script saves PTX and SASS disassembly and collects Nsight Compute reports for both fetch modes [H6].

## Cache evidence and performance interpretation

A texture object proves which API path was requested; generated instructions and profiler counters provide hardware evidence. Neither a source comment nor a repeated SHA-256 digest proves cache residency. Inspect the sampled kernels in the SASS and the texture/global memory workload reports. Record exact toolkit, driver, device, block size, profile, clock/power context and profiler configuration before comparing measurements.

The script requests `MemoryWorkloadAnalysis` and `LaunchStats` and saves the installed section listing. If an installed profiler version lacks these sections or hardware counters are unavailable, record the failure and adapt the *measurement command* explicitly. Do not disable security controls or change driver permissions without authorization. Captured reports still need interpretation; the verifier never asserts a speedup from their existence.

The emitted `wall_ms_including_io_and_oracle` includes host work, file writes and, in verification mode, CPU comparisons. It is **not kernel-only latency** and must not be used as a GPU speed benchmark. Profile the kernel regions separately. No cache-hit percentage, occupancy, register count, throughput, energy saving or nanosecond claim is supplied as a measured result in this release.

## Finite resource policy

The default laptop seed uses 131,072 cells and five field levels. Two state buffers, one sample array, two sets of packed planes and one LUT are allocated; verification temporarily adds a full LUT readback array. The host streams frames to disk rather than accumulating the entire time history in VRAM.

The logical allocation estimate is checked against the asset's 2048 MiB cap and 60% of currently free device memory. Texture dimensions are checked against device limits. Actual array allocation/layout and driver overhead are implementation-dependent, and CUDA allocation failure still terminates the run. These guards are not a claim that all supported maximum-size jobs meet a laptop's watchdog or thermal budget. Do not turn off the watchdog, overclock or change power limits for this test.

## Reports and failure meanings

Every invocation uses a new output folder. The native writer refuses pre-existing run artifacts, avoiding a stale success file after a failed run. `verification.json` records all command lines, exit codes, case results and instrumentation status. `run.json` distinguishes CPU passes, GPU invariant checks and GPU/CPU exact comparison passes.

Exit 0 means the specifically requested checks passed. Exit 1 means a check failed. Exit 2 means a required tool, device or access condition was blocked. `--cpu-only` can return 0 but reports `CPU_PASS_GPU_NOT_RUN`. `--quick` is explicitly limited and omits laptop-sized cases. A profiler block must not erase already collected functional evidence, nor be mistaken for a complete instrumentation pass.

No CI/cloud assertion, code inspection, CPU replay or symbolic theorem is a replacement for execution on the target device. A successful local run establishes that disclosed software/hardware test configuration. It does not prove consciousness or certify a biological or spiritual model.
