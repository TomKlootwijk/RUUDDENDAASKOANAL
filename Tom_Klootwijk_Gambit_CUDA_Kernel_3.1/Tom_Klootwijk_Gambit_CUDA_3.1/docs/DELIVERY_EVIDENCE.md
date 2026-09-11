# Executed evidence and binary self-feedback witness

## Verification status at delivery

The delivery environment had GCC 14.2, Clang 17, CMake 3.31.6 and Python 3.13.5. It did not expose an NVIDIA device, `nvidia-smi` or `nvcc`. Consequently native CUDA compilation, GPU execution, texture-cache measurements and GPU sanitizer results are **NOT_RUN / NOT_MEASURED**. No GPU executable is included. The complete CUDA source and local build/verification workflow are provided for the laptop.

The C++ test executable evaluated **325,550 assertions** and passed. This is one CTest target with many evaluated assertions, not 325,550 independent test functions. The separate Python suite passed **19 test methods**, and the command-line/error-path suite passed **16 negative-path checks**. Release-mode checks use an explicit throwing check function rather than a disabled C++ `assert` macro.

Both GCC and Clang built the CPU implementation and passed its integer contract. Their XX/XY verification traces matched the same canonical hashes. A separate CPU AddressSanitizer/UndefinedBehaviorSanitizer build passed the synthetic contract test. These are CPU tool results, not NVIDIA Compute Sanitizer results.

Four small cases were recreated by both native C++ and the independent Python implementation. Their canonical `words.bin`, `state.bin` and `summary.csv` files matched byte-for-byte. Both laptop-sized native traces were recreated in fresh executions and matched their canonical hashes. Source changes or a new model require a declared revision; the laptop verifier does not overwrite the distributed references.

## Actual CPU trace outcomes

| Case | Cells | Steps | Pulse bits | Ones | Conserved total mass |
|---|---:|---:|---:|---:|---:|
| XX verification | 2,112 | 64 | 135,168 | 49,025 | 86,047 |
| XY verification | 2,112 | 64 | 135,168 | 49,015 | 87,128 |
| XX laptop profile | 131,072 | 256 | 33,554,432 | 12,169,202 | 5,208,103 |
| XY laptop profile | 131,072 | 256 | 33,554,432 | 12,180,402 | 5,217,058 |
| XY pulse-feedback ablation | 2,112 | 64 | 135,168 | 50,864 | 87,128 |
| XY one-bit intervention | 2,112 | 64 | 135,168 | 49,015 | 87,128 |

The two laptop-profile runs contain 67,108,864 pulse bits in total. This excludes the additional hinge, event, occupancy and parity storage. All six disclosed cases reached atlas level four, with the last growth advance at step count 48. The explicit integer trace audits passed. Counts are properties of these supplied discrete examples, not biological measurements.

## The self-feedback counterfactual

The witness uses the released XY verification seed. Both runs have identical initial conditions and remain identical through updates 0, 1 and 2. At update 3, cell 7's read of its prior packed pulse is inverted once. Its stored previous bit was 1; the intervention supplies 0 to that read. No historical pulse is rewritten.

| Cell 7, after update 3 | Baseline | Read intervention |
|---|---:|---:|
| Effective field code | -122 | -106 |
| Prepared field drive | 42,912 | 26,272 |
| Fast state z | 33,813 | 30,693 |
| Memory m | 32,601 | 32,406 |
| Codec residual r | 62,462 | 59,342 |
| Material U / V | 82 / 51 | 82 / 51 |
| Accumulated ones | 1 | 1 |

The first state divergence is therefore update 3. The first differing packed **pulse** bit occurs at update 7. Both complete 64-step runs happen to contain 49,015 ones: a total count can hide changes in timing and internal state. This distinction is why full words and states, not merely an aggregate checksum of counts, are compared.

The full witness is in `evidence/feedback_witness.json`; `tools/feedback_witness.py` independently reproduces it. The ablation also changes the output trace. These experiments demonstrate causal re-use of the engine's output as an input. They are not a test of subjective awareness.

![Independent Python witness: cell 7's fast state differs after a single packed-feedback read is changed. The plotted update range is 0-25; the evidence file contains all 64 updates.](manuscript/figures/feedback_state.pdf)

![Frame-level pulse differences caused by the one-read intervention. Zero at an update does not imply equality of the hidden integer state.](manuscript/figures/feedback_bits.pdf)

\FloatBarrier

## Words that can be inspected directly

`tools/show_words.py` prints a selected packed word in increasing cell-offset order: its leftmost printed character is bit 0, not bit 31. For the XY verification run, word 17 covers cells 544 through 575. The following are the first eight **pulse-plane** words, produced by the CPU reference:

```text
step 0   00000000000000000000000000000000
step 1   00000000000000000000000000000000
step 2   11111111111111111111111111111111
step 3   00000000000000000000000000000000
step 4   11111111111111111111111111111111
step 5   00000000000000000000000000000001
step 6   11111111000000000011111111111110
step 7   00000000111111111100000000000011
```

The complete text excerpt additionally shows latch/event words and parity. These are data from an actual finite execution. The GPU is required to reproduce exactly these canonical words for the same seed and options, not simply generate visually similar patterns.

## What the evidence does not establish

The test suite is finite and the mathematical proofs depend on the stated model assumptions. No proof assistant has verified the C++ compiler, CUDA compiler or GPU. The original theory's physical, sensory and spiritual interpretation remains separate from this model. No result here establishes universal one-bit biology, a consciousness detector, infinite resolution, zero latency, or a measured texture-cache speedup.
