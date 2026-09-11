# Tom Klootwijk Gambit — Unified Closure Theorem U4


## Statement

**Fix a complete admitted seed, immutable LUT bytes and the transition just defined. Assume exact execution of the stated integer operations, complete and ordered old/new stages, sufficient allocated memory and no hardware faults.** Let $\mathcal S_\sigma$ be the product states satisfying the state bounds and fixed positive material total.

Then $T_\sigma$ is a uniquely defined endomorphism of $\mathcal S_\sigma$. For every $n\in\mathbb N$, $T_\sigma^n(S_0)$ exists within that domain. It conserves global material, keeps recurrence and codec state bounded, and emits a uniquely determined sequence of Boolean planes.

There is an injective canonical operational encoding

$$
E_\sigma:\mathcal S_\sigma\longrightarrow\{0,1\}^{B},
\qquad B=118N+27,
$$

with an exact inverse on its image. On that image,

$$
F_\sigma=E_\sigma T_\sigma E_\sigma^{-1}
$$

is a closed binary-word transition. The documented Boolean arithmetic algorithms realize the same numerical law. Native execution and Boolean execution therefore have the same specified state/output semantics; conformance tests supply implementation evidence for the distributed programs.

For every cell and every finite segment beginning with residual $r_{i,0}$,

$$
\boxed{D Q_i(t)+r_i(t)=r_{i,0}+K_i(t),}
\qquad
Q_i(t)=\sum_{n<t}q_i(n),\quad K_i(t)=\sum_{n<t}k_i(n).
$$

A saved capsule contains the immutable numerical seed and $E_\sigma(S)$, so restoring and continuing has the same future trajectory as uninterrupted execution. The full state word also admits an injective exact-SDF encoding with a conjugate transition. Every autonomous orbit is eventually periodic because its state set is finite.

The concrete witness establishes causal dependence on a read of the engine's own previous output. The last pulse alone is not a sufficient state quotient. These results do not assert subjective awareness, a universal biological law, zero-latency hardware, thermodynamic isolation or unlimited physical operation.

## Evidence levels

The **mathematical conclusion** follows from the supporting proofs below. **SMT results** prove their particular submitted algebraic targets in the solver's semantics. **Regression and differential tests** establish equality on the disclosed executions. A **GPU hardware result** requires local compilation and device tests and is not present in this delivery. None of these categories is substituted for another.


Normative definitions are in the full manuscript; this extract is not standalone axiomatization.
