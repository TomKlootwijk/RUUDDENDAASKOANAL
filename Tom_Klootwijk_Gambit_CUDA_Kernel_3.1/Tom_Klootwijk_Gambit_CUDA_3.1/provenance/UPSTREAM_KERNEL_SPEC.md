# Gambit 3.0 — executable kernel specification

**Author: Tom Klootwijk · NL200678942 · 10-07-1990**

## 1. State, seed and types

The alphabet is the immutable set `Σ = {X, Y, +, -, [, ]}`. `Σ*` is its finite-word set. A complete seed `σ` belongs to an admissible seed family `𝔖_N`, not to the alphabet. The JSON seed supplies all model and hinge fields explicitly, together with alphabet, grammar and schema. Versioned code supplies the interpreter, initial concentration and probe laws, numerical conventions, matrix construction and tie rules. Documentary `author`, `engine`, `interpretation` and `scope` fields are not numerical inputs.

The current schema is `ksfe-gambit-seed-3.0`; the model version is `3.0.0`. Duplicate JSON keys, unknown top-level fields, omitted model or hinge fields, unsupported alphabets/grammars and invalid numerical values are rejected. Resource bounds are finite. The complete machine includes the provided code and its arithmetic environment, not only the JSON bytes or a random integer.

A `GambitState` contains node mass arrays `u`, `v`; the stored Boolean active-node mask; three-dimensional fast state `z`; three-dimensional memory; generation, last-growth and step counters; an integer dyadic accumulator; and a tuple of three latch bits. `UnifiedState` is the inherited core without that last tuple. Neither is a brain or a quantum state.

## 2. Parallel growth and geometry

`X → X[+X]Y`, `Y → Y[-Y]X`; brackets and turns rewrite to themselves. The axiom is `[a][b]` for ordered pair `ab`. Both X and Y draw a segment. `+`/`-` turn by the declared angle. Brackets save/restore position and heading. The drawing step at bracket depth d is `turtle_step * turtle_shrink**d`. Initial position is the origin, initial heading is upward, and the resulting segments receive the configured scale/translation.

For generation g, drawing-symbol count is `2*3**g`; word length is `5*3**g+1`. A finite symbol budget applies. Bracket order and pair multiplicity are significant.

The boundary field is the minimum of capsule fields and the explicit double-arc/baseline field, clipped to `y >= 0` by a maximum. Capsule radius is positive. Arc thickness is `arc_thickness + memory_geometry_gain*tanh(memory[0])`; configuration constraints make it positive. The nonpositive set is the declared region. Composite negative values are not advertised as exact interior distances of overlapping unions. Neither field sign nor a minimum's derivative singularity establishes a physical quantum event.

## 3. Initial material and recurrent state

The finite grid uses equal represented cell area `h*h`. At position `(x,y)` the initial concentrations are

```
U = 0.1 + 0.8 * exp(-((x + 1.0)**2 + (y - 0.75)**2)/0.18)
V = 0.05 + 0.15 * exp(-((x - 1.0)**2 + (y - 0.50)**2)/0.25)
```

They are multiplied by the initial mask and `h*h` to form mass arrays. Fast state and memory start at zero. Default latch bits are `(0,0,0)`; their initial value is an explicit seed choice, not an inferred biological sex or automatic boundary classification. Codec residual and totals start at zero.

Matrix realizations use NumPy PCG64 and the declared random seed. Gaussian matrices are individually scaled to induced infinity norms `0.35, 0.15, 0.40, 0.30, 0.20` for A, B, C, D and E. Their realizations and all kernel source hashes contribute to the configuration fingerprint.

## 4. Exact accepted-step order

For stored state n, the order below defines the simulation. New memory never retroactively changes a field already sampled in the same update.

1. Compute the boundary growth score from the **stored mask and stored masses**. At a boundary node it is `U/(U+V)`, or zero when the denominator vanishes. Use the largest such value. A growth event requires score at least the threshold, dwell elapsed and generation below the cap. At most one rewrite is selected per update.
2. Compile the field at the selected generation using **incoming** memory. Its `<= 0` samples define the new mask. Reject an empty mask.
3. Conservatively remap U and V to the new mask. Retained nodes keep their mass. Removed-node mass goes to the nearest new active node; exact floating-point distance ties use the smallest index. Newly active nodes receive no invented background mass.
4. Read the **incoming** control latch. With feedback enabled, set multiplier `leakage + (1-leakage)*latch[gate_probe]`; otherwise use one. Multiply crossing-edge memory gates by this multiplier. This causal timing is part of the model.
5. Build directed conservative generators and advance each species by nonnegative substeps. Then apply the locally conservative reversible reaction.
6. Sample the selected field at the prescribed moving probes, still using incoming memory. Mix the bounded field feature with the post-reaction global U fraction to obtain bounded observations.
7. Update z and memory simultaneously from their incoming values using the recurrence below. Encode the new fast-state mean through the integer pulse-density accumulator.
8. Update each binary latch from that step's field sample and its incoming latch. Form the current payload `[latch1,latch2,latch3,growth_bit,pulse]`. Compute even parity separately. Export raw occupancy, latch changes, samples and material/recurrent metrics.
9. Store new masses, mask, recurrent state, memory, generation/counters, accumulator and latch bits. The newly stored memory and latches affect subsequent updates.

The inheritance implementation computes some independent bookkeeping operations in a different textual order, but these operations use exactly the data dependencies above. Neither latch update nor the code framing feeds back into an already executed material step.

## 5. Material operators

The ambient swirl is `v(x,y)=omega*(-y,x)`; its mathematical domain is all of R², while the computation uses only the finite grid. On active neighbor edges, diffusion plus upwind advection gives nonnegative directional rates. The edge gate is shared in both directions, even when advection is directed. Missing exterior edges produce a closed graph, not a calibrated biological membrane.

The column-generator convention is `Q[i,j] = rate from j to i`, with diagonal entries minus the total exit rate. Columns sum to zero. Each transport substep uses `P=I+dt_sub*Q`; the code chooses a substep count targeting `dt_sub*max_exit <= 0.9`. It multiplies by that nonnegative sparse matrix and does not hide negative mass by clipping.

The local reaction is `U -> V` at rate a and `V -> U` at rate b, with update matrix

```
[[1-dt_sub*a, dt_sub*b],
 [dt_sub*a,   1-dt_sub*b]]
```

Substeps preserve nonnegative coefficients. These simulation species have equal declared conserved mass units. Arbitrary chemical reactions, open-system sources or unequal physical stoichiometry are not inferred from this example.

The remap, transport and reaction factors are nonnegative column-stochastic in exact arithmetic. Therefore they preserve total represented mass and are nonexpansive in mass L1 norm **when comparing the same realized operator sequence**. State-dependent masks and gates can select different operators for different trajectories; global hybrid contraction is not claimed.

## 6. Probes, sensing and memory

Let `t = step*dt`, `a = probe_amplitude` and `f = probe_frequency`. The three simulation probes are

```
p1 = (-1 + .08*sin(.7*t), 1.02 + a*sin(f*t))
p2 = ( 1 + .08*cos(.6*t), 1.02 + a*cos(f*t))
p3 = ( .10*sin(.9*t),    .65 + .5*a*sin(f*t + .4))
```

No anatomical measurements are used. For sampled boundary-field values s, `field_feature = -tanh(s)`. Set `fraction = sum(U)/sum(U+V)` or 1/2 when total mass is zero, and `observation = .6*field_feature + .4*(2*fraction-1)`. This is a chosen dimensionless mixture, not an identity of concentration and distance.

```
z_next = (1-alpha)*z + alpha*tanh(A@z + B@memory + C@observation)
m_next = (1-eta)*memory + eta*tanh(D@z + E@observation)
```

For 0 < alpha,eta <= 1, the unit cube is invariant in exact arithmetic. Boundedness does not imply consciousness, permanent memory or contraction of the entire state-dependent loop. Retained geometric IPD/ITD utilities have separate length/time parameters and are not physiological calibration.

## 7. The one-bit hinge, pulse and frame

The hinge threshold is positive. For a sample s and previous bit b:

```
if s <= -threshold: next_bit = 1
elif s >= threshold: next_bit = 0
else: next_bit = b
```

Both threshold equalities are specified. The latch event is `b ^ next_bit`. Raw occupancy is instead `int(s <= 0)`; those bits can disagree inside the hysteresis band. Summing event bits modulo two telescopes to the initial/final bit difference. A threshold-margin certificate is sufficient to preserve the sampled latch trace under bounded sample errors. It says nothing about unobserved events between samples.

Pulse coverage is `(1+mean(z_next))/2`. With denominator `D=2**codec_bits`, nearest-half-up conversion selects integer k in [0,D]. The accumulator implements

```
q = int(residual + k >= D)
residual += k - D*q
```

Its exact certificate is `total_output*D - total_input == -residual` with `0 <= residual < D`. The dyadic prefix discrepancy lies in (-1,0]. The separate ideal real-to-dyadic rounding bound is at most N/(2D), in addition to the strict less-than-one accumulator bound. Binary output does not reconstruct the original full state.

The current payload has **five bits**; parity is a sixth bit. No parity bits are appended to material mass or treated as geometry. Odd bit-flip counts are detected by even parity; even counts can evade it. No encryption or tamper-proof authentication is claimed.

## 8. Quotient checker and edit utilities

`FiniteMachine` requires a nonempty total transition table with indexed input symbols, valid integer successor indices and explicit output labels. `analyse_quotient` receives a partition with contiguous nonnegative block indices. It checks each state against its block's representative, requiring equal current outputs and equal successor blocks for every input. A valid result supplies the quotient table; an invalid result supplies a representative witness. This proves the finite declared target only.

`edit_word` validates both existing and edited turtle programs, rejects unknown symbols or unbalanced brackets and requires a nonempty resulting standalone drawing. Segment translations and reflection closure are geometric demonstrations. No genome editing, molecular protocol or general automatic grammar inference is implemented.

## 9. Failures, resources and reproducibility

Invalid domains, versions, grammars, values and budget exhaustion raise errors; the code does not invent a physical interpretation for rejected input. `results/` contains delivery evidence. Re-execution into a separate directory preserves it. Same-environment tests compare traces and arrays; cross-platform rounding and artifact bytes can differ. The exact integer certificate applies to the k values actually computed.

The reference has no network access, automatic data collection or hardware driver. The mathematical ambient domain can be unbounded, but CPU memory, word length, grid nodes, substeps and run duration are finite.
