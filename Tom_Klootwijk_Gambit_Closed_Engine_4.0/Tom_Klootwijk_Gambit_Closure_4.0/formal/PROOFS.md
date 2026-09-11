# Supporting proofs C1–C16


## C1. Initialization and finite addressing

The admitted dimensions give $N\le2^{22}$ and at most $5N$ texels. The index $(gR+y)A+j$ is bounded by $5N-1$, so it fits an unsigned 32-bit index. At initialization, the deterministic unsigned mixer and frozen occupancy mask uniquely assign nonnegative material and set $z=m=D/2$, $r=0$ and flags zero. A nonempty mask gives $M_0>0$; the loader rejects an empty one.

The phase, generation and cooldown are initialized inside their bounds. Every read refers to a declared old cell, derived word, parameter or immutable texel. The explicit zero-total material branch prevents division by zero. The signed memory divisor is strictly positive. Thus every operation in one transition is defined.

## C2. Finite generative closure

Every grammar symbol has exactly one replacement. Parallel rewriting of a finite word produces one finite word, and every inserted branch bracket is balanced. Counting drawing symbols gives $n_{g+1}=3n_g$ and $n_0=2$. The interpreter and finite generation cap therefore give a finite collection of geometric samples.

Online growth chooses one of those stored levels; it does not allocate an unbounded branch tree. This proves closure of the released generative **selection** mechanism. It does not prove an infinite geometric continuum or biological growth beyond the specified interpreter.

## C3. Shared edge law and material nonnegativity

A node has at most four neighbors. Every nonzero outward transfer is at most $M_i/8$, so the sum of outward transfers is at most $M_i/2$. Hence $M_i-\sum_jJ_{i\to j}\ge0$. Incoming transfers are nonnegative, so every transported count is nonnegative.

Both endpoints determine edge activity and its divisor from the same old samples and old latch pair. Each directed amount occurs once with a minus sign at its source and once with a plus sign at its destination. Summing over all cells cancels every internal transfer. The radial boundary has no exterior transfer to cancel. Thus each species' global total is conserved during transport.

## C4. Local reaction preserves the total

The admitted positive reaction shifts imply $0\le A_i^{\rm rxn}\le\widetilde U_i$ and $0\le B_i^{\rm rxn}\le\widetilde V_i$. The two new species are therefore nonnegative. Adding their equations cancels both local transfers and gives $U_i'+V_i'=\widetilde U_i+\widetilde V_i$.

Combining this identity with C3 proves global conservation of $M_0$. Every individual species count is consequently at most $M_0<2^{32}$, justifying its storage width. No saturation of a material count is needed to conceal an underflow or overflow.

## C5. Recurrence, memory and intermediate arithmetic bounds

The clipped field drive lies in $[0,D]$. For positive local total, $0\le DU'/(U'+V')\le D$; the zero-total fallback is also in the interval. Each recurrence is the floor of a convex combination of bounded nonnegative integers. Therefore $v,z',m'$ remain in $[0,D]$.

The signed memory offset has magnitude at most 32768. The effective field lies in $[-65536,65535]$. All sample-drive intermediates fit signed 32-bit arithmetic, with wider operations used where specified. The material numerator is smaller than $2^{48}$; the growth comparison is at most $2^{38}$. The 64-bit intermediates suffice. Transport and reaction sums are bounded by the proven material invariant rather than a floating-point estimate.

## C6. One-bit codec closure and the prefix identity

Since $0\le r<D$ and $0\le k\le D$, $0\le r+k<2D$. Consequently the threshold selects a Boolean $q$, and subtracting $Dq$ leaves $0\le r'<D$. Rearrangement gives $Dq+r'=r+k$.

Summing over any finite segment cancels every intermediate residual and gives U4's certificate. It uses ordinary mathematical sums for the observer; it does not require those sums as operational registers. The arbitrary-segment discrepancy is

$$
Q_i(t)-K_i(t)/D=(r_{i,0}-r_i(t))/D,\qquad
\left|Q_i(t)-K_i(t)/D\right|<1.
$$

From the original zero residual, the stronger one-sided bound is $-1<Q_i-K_i/D\le0$. After a checkpoint restart with nonzero residual, the one-sided bound is not generally valid; the segment formula is the correct certificate.

## C7. Hysteresis and event closure

A positive threshold makes $F\le-H$ and $F\ge H$ disjoint. Each outer case assigns a bit; the middle case inherits a valid old bit. Thus the latch remains Boolean, including both endpoint equalities.

The XOR of successive events cancels each intermediate latch twice:

$$
\bigoplus_{n<t}e_i(n)=\ell_i(0)\oplus\ell_i(t).
$$

This is an event-history identity, not error correction. Occupancy remains a separately defined Boolean sign test and does not overwrite hysteresis memory.

## C8. Exact packing and the limit of parity

For a Boolean plane, distinct positions occupy distinct powers $2^j$, $0\le j<32$. OR-combining them and then extracting position $j$ returns the original bit exactly. Reading the previous pulse from this packed array therefore recovers the corresponding flag bit without approximation.

Word parity is the XOR of its data bits. Flipping error mask $e$ changes parity by the parity of $e$, which detects odd-weight masks. Two flipped data bits can preserve parity. A parity reduction cannot recover a word, identify its topological dimension or authenticate its sender. The same indicator algebra can describe symmetric difference without making those stronger claims.

## C9. Bounded phase and cooldown form an exact quotient

In the 3.1 equations without a scheduled intervention, absolute time enters the lookup only as $ns\bmod A$. The last-growth timestamp enters the next growth decision only through whether $n-\text{last}\ge d_{\rm dwell}$. The projection

$$
\pi(n,g,\text{last},\text{cells},K,Q)=
(ns\bmod A,\;g,\;\min(d_{\rm dwell},n-\text{last}),\;\text{operative cells})
$$

therefore retains every value used by the next operative update. The cumulative $K,Q$ are not read by its field, transport, reaction, recurrence or latch equations.

For a nongrowth step,

$$
\min(d,\min(d,e)+1)=\min(d,e+1),\qquad e\ge0.
$$

For a growth step both descriptions reset elapsed dwell to zero. Phase updates agree by modular addition. Hence $\pi T_{3.1}=T_4\pi$ through the older model's admitted finite run domain. The 4.0 law itself continues without an absolute counter beyond that domain. This is a proved reduction of sufficient state, not erasure based only on a common vocabulary.

## C10. One-bit ALU refinement

For bits $a,b,c$, define sum digit $s=a\oplus b\oplus c$ and carry $c'=(a\land b)\lor((a\oplus b)\land c)$. Direct Boolean case analysis gives $a+b+c=s+2c'$. Induction over digit positions proves that the ripple adder implements addition modulo $2^w$.

Bitwise complement plus one gives modular negation, hence subtraction. The borrow recurrence implemented in `boolean.hpp` is unsigned comparison by digit induction. A fixed shift is wire routing. A multiplexer selects one of two bits; repeated selected additions implement multiplication.

For unsigned division, the restoring algorithm maintains remainder $0\le R<d$ while consuming one numerator bit at a time. The trial $2R+a_i$ is less than $2d$. Subtracting $d$ exactly when the trial is at least $d$ yields the next quotient bit and a valid remainder. A $w+1$-bit remainder register prevents loss of the trial's carry. Induction gives the quotient and remainder for every nonzero divisor.

Signed memory division first selects the magnitude, performs positive unsigned division, and restores the sign, which is truncation toward zero. C5 excludes out-of-range mathematical results where modular arithmetic could change the intended value. Substitution of these correct primitives proves equality of the Boolean datapath and the integer transition, including pulse count and bounded-control arithmetic.

The delivered gate backend is a software realization of these one-bit arithmetic operations. Array addressing, loop control, byte conversion, file I/O, validation and hash calculation still use an ordinary host computer. It is not a claim that the CPU or GPU physically has one-bit-wide registers or executes only one-bit instructions.

## C11. Canonical binary state and checkpoint sufficiency

The six operative cell fields require 32, 32, 17, 17, 16 and 4 bits respectively, totaling 118. Phase, level and cooldown require 11, 3 and 13 bits, totaling 27. Fixed field order, widths and least-significant-bit-first serialization define an injective encoding of all admitted states.

Sequential extraction reverses sequential insertion. Unused final padding bits are fixed to zero and rejected otherwise. The capsule also includes the validated LUT header, texel bytes, feedback bit and initial-material descriptor. The loader reconstructs packed output from the flags. Therefore it recovers every causal input needed by the next transition.

For an accepted state, encode/decode is the identity. Induction on subsequent transitions proves exact pause/resume equivalence. Acceptance verifies format, integrity and state invariants; it does not, by itself, prove that an arbitrary correctly re-signed state is reachable from the declared initial seed. Reachability of a checkpoint requires replay or an independently verified trace.

## C12. Autonomous closure, repeated execution and recurrence

C1 and C3-C7 show that each cell operation is defined and invariant-preserving. Modular phase, bounded level selection and saturating cooldown keep control in range. Thus $T_\sigma(\mathcal S_\sigma)\subseteq\mathcal S_\sigma$. Induction gives a unique valid state for every finite mathematical iteration count.

Because $E_\sigma$ is injective, $|\mathcal S_\sigma|\le2^{118N+27}$. Any trajectory of more than $|\mathcal S_\sigma|$ transitions must repeat a state. Determinism then repeats its future, so the orbit has a finite preperiod and a positive period. The proof does not specify a small period, a fixed point or convergence to a conscious state.

This is operational and representational closure. It says nothing about an unlimited real computer, immunity to hardware faults, power consumption, or free energy.

## C13. A genuine SDF representation of the complete state

This is a **new explicit construction** addressing the corpus's request to represent everything as SDF notation. Let $b=(b_1,\ldots,b_B)$ be the complete binary state word. In one-dimensional Euclidean space, define the closed set

$$
\Omega_b=[-\tfrac14,\tfrac14]\;\cup\!
\bigcup_{j:b_j=1}[3j-\tfrac14,3j+\tfrac14].
$$

The permanent anchor makes the empty-bit case nonempty. The intervals are separated. Define its exact signed distance by

$$
d_b(x)=\begin{cases}
-\operatorname{dist}(x,\mathbb R\setminus\Omega_b),&x\in\Omega_b,\\
\operatorname{dist}(x,\Omega_b),&x\notin\Omega_b.
\end{cases}
$$

At the query centre $x=3j$, $d_b(3j)=-1/4$ exactly when $b_j=1$. Otherwise the point is outside all intervals and has positive distance. Hence $b_j=\mathbf1\{d_b(3j)<0\}$, proving that $J:b\mapsto d_b$ is injective with an explicit inverse on its image.

Define $\Psi=JFJ^{-1}$ on that image. Then $\Psi J=JF$, so the same dynamics admit an exact SDF representation. This is not the assertion that an arbitrary implicit polynomial is an SDF, that a Klein-bottle drawing is a physical container, or that scalar functions $\mathbb R^n\to\mathbb R$ automatically compose as endomorphisms. Encoding the state as geometry preserves information; it does not remove the decoding and update work.

\begin{figure}[H]
\includegraphics[width=\linewidth]{manuscript/figures/state_sdf.pdf}
\caption{Exact SDF encoding of eight symbols. A negative query value decodes one; a positive value decodes zero. The permanent anchor at zero makes the all-zero word well-defined. This is a representation of state, not a physical-field claim.}
\end{figure}

## C14. Exact reduced-description criterion

Let $e:S\to Y$ be a proposed reduction and $h:S\to O$ a declared observation. There exist well-defined functions $\bar T:e(S)\to e(S)$ and $\bar h:e(S)\to O$ satisfying $eT=\bar T e$ and $h=\bar h e$ **if and only if**

$$
e(s)=e(t)\Longrightarrow
\big(e(Ts)=e(Tt)\ \text{and}\ h(s)=h(t)\big).
$$

Necessity follows by substituting a common encoded value into $\bar T,\bar h$. For sufficiency, choose any representative of a fibre and define both functions using it; the stated implication makes the choices independent of representative. With external inputs, the same condition must hold for each common input separately.

The complete checkpoint encoding satisfies this condition. The phase/cooldown projection satisfies it for the retained operative observations by C9. The last pulse alone fails even on the full admitted state space. Keep every field except one cell's residual identical, with old $z=D/2$ and the same old pulse. The next activity $k$ is independent of that residual and lies between $3D/8$ and $5D/8$, so $0<k<D$. Residuals zero and $D-k$ are both admitted and produce next pulses zero and one. Their old pulse words agree; their new pulse words do not. This does not assert that both states occur on a particular initialized orbit. The simpler $k=1$, residuals zero and $D-1$ codec counterexample is separately supplied to the solver. Thus the unqualified assertion that one final bit is the entire next seed is not adopted.

## C15. Causal self-reference has an executed witness

In the released verification XY seed, compare two executions identical before tick 3. At tick 3 only, invert the read of the prior output bit at cell 7 in one execution. Do not alter the stored historical word or apply any later intervention.

The recorded runs first differ in operative state at tick 3 and first differ in packed pulse output at tick 7. The difference follows from the previous pulse entering the angular address and direct drive. This is a constructive witness that the engine consumes and responds to a descriptor of its own earlier output.

The claim is not that every bit perturbation must spread, nor that feedback implies a quine, self-modifying source code, unrestricted self-proof or subjective experience. The ordinary $T_\sigma$ remains the unperturbed autonomous map; the intervention is a separate experimental operation.

## C16. Conditional CUDA refinement and the trusted boundary

The CUDA source prepares each sample from completed old state and immutable LUT data, then advances one next cell per thread. Warp ballots pack completed flag bits; padded lanes contribute false and participate in every ballot. The input size is a multiple of 32. Each valid packed word has a unique writer.

Sequential kernel launches and completed device-to-host copies establish the required stage order. The host then computes the same bounded control and verifies the local count and material invariants. The checked GPU executable compares every new state, word and control value against the native reference.

For the admitted dimensions, integer texel centres plus one half are exactly representable by binary32. The texture is unsigned integer data with point sampling and element-type reads. Those are the intended CUDA API semantics. [N1] The compiler, runtime, driver and physical hardware must still honor them. The written refinement argument and CPU tests are not a proof of those components. Local GPU compilation, LUT readback, differential runs and instrumentation remain separately required.

