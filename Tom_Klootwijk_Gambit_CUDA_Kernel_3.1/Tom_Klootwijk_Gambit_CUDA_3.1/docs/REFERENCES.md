# Source and implementation references

Consulted 11 September 2026. Hardware/API references support engineering facts only; none establishes consciousness or validates the user's interpretive claims.

## Supplied project basis

[S1] Tom Klootwijk, *Gambit Unified Seed-Field Theorem and Theory of Consciousness - Edition 3.0*, supplied 35-page manuscript and accompanying archive. The original ZIP is preserved unchanged in `provenance/Tom_Klootwijk_Gambit_v3.0_original.zip`. It includes its source corpus, theorem U3, audits, Python kernel, configurations and historical evidence. Prior evidence is not presented as a CUDA test.

[S2] Supplied *double-arc-M-with-UU-double-set-SDF-notation-(signed-distance-field).pdf*, 12 pages; particularly pages 1-3 for arc/baseline notation and pages 3-6 for the conceptual log-polar LUT/one-bit pipeline. The earlier source's numerical and physical claims remain subject to the Edition 3.0 audits. Page 6's pseudocode is not an actual native CUDA implementation.

[S3] Supplied *Tom Klootwijk NL200678942 10-07-1990 Gambit.pdf*, 48 pages; specifically pages 13-16 (seed, grammar and field), 21-25 (transport/growth coupling), 38-42 (one-bit versus multiscale distinctions and assertions) and 47-48 (seed/alphabet notation). This is source history and project terminology, not independent scientific evidence.

## Primary hardware and software documentation

[H1] NVIDIA, *GeForce RTX 50 Series Laptops*, specification table. The RTX 5070 Ti Laptop entry lists 12 GB GDDR7. <https://www.nvidia.com/en-us/geforce/laptops/50-series/>

[H2] NVIDIA Developer, *CUDA GPU Compute Capability*. The GeForce RTX 5070 Ti family appears under 12.0. Actual laptop identity/capability is queried locally. <https://developer.nvidia.com/cuda/gpus>

[H3] NVIDIA, *CUDA Compiler Driver NVCC*, CUDA 12.8.1 documentation, GPU architecture/code targets. Explicit `compute_120` and `sm_120` support. <https://docs.nvidia.com/cuda/archive/12.8.1/cuda-compiler-driver-nvcc/index.html>

[H4] NVIDIA, *CUDA C++ Programming Guide*, CUDA 12.8.1, texture/surface memory, texture object API, thread/warp execution and stream ordering. Element-type reads do not normalize values; integer point sampling is distinct from floating linear interpolation; same-kernel write/read texture coherence has restrictions. This package avoids modifying the texture during execution. <https://docs.nvidia.com/cuda/archive/12.8.1/cuda-c-programming-guide/index.html>

[H5] NVIDIA, *Compute Sanitizer User Guide*, tool roles and command-line usage. Racecheck is principally a shared-memory hazard detector. <https://docs.nvidia.com/compute-sanitizer/ComputeSanitizer/index.html>

[H6] NVIDIA, *Nsight Compute CLI User Guide*, metrics, sections, export and profiler operation. Local measurements and their interpretation are still required. <https://docs.nvidia.com/nsight-compute/NsightComputeCli/index.html>

[H7] OpenAI, *Custom instructions with AGENTS.md*. Repository guidance for Codex; this does not supply unavailable local hardware. <https://developers.openai.com/codex/guides/agents-md/>

[H8] NVIDIA, *Blackwell Compatibility Guide*, CUDA 12.8.1, forced-PTX compatibility testing. The generic guide's examples include datacenter targets; this package deliberately uses GeForce `sm_120`, not `sm_100`. <https://docs.nvidia.com/cuda/archive/12.8.1/blackwell-compatibility-guide/index.html>

The concrete integer model, formats, proof family, coefficients, source-to-code mapping, test cases and package layout are the engineering construction supplied in this release. Published API facts and vendor model specifications do not certify that construction without testing.
