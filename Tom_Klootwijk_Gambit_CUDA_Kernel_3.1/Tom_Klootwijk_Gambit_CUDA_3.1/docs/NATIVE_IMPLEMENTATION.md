# Native kernel implementation

## A finite hardware target, not a placeholder shader

`src/gambit_cuda.cu` contains a native CUDA executable with checked allocations, texture creation, four named device kernels, full state/output checks and canonical binary writers. `include/gambit/model.hpp` contains the bounded integer transition functions compiled for both CPU and device. `src/host.cpp` supplies loading, validation, initialization, the scalar C++ reference and output serialization. It is not an empty framework adapter or an instruction to implement the model later.

This is source delivery, however: it has not been compiled by nvcc in the delivery environment. A source-complete implementation is not the same as an executed GPU binary. Compiler and driver compatibility, code generation, device correctness and physical performance remain local verification obligations.

## Read-only log-polar texture atlas

The five geometric generations are stacked vertically in one two-dimensional unsigned 32-bit CUDA array. A row is an angular strip at a fixed log radius. A generation has `height` consecutive rows. Array width is `width`; array height is `height * levels`. The field-code and drive channels are bit-packed into one texel.

`cudaCreateTextureObject` uses an array resource, point filtering, element-type reads and unnormalized coordinates. The fetch returns an unsigned integer, not a normalized float [H4]. The query integer is converted only to an exactly representable half-integer texel-centre address:

```cpp
return tex2D<unsigned int>(tex,
    float(k % width) + 0.5f,
    float(k / width) + 0.5f);
```

Angular wrap is performed by integer masking before the fetch; clamp addressing is a secondary guard, not the mechanism implementing cyclic topology. Radial indexing remains in range. The texture is immutable for the entire run, avoiding same-kernel texture read/write coherence ambiguities [H4]. Dynamic memory deforms the sampled field code in registers; it does not overwrite cached texture storage.

The alternate `--fetch global` path indexes the same packed bytes through a global-memory pointer. The verifier compares both paths to the CPU. This is a correctness and profiling comparison, not an assumption that texture fetching will outperform a regular load. The GPU's cache behavior must be read from generated instructions and actual profiler evidence.

![The actual distributed generation-four XY field in log-polar atlas coordinates. This is a finite sampled chart, not an infinite axis or a GPU performance measurement.](manuscript/figures/polar_lut.pdf)

\FloatBarrier

## Ordered stages and unique writers

The update sequence has explicit stage boundaries:

```text
incoming state + packed output + control
    -> prepare: point lookup and feedback
    -> advance: transport, reaction, state, words
    -> summarize: integer counts and growth control
    -> write the frame; swap old/new buffers
```

`gambit_prepare` fetches the immutable atlas and applies the incoming memory/pulse law. Each thread writes one sample. `gambit_advance` gathers transport from incoming cells and completed samples, applies reaction, sensing, memory and the one-bit codec, then writes one new cell. Four warp ballots pack the Boolean output planes. Every launched lane reaches every ballot; padding lanes contribute false. Lane zero writes each valid word exactly once.

`gambit_summarize` uses one fixed 256-thread block and a synchronized shared-memory integer reduction. Only its thread zero updates the global control. `gambit_texture_probe`, used before a verified run, fetches every atlas entry through the chosen texture/global path and compares the result against the original host bytes. Probe success establishes those reads for that run, not a universal cache guarantee.

Three update kernels are launched in order in the same stream. The host checks the summary, writes the emitted frame and swaps old/new state and word buffers. No mathematical state is updated in place. There are no floating-point reductions or atomic updates. The shared model header supplies identical integer operations, while the independent Python reference avoids relying only on shared source when validating the smaller cases.

\Needspace{18\baselineskip}

## Resource accounting for the supplied laptop profile

For N = 512 * 256 cells and G = 5 levels, the logical device payload is:

| Allocation | Bytes |
|---|---:|
| Two cell buffers, 2 * 40 N | 10,485,760 |
| One sample buffer, 8 N | 1,048,576 |
| Two sets of five packed/storage planes | 163,840 |
| One unsigned-32-bit field atlas, 4 G N | 2,621,440 |
| Control and report | 76 |
| **Run payload** | **14,319,692** |
| Temporary full atlas probe in verification mode | 2,621,440 |
| **Conservative logical estimate with probe** | **16,941,132** |

The estimate is about 16.16 MiB with the probe. It excludes implementation-dependent texture layout, the CUDA context, runtime and driver allocations. The probe is actually freed before the persistent cell buffers are allocated, so the displayed combined estimate is deliberately conservative for these explicit buffers. Actual free memory is queried, allocation errors are checked, and the default seed cap is 2048 MiB. Reserving the entire advertised 12 GB is neither necessary nor desirable for this audit workload.

The history is written to files rather than retained as all timesteps in VRAM. One laptop-profile `words.bin` is 20,971,548 bytes, including all four packed Boolean planes plus the separate parity records and header. The final state file is 5,242,904 bytes. These sizes are part of the binary format, not a claim of lossless one-bit compression of the complete engine.

## Execution boundaries

The device loop does not evaluate `log`, `sin`, `cos`, continuous SDF distances or L-system string rewriting. Those operations occur in the disclosed offline asset compiler. New dimensions, geometry or coefficients create a new complete seed and require new independently reviewed references. Regeneration of a shipped floating bake can change last-bit rounding and must not be used to hide a mismatch.

This native CUDA path still uses the operating system, NVIDIA driver/runtime, memory allocation, kernel launches, synchronization and host file I/O. It is not driverless firmware or an operating-system kernel. No display, audio actuator, transducer, network endpoint or biological interface is driven by this release. Outputs are model data files.
