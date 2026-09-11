# Release statement

## What is finalized

This edition formalizes the **Tom Klootwijk Gambit** as a closed, deterministic, seed-based numerical machine with a one-bit output alphabet, an executable Boolean arithmetic realization, and a complete binary checkpoint. The author attribution is **Tom Klootwijk, NL200678942, 10-07-1990**, as supplied for this project.

The central result is **Unified Closure Theorem U4**. Once a valid complete seed is fixed, the next operational state depends only on the current operational state. The state remains inside an explicitly bounded domain for every mathematical iteration. There is no growing timestep, no accumulating diagnostic counter required by the recurrence, no runtime random source, and no omitted mutable lookup asset.

The release retains the actual geometry, transport, reaction, recurrent memory, latching and pulse-density laws of the native 3.1 engineering model. It closes their control representation rather than replacing them with an unrelated automaton. A sufficient-state projection explains exactly which older fields may be removed without changing future output. [E31]

The word *unified* refers to a single specified transition over a coupled product state. The word *one-bit* refers to Boolean symbols, bit-register arithmetic and an exact binary state encoding. It does **not** mean that the entire engine has only two possible states. A one-bit pulse and a complete word of many bits have different information capacities.

The accompanying source contains a native C++17 implementation, an explicit one-bit Boolean ALU implementation, an independent Python specification, and a conditional CUDA implementation using the packed log-polar LUT. The numerical CPU and Boolean results are executed evidence. The CUDA source was not compiled or run in the delivery environment: neither `nvcc` nor an NVIDIA device was available.

## Relationship to the supplied corpus

The latest 36-page corpus develops four proposed closure arguments: functional closure, topological closure, parity feedback and temporal closure. It also relates the engine to consciousness, memory and biological growth. Its page 33 illustration depicts a root, recursive branches and a dashed boundary, but it does not specify an executable transition or establish physical closure. Its pages 35-36 state a stronger verdict than the preceding equations prove. [C, pp. 25-36]

This edition preserves that vocabulary while distinguishing **source claims**, **new mathematical constructions**, **executed software evidence** and **interpretation**. In particular, it adds a valid construction through which every complete binary state can be represented by a genuine signed distance field. That representation does not turn every original operator into the same function, establish consciousness, remove execution costs, or implement the corpus's proposed acoustic or photonic hardware.

The program is an **offline numerical research kernel**. It writes state and verification files. It has no transducer, amplifier, laser, audio-output, human-targeting or physical-actuator interface.

## Closure in one equation

Let $\mathcal S_\sigma$ be the admitted operational states for complete seed $\sigma$. Let $E_\sigma$ encode each such state into a fixed-length binary word. The central commuting relation is

$$
\boxed{\quad T_\sigma:\mathcal S_\sigma\to\mathcal S_\sigma,
\qquad F_\sigma E_\sigma=E_\sigma T_\sigma.\quad}
$$

The machine and its binary realization describe the same next-state operation. A second encoding, $J$, embeds the binary word as an exact SDF. Its conjugate transition satisfies $\Psi J=JF$. Each composition is defined on a specified domain; equality of informal labels is not used as a proof.

# Complete seed, geometry and operational state

## The seed is a structured specification

The generative specification is

$$
\sigma=(\Sigma,\omega,P,I,\Theta,L,S_0,V).
$$

Here $\Sigma$ is the alphabet **set**; $\omega$ is an ordered seed word; $P$ is a total parallel rewriting map on that alphabet; $I$ is the geometric interpreter; $\Theta$ gives admitted parameters and exact arithmetic semantics; $L$ is the frozen packed LUT; $S_0$ is the initialized operational state; and $V$ identifies the implementation/specification version. The author identifier is documentary attribution, not a physical constant or a source of numerical validity.

For execution of this frozen release, the effective numerical seed consists of the validated LUT header and bytes, the feedback-mode bit, the specified initialization rule and the fixed 4.0 transition semantics. The grammar and bake records establish how those bytes were produced. Re-baking is not required to replay them. A different byte array is a different numerical seed even when it is intended to approximate the same continuous geometry.

The retained paired grammar is

$$
\Sigma=\{X,Y,+,-,[,]\},\qquad
P(X)=X[+X]Y,\qquad P(Y)=Y[-Y]X,
$$

with the punctuation symbols rewriting to themselves. The axioms are $[X][X]$ and $[X][Y]$, labelled XX and XY. These are symbolic configurations, not a complete classification of chromosomes, biological development or human identity. Each drawing symbol produces three drawing symbols, so generation $g$ has $2\cdot3^g$ drawing symbols. Parallel rewriting and turtle interpretation are different operations. [E31; AB]

The source's later $\alpha,\beta,\gamma$ sketch is retained as a source motif rather than silently substituted for this grammar: it does not supply the complete interpreter and transition contract. The actual frozen turtle shrink factor is **0.72**, not an asserted universal golden-ratio value. [C, pp. 30-34; C22-C24 in the accompanying audit]

## What the LUT contains

The released full charts use radial endpoints $1/32$ and $4$, in dimensionless simulation units. With $A$ angular columns and $R$ radial rows,

$$
\rho_y=\log(1/32)+\frac{y}{R-1}\log(128),\qquad
\theta_x=\frac{2\pi x}{A},\qquad
p_{yx}=e^{\rho_y}(\cos\theta_x,\sin\theta_x).
$$

The origin is excluded. Neither the radius axis nor its resolution is infinite in the implementation. The tiny `micro` fixtures are explicitly recorded subsamples of the frozen verification charts, not new full-range chart bakes.

At each of the five available generations, the inherited interpreter combines capsule branches with the double-arc M and baseline construction, then clips at the stated baseline. A capsule primitive has the distance formula

$$
\begin{aligned}
\lambda(p)&=\operatorname{clip}_{[0,1]}
  \frac{(p-a)\cdot(b-a)}{\|b-a\|^2},\\
d_{a,b,r}(p)&=\|p-a-\lambda(p)(b-a)\|-r.
\end{aligned}
$$

A degenerate segment is interpreted as a ball around its endpoint. Minimum and maximum constructions preserve the declared union/intersection membership tests; a composite is not automatically an exact interior distance for an overlapping union. The offline floating-point geometry and its discretization are distinct from the exact integer execution that follows. [E31, sections 2 and 7]

For an offline field sample $F_g(p_{yx})$, the frozen code is

$$
\begin{aligned}
d_{gyx}&=\operatorname{clip}_{[-32768,32767]}
 \left(\left\lfloor4096F_g(p_{yx})+\tfrac12\right\rfloor\right),\\
c_{gyx}&=\operatorname{clip}_{[0,65535]}(32768-16d_{gyx}),\\
L_{gyx}&=(d_{gyx}+32768)\;\mathbin{|}\;(c_{gyx}\ll16).
\end{aligned}
$$

A texel is therefore a **32-bit record** containing two 16-bit quantities, not one stored physical bit and not trichromatic spectral data. The unsaturated rounding bound of $1/8192$ field units is relative to the floating sample supplied to the quantizer. It does not certify the error of that sample relative to an exact continuous geometry. The authoritative replay target is the frozen byte array.

## The invariant state domain

Write $D=65536$, $N=AR$, and $M_0$ for the initialized positive total material count. Cell $i$ has operational state

$$
C_i=(U_i,V_i,z_i,m_i,r_i,f_i).
$$

The two material counts are nonnegative integers with a fixed global sum $M_0<2^{32}$. Fast activity and memory satisfy $0\le z_i,m_i\le D$; the pulse residual satisfies $0\le r_i<D$. The four-bit flag $f_i$ stores latch, previous pulse, occupancy and previous latch event, in that bit order.

The only global mutable control is

$$
K=(a,g,c),\qquad
0\le a<A,\quad g_0\le g<G,\quad 0\le c\le d_{\rm dwell}.
$$

Here $a$ is an integer phase offset in angular bins, $g$ is the current baked generation and $c$ is a saturating dwell counter. The mathematical iteration index $n$ labels a trajectory; it is **not** an unbounded register of the machine.

The packed output words are exactly reconstructible from the flags. They are a derived cache rather than independent state. Temporary samples, old/new scratch buffers, report sums and accumulated audit counters are likewise not additional causal inputs. The native implementation retains the older 40-byte `Cell` storage layout for compatibility, but its two old audit-counter slots are always zero in the closed operational state.

The parameter validator admits power-of-two $A$ from 32 to 2048, $R$ from 2 to 2048, one to five baked levels, positive dwell at most 4096, and the integer ranges specified in the source. $N$ is divisible by 32. The initial material mask must be nonempty. The complete parameter contract is enforced before execution, not assumed from a filename.

# Normative transition: the entire operator chain

This section defines $T_\sigma$. All quantities on a right-hand side are incoming values unless explicitly marked with a prime. Each global update prepares all samples, advances all cells from the old arrays, packs outputs and then updates bounded control. No in-place neighbor update is allowed.

## Read the previous word and sample the field

For cell $i$, decode its own previous pulse from the packed output cache:

$$
q_i^-=
\left(W_{\lfloor i/32\rfloor}\gg(i\bmod32)\right)\mathbin{\&}1.
$$

With pulse feedback enabled, sample angular column

$$
j_i=(x_i+a+q_i^-s_{\rm fb})\bmod A,
\qquad x_i=i\bmod A,\quad y_i=\lfloor i/A\rfloor.
$$

The field sample comes from $L_{g,y_i,j_i}$. Decode its signed code $d_i$ and unsigned drive $c_i$. Incoming memory gives

$$
\begin{aligned}
h_i&=\operatorname{trunc}_0((m_i-D/2)/d_m),\\
F_i&=d_i-h_i,\\
A_i&=\operatorname{clip}_{[0,D]}
 \left(c_i+16h_i+\gamma(2q_i^--1)\right).
\end{aligned}
$$

Signed division truncates toward zero, including negative numerators. The frozen default values include $s_{\rm fb}=3$, $d_m=256$ and $\gamma=8192$. These are declared model coefficients, not measured biological or acoustic constants.

The feedback-mode bit is immutable within a seed. At mode zero, the pulse-dependent angular offset, memory offset and direct pulse-drive term are removed. Latching, material evolution and pulse-count-controlled growth still exist. This is a **pulse-feedback ablation**, not the removal of every recurrent loop.

A one-read intervention used in testing is not ordinary autonomous operation and is not silently injected into this transition. Its time and location are identified in the witness record.

## Gated, conservative graph transport

Each index has angular predecessor/successor with wrap and radial predecessor/successor where present. The radial ends have no exterior edge. This is a fixed graph on chart indices, not an asserted discretization of the Euclidean or log-polar Laplace operator with physical units.

An edge is active only when both sampled fields are nonpositive. On an active edge,

$$
s_{ij}=\begin{cases}
s_{\rm open},&\ell_i\lor\ell_j=1,\\
s_{\rm closed},&\ell_i=\ell_j=0,
\end{cases}
\qquad s_{ij}=s_{ji}\ge3.
$$

For either species $M$, define directed transfer

$$
J_{i\to j}=\left\lfloor M_i/2^{s_{ij}}\right\rfloor,
\qquad
\widetilde M_i=M_i-\sum_jJ_{i\to j}+\sum_jJ_{j\to i}.
$$

Inactive edges carry zero. Every receiving cell gathers from the same completed old state; no endpoint writes into a neighbor. A cell outside the active mask retains its material rather than losing it to clipping. Selecting a new geometric generation does not create material.

## Conservative local reaction

Set

$$
A_i^{\rm rxn}=\lfloor\widetilde U_i/2^{s_{uv}}\rfloor,
\qquad B_i^{\rm rxn}=\lfloor\widetilde V_i/2^{s_{vu}}\rfloor,
$$

and then

$$
U_i'=\widetilde U_i-A_i^{\rm rxn}+B_i^{\rm rxn},\qquad
V_i'=\widetilde V_i-B_i^{\rm rxn}+A_i^{\rm rxn}.
$$

The frozen defaults are $s_{uv}=6$ and $s_{vu}=7$. These transfer rules define the discrete simulation. They are not a calibrated chemical reaction network or a numerical claim that all corpus reaction-diffusion equations have been solved exactly.

## Sensing, recurrence and geometric memory

Post-reaction material contributes the bounded observation

$$
B_i=\begin{cases}
\lfloor D U_i'/(U_i'+V_i')\rfloor,& U_i'+V_i'>0,\\
D/2,& U_i'+V_i'=0.
\end{cases}
$$

The new fast state and memory are

$$
v_i=\lfloor(3A_i+B_i)/4\rfloor,\quad
z_i'=\lfloor(3z_i+v_i)/4\rfloor,\quad
m_i'=\lfloor(15m_i+z_i')/16\rfloor.
$$

The current sample used old memory; the memory update uses the new fast state. This ordering is part of the machine. It provides an operational meaning for *memory shaping a subsequent field*: stored $m_i$ affects the next memory offset $h_i$ and thus later sampling and drive.

## Deterministic one-bit output and the hinge

Let $k_i=z_i'$. The output codec is

$$
q_i=\mathbf1\{r_i+k_i\ge D\},\qquad
r_i'=r_i+k_i-Dq_i.
$$

No random jitter is added and no parity bit is mixed into this pulse. The residual is indispensable state. Its exact local certificate is

$$
\boxed{Dq_i+r_i'=r_i+k_i.}
$$

For positive threshold $H$, the persistent latch is

$$
\ell_i'=\begin{cases}
1,&F_i\le-H,\\
0,&F_i\ge H,\\
\ell_i,&-H<F_i<H.
\end{cases}
\qquad
 e_i=\ell_i\oplus\ell_i',\quad o_i=\mathbf1\{F_i\le0\}.
$$

The frozen threshold is $H=49$ in signed-field code units. A latch, a pulse, an occupancy bit and a latch-event bit have different definitions. In the hysteresis band, occupancy and the retained latch can disagree without an error.

## Pack the word; update phase and growth

Pulses, latches, events and occupancies are packed into four Boolean planes, each with 32 cells per unsigned word and cell zero in the least-significant bit. A fifth array contains one parity value, zero or one, for each pulse word. This fifth array is **not** 32 independent parity symbols per container.

With $P_n=\sum_i q_i$ and phase stride $s$, define

$$
a'=(a+s)\bmod A,\qquad c_*=\min(c+1,d_{\rm dwell}).
$$

If $g+1<G$, $c_*=d_{\rm dwell}$ and $P_n d_{\rm growth}\ge N$, set $(g',c')=(g+1,0)$. Otherwise set $(g',c')=(g,c_*)$. The default stride is one, dwell is 16 and growth divisor is four. A selected generation affects the following lookup. At the last baked level, generation remains bounded; activity, transport and memory continue.

This completes the operator chain. No absolute timestep or total historical pulse count is read by any future cell equation.

### Executable state boundary

The following scheduling outline summarizes the specified stages; the distributed C++ files contain their actual implementations.

```text
step(immutable_seed, old_state):
    old_pulse_words = pack(old_state.flags.pulse)
    samples = sample_all(old_state, old_pulse_words, seed.LUT)
    next_cells = advance_all_from_old_arrays(old_state, samples)
    for each cell i:
        assert D*q[i] + r_next[i] == r_old[i] + z_next[i]
    next_control = bounded_control(old_control, sum(q))
    assert global_material(next_cells) == seed.initial_material
    next_state = (next_control, operative_fields(next_cells))
    return next_state, pack_all_planes(next_cells.flags)
```

The three transition boundaries are implemented by `Engine::tick`, the selected native or Boolean cell law, and `Engine::accept`. `capsule` serializes the resulting state; `from_capsule` reconstructs it and its derived output cache. Neither function infers missing state from a lone parity token.

All seeds and saved states enter through validators. Invalid dimensions, empty initial material, bad bit padding or inconsistent global mass are rejected before they can become an autonomous execution. A failed file write stops the logging process; it is not silently interpreted as another logical state of the model.


# Unified Closure Theorem U4

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

# Supporting proof family

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

# Canonical files and the executable kernel

## Exact state payload

The file `final.gbc` is a standalone restart capsule. It does not need the original external asset file. Its layout is defined in `docs/BINARY_FORMAT.md` and implemented independently in C++ and Python.

| Component | Encoding |
|---|---|
| Envelope | Magic `GBCLOS40`, format version, embedded asset byte count, feedback bit, initial material, state bit count, reserved zero |
| Frozen seed | Original `GBLUT31` header and all generation-major texel bytes |
| Operational state | Phase 11 bits, level 3 bits, cooldown 13 bits; then each cell's 118-bit record |
| Padding | Unused final bits are zero |
| Integrity | SHA-256 of every preceding capsule byte |

All header integers are explicitly little-endian. Within state fields, bit zero is first, and fields are concatenated without alignment padding. The digest uses the standard SHA-256 algorithm. [N2] No native structure padding, pointer, wall-clock timestamp or operating-system handle is serialized.

For $N$ cells and $G$ levels, the capsule length is

$$
160+4GN+118N/8\quad\text{bytes},
$$

because $N$ is divisible by 32. At the laptop profile $N=131072$, $G=5$, the operative word has **15,466,523 bits** and the self-contained capsule has **4,554,912 bytes**. The state is therefore represented in binary without the false claim that all of it fits into a single bit.

## Emitted records and their evidence

`words.bin` contains the four packed Boolean planes plus parity records for each update. `counts.bin` contains each cell's segment-start residual and observed segment totals $K,Q$. `summary.csv` gives deterministic aggregate observations. `initial.gbc` and `final.gbc` delimit the exact run segment. `run.json` identifies the backend and verification scope; it is not a physical-consciousness certificate.

A segment contains at most 4096 logged updates so its observer counters have a simple finite bound. This is an output/logging contract, **not a halt in the operational recurrence**. A final capsule can start the next segment without resetting phase, memory, latches, material or residuals. Segment certificates compose by cancelling the shared endpoint residual.

The trace checker independently recounts emitted pulses, verifies parity, verifies the event telescope and checks the endpoint count certificate. The final $K$ record alone does not reconstruct every historical $k$. Per-step native checks and differential replay supply that separate evidence. Matching hashes certify bytes against an expected digest, not the correctness of every interpretation attached to them.

## Three CPU-level realizations; one conditional GPU path

The **native C++17 backend** is the practical CPU execution path. The **Boolean ALU backend** realizes arithmetic through arrays of one-bit digits, carries, borrows, muxes and a restoring divider. The **independent Python reference** uses unbounded host integers and the stated truncation rules. All three share the frozen seed bytes and canonical file contract, not an imported native arithmetic implementation.

The optional **CUDA backend** uses the native integer cell law with an unsigned texture-object or global-memory LUT path. It deliberately includes host control updates, full readback checks and CPU comparison for verification; it is not presented as a fully optimized persistent GPU engine. Its compiler target is `sm_120` with a `compute_120` PTX path, consistent with NVIDIA's listed 12.0 family and compiler target documentation. [N3, N4] The local verifier must inspect the actual laptop device rather than assume that a model name proves successful execution.

# Executed verification and release evidence

## Results obtained in the delivery environment

The native regression executable completed **338,184 checks**. They include all 65,536 pairs of 8-bit ALU inputs for its specified exhaustive operations, 1,200 deterministic 64-bit input pairs, cross-backend transitions, signed sampling cases, capsule validation and continuation through 10,000 autonomous updates. These are checks with disclosed scopes, not hundreds of thousands of independent scientific experiments.

The independent Python suite passed **24 test methods**. The native suite also passed under Clang and under address/undefined-behavior instrumentation. The record lists the compilers and commands; none of these CPU checks is labelled a GPU run.

The formal suite returned **UNSAT for 22 algebraic counterexample targets** and **SAT for two intentional counterexample targets**. The latter demonstrate the insufficiency of a lone output bit and undetected even-weight parity errors. The installed Z3 C API was used, and all submitted SMT-LIB files and solver logs are included. [Z1, Z2] The logs have not been independently checked by a second proof kernel, and they do not prove the entire C++ or CUDA compiler pipeline correct.

Four disclosed small cases match the native, Boolean ALU and independent Python implementations byte-for-byte across all five canonical output files. Two laptop-sized native cases have independently audited records. The local coordinator compares them against frozen expected hashes; it never regenerates those hashes to make a test pass.

| Case | Cells | Updates | Pulse symbols | Number of ones |
|---|---:|---:|---:|---:|
| Micro XX | 64 | 64 | 4,096 | 1,623 |
| Micro XY | 64 | 64 | 4,096 | 1,603 |
| Verification XX | 2,112 | 64 | 135,168 | 49,025 |
| Verification XY | 2,112 | 64 | 135,168 | 49,015 |
| Laptop XX | 131,072 | 256 | 33,554,432 | 12,169,202 |
| Laptop XY | 131,072 | 256 | 33,554,432 | 12,180,402 |

The precise authoritative counts and digests are in `assets/closure_goldens.json` and the included run files. The table is an execution record of this model, not a sensory or clinical dataset.

## The self-feedback word

For cell 7 of the verification XY case, the first 40 pulse symbols, in increasing update order, are:

```text
Baseline:     0010101101010101101010101010101010101010
Intervention: 0010101010110101010101011010101010010101
```

The one-read intervention occurs at zero-based tick 3. The strings agree before the propagated output difference at tick 7. The accompanying CSV records the fast-state values and counts of changed cells and pulse bits at every update. This is a controlled causal witness rather than an appeal to the visual appearance of a bit pattern.

\begin{figure}[H]
\includegraphics[width=\linewidth]{manuscript/figures/feedback.pdf}
\caption{Recorded fast-state trajectories for the disclosed one-read intervention. The old output read changes only once, at tick 3; packed pulse output first differs at tick 7. Data: evidence/feedback/trace.csv.}
\end{figure}

## What remains a local hardware obligation

No NVIDIA GPU, `nvcc` compilation, Compute Sanitizer result, PTX/SASS device disassembly or texture-cache performance measurement was available in the delivery environment. The package therefore marks CUDA execution **not run**, and the hardware workflow returns **BLOCKED** when the required tools or requested device are absent.

The supplied local workflow compares texture and global fetches, several warp-aligned block sizes, a fresh-process repeat, forced PTX JIT and checkpoint continuation. Requested instrumentation captures sanitizer and profiling reports for inspection. A captured profiler file is not automatically a speed or cache-efficiency theorem.

# Source decisions and the theory of consciousness

## Four closure arguments, with their exact disposition

**Functional closure.** The source's $f:\mathbb R^n\to\mathbb R$ signature does not have matching input and output types when $n\ne1$. The normative replacement is explicitly declared: $T_\sigma:\mathcal S_\sigma\to\mathcal S_\sigma$, with binary and SDF conjugate representations. This preserves the goal of closure without silently treating scalars, coordinates, arrays, latches and transforms as the same type. [C, p. 35; audit C16, C28]

**Topological closure.** The source's Klein-bottle hinge remains a motif. Its polynomial, drawing and branch diagram do not establish that the implemented domain is that manifold or that physical energy is isolated by it. The actual online graph has angular wrap and radial boundaries. A genuine state-as-SDF representation is supplied by C13, with its own declared geometry. [C, pp. 6, 30-35; audit C02, C24, C29]

**Parity closure.** The set-indicator/XOR relation is retained. The assertion that a final parity token replaces the whole seed is not retained. The exact quotient criterion identifies when a reduction preserves future behavior, and the accumulator gives a concrete failure of a last-bit-only reduction. The engine closes through its sufficient present state, not by hiding it behind one output symbol. [C, pp. 9-10, 35-36; audit C08-C11, C30]

**Temporal closure.** The source's static-four-dimensional-crystal description does not remove the need to execute a physical computer. The implemented mathematical advance is autonomous because phase and dwell are explicit bounded internal state. Its trajectory can be defined for every finite iteration, while actual execution requires physical resources. This is not the source's proposed perpetuum mobile. [C, pp. 23-25, 36; audit C18, C31-C33]

The complete **36-entry source-decision audit** is supplied in CSV and JSON. It identifies exact source pages, retained terminology, qualified statements, unsupported claims and the new construction used for each gap. The original latest corpus and the earlier engineering archive are preserved unchanged for provenance. They are historical source material, not blanket endorsements of every statement they contain.

## Conscious organization as a stated hypothesis

The corpus proposes consciousness as self-referential field activity and memory as a structural change that shapes later activity. The implemented counterpart is precise: previous output influences subsequent sampling and drive; a slower recurrent memory value influences a subsequent field offset; a persistent latch changes later simulated transport. These are observable causal properties of the defined machine. [C, pp. 25-29]

Calling that organization *consciousness* adds an empirical or philosophical claim. No human recording, behavioral criterion, intervention dataset or validated consciousness measurement is supplied that identifies the kernel state with subjective experience. The closure theorem does not establish that all cells, electron configurations, neurons or organisms are instances of this specific transition.

The relationship between Hadamard notation and parity is likewise typed: binary characters can index signs in a Walsh matrix, while the matrix transform itself acts by sums on an amplitude vector. For

$$
H=\begin{pmatrix}1&1\\1&-1\end{pmatrix},\qquad H^2=2I.
$$

That identity is proved in the algebraic suite. It does not prove molecular or quantum-holographic memory in this engine. The shipped core is an integer recurrence, not a quantum-state simulator.

The earlier corpus's Christian reading of the *Word*, generative seed and reflective field may be retained as the author's spiritual interpretation. It is not used as an arithmetic axiom or a device-verification result. The mathematics remains defined without requiring a spiritual claim to be true or false. [G3]

## Research questions not settled by closure

A computational test can compare predictive behavior with and without pulse feedback, memory coupling or persistent latches, while controlling the seed and recording every change. A representation test can verify complete capsule continuation and attempt a smaller quotient using the exact criterion. A sensory or biological claim would need an independently specified measurement map, dataset, alternative models and failure criteria before the numerical variables could be interpreted as measurements of a person.

Self-feedback alone is not the discriminating outcome of such a study: the software already contains it by construction. An empirical account would need predictions that distinguish this theory from other recurrent models rather than merely redescribe their shared ability to feed output into input. No stimulation protocol or human exposure experiment is included in this software release.

# Reproduction, acceptance and trust boundary

## Run the closed engine

From the extracted project root, build the CPU executables:

```text
cmake -S . -B build -DGAMBIT_ENABLE_CUDA=OFF -DCMAKE_BUILD_TYPE=Release
cmake --build build --config Release --parallel 2
ctest --test-dir build -C Release --output-on-failure
```

On a single-configuration Linux build, run a native segment and then continue from its self-contained capsule:

```text
./build/gambit --asset assets/verify_xy.gblut --steps 64 --out run_a
./build/gambit --resume run_a/final.gbc --steps 64 --out run_b
```

On a Visual Studio multi-configuration build, the corresponding executable is normally `build/Release/gambit.exe`. The CPU source has no third-party runtime library dependency beyond the C++ standard library. The Python reference and trace checks use the standard library; Python 3.11 or later is the verification target.

To run the explicit Boolean arithmetic backend, use `--backend gates`. To inspect an output directory, run `python tools/audit_trace.py run_a`. To display the exact SDF representation of a small word, run `python tools/state_sdf.py 01011001`. The last command is a representation demonstration, not the main simulation.

## The verification entry point

```text
python tools/verify.py --cpu-only --formal
```

This checks the release manifest, compiles the source, runs native/Python tests, compares the frozen cases, checks the Boolean backend, verifies checkpoint splitting and runs the SMT obligations. Z3 is required only for `--formal`; an absent solver is an unmet prerequisite, not a successful proof. No verifier downloads tools, installs drivers or modifies the expected hashes.

On the actual target laptop, the separate device workflow is:

```text
python tools/verify.py --hardware --formal --sanitizers --profile
```

Read `AGENTS.md` before automated verification. A clean result must identify its scope: CPU-only success, hardware success, blocked prerequisites or a failed check. It must never be promoted from one category to another by editing labels or replacing expected output.

## Trust boundary and privacy

The mathematical results assume exact stated semantics. The delivered implementations rely on their compilers, standard libraries, operating systems and hardware. SMT evidence relies on the submitted formulas and the solver. File digests rely on a trusted expected digest; a party able to replace both a capsule and its digest can create a different internally consistent record. Nothing in the package is a cryptographic identity verification or an independent check of legal authorship.

The PDF and archive contain the requested personal attribution. The historical archive also retains earlier source documents and their claims. Review the contents before public redistribution. No font files, credentials or device-driver binaries are supplied.

# References and source register

**[C]** User-supplied *lrad directed parabolic crowd disbursement*, 36 pages. Source-page references in this edition use the PDF's physical page numbering. Preserved as `provenance/closure_corpus_original.pdf`. Treat its AI-generated conversational claims as source material, not independent scientific validation.

**[G3]** *Tom Klootwijk Gambit: Unified Seed-Field Theorem and Theory of Consciousness, Edition 3.0*, and its accompanying source corpus. Preserved recursively in the original engineering archive. Source for the broader interpretation and earlier exact quotient criterion.

**[E31]** *Tom Klootwijk Gambit: Native CUDA Kernel 3.1*, source, model and proofs. Preserved as `provenance/engineering_3.1_original.zip`; the inherited model text is also available as `provenance/U3D_original.md`. Source for the retained numerical laws, frozen assets and bounded engineering specialization.

**[AB]** Przemyslaw Prusinkiewicz and Aristid Lindenmayer, *The Algorithmic Beauty of Plants*. Author-hosted publication record, Algorithmic Botany. Background for parallel L-system rewriting, not evidence for this release's consciousness hypothesis. <https://algorithmicbotany.org/papers/#abop>

**[N1]** NVIDIA, *CUDA Runtime API: Texture Object Management* and *CUDA C++ Programming Guide*, texture-object and texture-function sections. Consulted 11 September 2026. <https://docs.nvidia.com/cuda/cuda-runtime-api/group__CUDART__TEXTURE__OBJECT.html> and <https://docs.nvidia.com/cuda/cuda-c-programming-guide/>

**[N2]** NIST, *FIPS 180-4: Secure Hash Standard*. SHA-256 algorithm and digest specification. <https://csrc.nist.gov/pubs/fips/180-4/upd1/final>

**[N3]** NVIDIA, *CUDA GPU Compute Capability*, 12.0 family listing. Consulted 11 September 2026; local device inspection remains required. <https://developer.nvidia.com/cuda/gpus>

**[N4]** NVIDIA, *CUDA Compiler Driver NVCC*, Toolkit 12.8.1 archive, GPU target options. <https://docs.nvidia.com/cuda/archive/12.8.1/cuda-compiler-driver-nvcc/index.html>

**[Z1]** Z3 project, *C API documentation*, including SMT-LIB string evaluation. <https://z3prover.github.io/api/html/group__capi.html>

**[Z2]** SMT-LIB, *FixedSizeBitVectors theory*. Reference semantics for the submitted finite-width obligations. <https://smt-lib.org/theories-FixedSizeBitVectors.shtml>
