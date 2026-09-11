# Explicit migration from Edition 3.0

Author: Tom Klootwijk · NL200678942 · 10-07-1990.

The requested basis is the delivered Edition 3.0 manuscript/kernel and its preserved source corpus. The log-encoded polar LUT/one-bit pipeline is also present on pages 3-6 of the double-arc addendum. Those pages are conceptual source material, not an implementation test. The present CUDA source, binary formats, integer coefficients and verification protocol are newly supplied engineering choices.

## Retained foundations

The alphabet set remains Sigma = {X,Y,+,-,[,]}; a finite word is a sequence, not a set that discards order or multiplicity. The complete seed is a structured machine input, not a solitary selector bit. The ordered XX and XY choices generate `[X][X]` and `[X][Y]`. Parallel productions are `X -> X[+X]Y` and `Y -> Y[-Y]X`; turns and brackets retain themselves. At level g, the number of drawing symbols is `2*3^g` and the word length is `5*3^g+1`.

The offline field uses the actual Edition 3.0 geometric interpreter and its default parameters: turtle step 0.12, angle pi/7, shrink 0.72, translation (0,0.1), capsule radius 0.045, arc radius/spacing 1, and zero-memory arc thickness 0.105. Capsule/arc/baseline minimum composition and the final `y >= 0` clipping are retained. `tools/geometry_v3.py` is a documented extracted subset of the earlier `kernel/core.py`. The complete original file remains in the original archive.

Binary latches, explicit threshold equalities, separate parity, integer pulse-density residuals, bounded memory, feedback and reproducible seeds are retained as ideas and formal interfaces. These are not licenses to equate geometry, chemistry and consciousness.

## Deliberate changes - not an equivalence claim

| Edition 3.0 | Native integer specialization 3.1 |
|---|---|
| Floating Cartesian graph masses and numerical transport substeps | Fixed log-polar graph with integer mass quanta and donor-limited integer transfers |
| Global U fraction and three moving probes | A local post-reaction material fraction plus field observation at every lattice cell |
| Three global hysteresis latches | One latch per lattice cell, packed in a separate bitplane |
| NumPy matrices and tanh recurrences | Explicit bounded integer weighted averages, with no floating reduction |
| Incoming memory adjusts arc thickness | Incoming per-cell memory offsets a quantized sampled field |
| Dynamic analytical geometry evaluation | Five frozen level atlases, baked before execution and selected on device |
| Conservative nearest-node remap when active mask changes | Fixed storage lattice; closed/inactive cells retain their mass without moving it |
| State-dependent analytical growth criterion | Global pulse count and dwell select the next pre-baked level |
| Five-bit payload plus parity at each global step | Four packed per-cell bitplanes; parity of each 32-pulse word is separately stored |
| Continuous coordinates and analytical utilities | Finite native log-polar cell addresses; origin and infinity are not represented |

The transport graph uses angular wrap and closed radial ends. Its rates are defined on graph adjacency, without polar metric/area factors. Therefore it is not a claim to discretize a physical polar Laplacian, calibrated diffusion, advection or chemistry. The two species are abstract, equally counted model mass units. The positive-total guard and exact divisors define their behavior.

No stochastic dither is used. Deterministic pulse-density encoding provides an exact dyadic count certificate; it does not promise blue-noise statistics, audio quality or lossless recovery of a continuous field. The 32-bit seed mixer is only a reproducible initializer and is not cryptography.

## Source-to-code boundary

The corpus's terms “Word”, “quintessence”, spiritual interpretation, bodily analogy and consciousness remain documentary in the preserved Edition 3.0 corpus. They do not enter CUDA device selection, numerical coefficients or verification criteria. The author's name, identifier and supplied date are attribution metadata rather than secret numerical keys.

The archive is preserved as source history, not endorsed wholesale. Earlier unsupported or conflicting statements remain governed by the audits in Edition 3.0. This companion neither reinstates those assertions nor rewrites the user's corpus to make it appear to support a GPU result.

U3-D below is a theorem about the newly specified integer transition. Its relationship to the earlier model is structural and explicitly mapped above. No simulation-error theorem or exact behavioral quotient from the full Edition 3.0 state has been demonstrated. The exact CPU/GPU equivalence target is within U3-D, conditional on the CUDA implementation and hardware satisfying the stated execution contract.
