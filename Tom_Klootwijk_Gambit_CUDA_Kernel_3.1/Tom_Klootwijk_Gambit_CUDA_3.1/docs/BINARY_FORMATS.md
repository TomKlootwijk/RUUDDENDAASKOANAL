# Canonical binary formats

All integers on disk are explicitly little-endian. No native C++ structure padding is serialized. CSV rows use LF newlines on both Windows and Linux. Runtime timing and hardware metadata are deliberately separate from the deterministic byte streams.

## 1. Packed LUT: `.gblut`

Header: 8 bytes `GBLUT31\0`; uint32 format version 1; uint32 parameter count 19; then nineteen uint32 values in the order below. Header size is exactly 92 bytes.

```text
width, height, levels, start_level, steps, threshold,
feedback_gain, memory_divisor, phase_stride, feedback_angle,
open_shift, closed_shift, reaction_uv_shift, reaction_vu_shift,
growth_dwell, growth_divisor, seed, pair, device_budget_mib
```

The payload contains `levels * height * width` uint32 texels in generation-major, radial-major, angular-minor order. The low 16 bits are `signed_field_code + 32768`; the high 16 bits are the clamped field drive. `pair=0` selects XX and `pair=1` selects XY as symbolic configuration labels. It is not a chromosome data format.

The paired JSON manifest adds the SHA-256 digest, chart and bake metadata, complete grammar words and author attribution. Runtime arithmetic is determined by the actual validated header and texel bytes. The verifier compares them against the manifest, then against expected traces. The binary loader itself validates magic, header/version, safe parameter ranges and exact file length, but is not a cryptographic authenticator.

## 2. Packed one-bit words: `words.bin`

Header: 8 bytes `GBWORD31`, followed by five uint32 values: angular width, radial height, step count, storage-plane count (=5), words per plane (=N/32). Header size is 28 bytes.

Each timestep contains five consecutive arrays of N/32 uint32 containers:

| Storage plane | Content | Meaning of lane j in container w |
|---|---|---|
| 0 | Pulse bits | q for cell `32*w+j` |
| 1 | Latch bits | New persistent hinge state |
| 2 | Latch-event bits | Old hinge XOR new hinge |
| 3 | Occupancy bits | Effective sampled field <= 0 |
| 4 | Parity records | The whole uint32 is 0 or 1, parity of pulse word w |

Planes 0-3 are genuinely bit packed. Plane 4 is a parity-record array, not 32 independent parity bits in each word. Parity is stored separately from pulses so it does not corrupt the pulse-density certificate. Latch or occupancy bits do not replace pulses in codec counts.

A textual rendering prints bits in increasing cell order: bit 0 first. This is deliberately the reverse of the usual most-significant-bit-first human display of an integer. `tools/show_words.py` implements the canonical cell order. File size is `28 + steps * 20 * (N/32)` bytes.

## 3. Complete final state: `state.bin`

Header: 8 bytes `GBSTAT31`, then uint32 N. Every cell contributes six uint32 fields (`u`, `v`, `z`, `memory`, `residual`, `flags`) followed by two uint64 fields (`total_input`, `total_output`). Each cell is 40 bytes. Three uint32 control values (`step`, `level`, `last_growth`) follow all cells. Total file size is `24 + 40*N`.

Flag bit 0 is latch, bit 1 pulse, bit 2 occupancy and bit 3 latch event. All other flag bits are zero. All cells initially have zero flags, zero codec residual/counts, and z=memory=32768. Initial U and V are determined by the declared mixer and the initial level's quantized occupancy.

The final state supports per-cell `65536*total_output + residual == total_input`. `tools/check_trace.py` independently re-counts the emitted pulse bits per cell, checks latch-event telescoping and every parity record, compares final flags and verifies total mass/state consistency.

## 4. Summaries and expected hashes

`summary.csv` contains step, used/next generation, growth, counts, species totals, cumulative codec totals and error flags. `run.json` records backend, run options and nondeterministic operational metadata. `golden_traces.json` hashes only `words.bin`, `state.bin` and `summary.csv` for its disclosed cases.

A final-state certificate is not by itself an independent reconstruction of every prior coverage input. For that, execute the deterministic reference and compare states at every step, as the GPU verifier does, or use the independent Python specification on the disclosed small cases. A SHA-256 manifest proves equality with an expected file digest; it does not establish semantic correctness or authentication against replacement of both data and digest.
