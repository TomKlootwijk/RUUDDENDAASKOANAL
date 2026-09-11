# Canonical binary contract — 4.0

All unsigned byte-aligned integers are little-endian. There is no native-struct
padding, pointer or timestamp. The normative implementation pair is
`src/capsule.cpp` and `tools/reference.py`.

## Self-contained restart capsule (`*.gbc`)

| Offset | Bytes | Field |
|---:|---:|---|
| 0 | 8 | ASCII `GBCLOS40` |
| 8 | 4 | Format version = 1 |
| 12 | 4 | Embedded LUT byte length |
| 16 | 4 | Feedback mode, 0 or 1 |
| 20 | 4 | Initialized material total M0 |
| 24 | 4 | State bit length = 27 + 118*N |
| 28 | 4 | Reserved = 0 |
| 32 | variable | Complete original GBLUT31 bytes |
| following | ceil(state_bits/8) | Packed state |
| final | 32 | SHA-256 of all preceding bytes, standard digest byte order |

The state stream appends phase (11 bits), level (3), cooldown (13), then the
following fields for each cell in row-major order: U (32), V (32), z (17), memory
(17), residual (16), flags (4). Each field is least-significant-bit first. The
stream fills each byte from its least-significant bit. Fields are not byte-aligned.
The final five unused bits are zero; nonzero padding is rejected.

Flags: bit 0 latch; bit 1 previous pulse; bit 2 occupancy; bit 3 previous latch
change event. These represent different observations. The previous packed pulse
cache is reconstructed from flag bit 1. Old cumulative audit counters and scratch
buffers are not serialized because they do not drive the next state.

For N divisible by 32 and G levels, the exact total byte length is
`160 + 4*G*N + 118*N/8`. At N=131072, G=5 it is 4554912 bytes.

The loader rejects malformed magic, length, format, padding, digest, asset,
parameter bounds, initial mass descriptor or operative state invariants. Its
256 MiB input bound is part of this file implementation. The digest is unkeyed:
an adversary can replace both data and digest. A valid digest is not authentication.
A valid state capsule is not, alone, proof of reachability from its declared seed.

## Frozen LUT asset (`*.gblut`)

The embedded asset is byte-for-byte the same format as engineering 3.1:
ASCII `GBLUT31` followed by a zero byte (8 bytes total), then u32 version 1,
u32 parameter count 19, then these 19 u32 values in order:

```text
width, height, levels, start_level, steps,
threshold, feedback_gain, memory_divisor, phase_stride, feedback_angle,
open_shift, closed_shift, reaction_uv_shift, reaction_vu_shift,
growth_dwell, growth_divisor, seed, pair, device_budget_mib
```

The header is 92 bytes. The remaining `4*levels*width*height` bytes are texels,
level-major, then radial row, then angular column. Each u32 texel has a low 16-bit
biased signed-field code (`d = low16 - 32768`) and a high 16-bit drive code.
`steps` is inherited seed metadata, not an absolute operational clock. CLI logging
length is explicit. `pair` is a symbolic profile designation, not a biological law.

## Boolean-plane trace (`words.bin`)

Header: ASCII `GBWORD40` (8 bytes), then u32 width, height, logged update count,
plane count 5, and words per plane `N/32`. Total header = 28 bytes.

Each update has five arrays of N/32 u32 values, in order:
pulses, latches, events, occupancies, pulse-word parities.
In the first four arrays, bit j denotes cell `32*k+j`; unused cells are absent
because N is divisible by 32. The last array has one u32 value 0 or 1 for each
pulse word; its other 31 bits are zero. This is parity of 32 data symbols, not
32 further independent bits. Updates are stored in chronological order.

The exact file size is `28 + steps*5*(N/32)*4` bytes. There is no waveform sample
rate or physical output binding. A log record is not a hardware driver command.

## Segment counters (`counts.bin`)

ASCII `GBCOUNT4` (8 bytes), u32 N, then for each cell:
segment-start residual u32, sum K of new activity u64, count Q of pulse ones u64.
The file is exactly `12+20*N` bytes. Verify
`65536*Q + final_residual == start_residual + K`.
K and Q are observer counters scoped to this finite logged segment, not recurrence
state. A resumed run starts new observer counters but retains the incoming residual.

## Summary (`summary.csv`)

UTF-8/ASCII, LF newlines, decimal integers, comma-separated header:

```text
tick,phase,level,cooldown,pulses,latches,mass_u,mass_v,input_sum,pulse_sum
```

`tick` is zero-based within this log segment. Phase, level, cooldown are the
post-update control values. `pulses` and `latches` are counts in the current output;
`input_sum` and `pulse_sum` are cumulative segment totals over all cells. They
restart in a new log segment, unlike operative state. `run.json` reports backend
and verification scope and is not included in the five-file conformance target.

The five consensus files are `initial.gbc`, `final.gbc`, `words.bin`, `counts.bin`,
and `summary.csv`. Matching means byte-for-byte equality, not approximate values.
