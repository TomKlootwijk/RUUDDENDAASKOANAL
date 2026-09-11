# Verification scopes and reproduction

Revision 4.0.1 keeps the numerical contract and expected outputs from 4.0.
Current Windows CPU, CUDA, formal, sanitizer, and profiling evidence belongs in
`validation/` and the final verification PDF under `output/pdf/`. Historical
execution counts and delivery limitations below describe the archived 4.0
evidence. `tools/verify.py --cmake-cuda-toolset cuda=12.8` selects the installed
Visual Studio CUDA integration explicitly when running `--hardware` on this PC.
`tests/cuda_contract.cu` exercises the production CUDA error helper, including
single evaluation and exception propagation. `tools/verify_gpu_edges.py` adds
block-64, feedback-disabled, invalid-input, and no-device regression checks.

## Executed evidence

The delivery executes the native C++ suite (338184 checks), the independent Python
suite (24 methods), the Boolean/native/Python five-file conformance tests on four
small profiles, and two laptop-sized native trajectories with independent trace
audits. It also executes 22 expected-UNSAT and two expected-SAT SMT targets under
Z3 4.13.3.0, and native tests under GCC, Clang and ASan/UBSan.

The original 3.1 model is compared after projecting absolute time to phase and
elapsed dwell, and discarding audit counters. The complete mathematical argument
is U4/C9; numerical tests cover the disclosed runs, not every state in that proof.
The explicit Boolean path uses software digit arrays; it is not a synthesized
physical gate circuit or a one-bit-wide device ISA.

## Coordinator

`python tools/verify.py --cpu-only --formal` checks the frozen release manifest,
builds C++17 with CMake, runs regression suites, checks six native golden profiles,
compares four with Boolean and independent Python execution, audits the outputs,
checks the 17+47 checkpoint semigroup, runs four invalid CLI cases and the solver.
`--quick` omits laptop profiles and is explicitly labelled quick. `--formal` requires
an already installed Z3 executable or libz3; neither is downloaded.

Exit 0: success at its stated scope. Exit 1: failed check. Exit 2: blocked prerequisite.
The final `verification.json` includes the scope and each subprocess's return code.
Logs are preserved in a new output directory. Expected hashes are never regenerated
by verification. An independent trace audit is narrower than complete replay: it
checks emitted bits, event/parity identities and endpoint certificates; it does not
recover every historical activity input from a final cumulative count.

## Target GPU workflow (not executed here)

`python tools/verify.py --hardware --formal --sanitizers --profile`

Requires the requested NVIDIA RTX 5070 Ti Laptop device at device index 0, a suitable
NVIDIA driver, CUDA compiler supporting sm_120/compute_120 (12.8+), and CMake/C++17.
Instrumentation additionally requires `compute-sanitizer` and `ncu`. Missing tools,
wrong requested device or unsupported capability are not substituted with a CPU run.
The CUDA executable also checks capability and allocatable-device constraints.

The workflow tests integer point-sampled texture objects and global loads, complete
LUT readback, per-step equality with CPU, warp-aligned block sizes, repeat processes,
forced PTX JIT and capsule restart. The verification-oriented GPU implementation
copies state to the host and checks it; it is intentionally not a throughput benchmark.
Compute Sanitizer is requested in memcheck, racecheck, initcheck and synccheck modes.
Nsight's basic reports are captured for both fetch paths; inspect available metrics
and disassembly on the actual device before drawing cache conclusions.

CPU success and conditional source inspection are not GPU execution evidence.
No driverless bare-metal image, precompiled GPU binary or hardware timing guarantee
is supplied. Native CUDA still requires the runtime, driver and physical hardware.

## Trust assumptions

The theorem assumes exact stated arithmetic, sufficient memory, ordered stages and
fault-free execution. Tests additionally trust the compiler/OS/runtime/hardware.
The SMT checks trust the submitted target formulas and Z3; solver proof text is not
independently rechecked by a second proof kernel. There is no proof-assistant claim
covering the entire compiler, C++ standard library, CUDA runtime or GPU.

Checkpoint SHA-256 detects changes against a trusted digest but is not a signature,
encryption, authorship verification or proof of reachability. Parity detects only
odd-weight errors. None of the evidence establishes a biological law, subjective
consciousness, zero-latency photonics or physical perpetual operation.
