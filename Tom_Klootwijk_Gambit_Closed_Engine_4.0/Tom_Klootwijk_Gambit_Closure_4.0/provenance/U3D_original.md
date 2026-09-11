# Finite integer model and Unified Theorem U3-D

**Tom Klootwijk Gambit - native CUDA engineering specialization 3.1**

The theorem is about an explicitly bounded discrete machine. It is not an empirical theorem of consciousness. Written mathematical arguments, executable finite tests and prospective device measurements have different evidential roles.

## 1. Complete finite seed

Let the complete seed be

$$\sigma_D=(\Sigma,\omega,P,\Theta,L,X_0,V,\mathcal O).$$

Here Sigma is the alphabet set, omega the ordered axiom, P the parallel grammar, Theta the validated integer/header and bake parameters, L the immutable packed LUT bytes, X0 the deterministic initial cell/control state, V the versioned implementation, and O the run options including pulse-feedback and any declared intervention. The selected step count belongs to O. All emitted file orderings are fixed. Documentary attribution fields do not change this mathematical machine.

The distributed chart has radial samples between r = 1/32 and r = 4 in dimensionless units. With R rows and A angular columns,

$$\rho_y=\log(1/32)+\frac{y}{R-1}\log(128),\quad
\theta_x=2\pi x/A,\quad p_{y,x}=e^{\rho_y}(\cos\theta_x,\sin\theta_x).$$

The radius origin is excluded. Only finitely many samples exist. A is a power of two between 32 and 2048; R is between 2 and 2048; levels G are in 1 through 5; and the run has 1 through 4096 updates. Consequently N = AR is divisible by 32, and no partial output word is required. Partially occupied thread blocks are nevertheless exercised by the verification asset.

## 2. Offline field and packed LUT

At every admitted generation g, the Edition 3.0 zero-memory geometry produces a sampled field F_g. The packed code is

$$d_{g,y,x}=\operatorname{clip}_{[-32768,32767]}
 \left(\left\lfloor4096F_g(p_{y,x})+\tfrac12\right\rfloor\right),$$

$$c_{g,y,x}=\operatorname{clip}_{[0,65535]}(32768-16d_{g,y,x}),\qquad
L_{g,y,x}=(d_{g,y,x}+32768)\;\mathbin{|}\;(c_{g,y,x}\ll16).$$

The low 16 bits use a biased signed-field representation; the upper 16 bits hold an unsigned field drive. The texture is unsigned 32-bit integer data, not normalized colour. Asset manifests record grammar words, sampling, saturation, hashes and the bake environment.

For an unsaturated *input sample value*, nearest-half-up quantization introduces at most 1/8192 field units of error. This statement is relative to the supplied floating sample. It is not an interval certificate for the error of the floating geometry evaluation itself. Away from a sample centre, finite sampling adds error. Saturation and field sign/threshold margins must be checked before drawing any continuous-space conclusion. The composite field is not asserted to be an exact interior distance to an overlapping union.

## 3. State and computational self-reference

For cell i, let

$$X_i^n=(U_i^n,V_i^n,z_i^n,m_i^n,r_i^n,f_i^n,K_i^n,Q_i^n).$$

U and V are nonnegative integer mass counts; z and m are in [0,D]; r is in [0,D-1]; D = 65536. K and Q store cumulative codec input and pulse counts. Four flag bits store the latch, pulse, occupancy and latch event. The global control is (n,g,last-growth). State arrays use six 32-bit and two 64-bit fields per cell. That is 40 bytes, not one bit.

The previous pulse is decoded from the machine's **own packed output buffer**:

$$q_i^{n-1}=\left(W^{n-1}_{\lfloor i/32\rfloor}\gg(i\bmod32)\right)\mathbin{\&}1.$$

The initial output buffer is zero. A declared one-bit intervention flips this read at one cell and one step only; it does not alter the historical output log. This creates a controlled counterfactual without corrupting the codec certificate.

With pulse-feedback enabled, the sampled angular bin is

$$j_i^n=\left(x_i+n s+q_i^{n-1}a\right)\bmod A,$$

where s = 1 and a = 3 in the supplied assets. The radial bin is unchanged. Incoming memory supplies

$$h_i^n=\operatorname{trunc}_0((m_i^n-D/2)/256),\quad
F_i^n=d_{g,y_i,j_i^n}-h_i^n,$$

$$a_i^n=\operatorname{clip}_{[0,D]}
\left(c_{g,y_i,j_i^n}+16h_i^n+8192(2q_i^{n-1}-1)\right).$$

The divisors, angular shifts and gain are explicit header parameters. Signed division truncates toward zero, including for negative values. `--feedback 0` removes the pulse-dependent angular offset, memory field offset and direct pulse-drive term. It does not disable every other feedback loop: latch-mediated transport and pulse-count growth still operate. Therefore this option is described as **pulse-feedback ablation**, not a globally open-loop model.

Self-reference has this precise operational meaning: a descriptor produced by the machine becomes an input to its own subsequent transition. It does not mean a quine, a self-modifying executable, a model that proves all of its own properties, or subjective awareness.

## 4. Conservative transport and reaction

Each cell has up to four neighbors: angular predecessor/successor with wrap, and radial predecessor/successor where present. Radial ends have no exterior edge. If either sampled field on an edge is positive, its flux is zero. Otherwise the edge divisor is 8 when either incoming latch is one and 32 when both latches are zero. Both endpoints use the same edge divisor.

For one species M and each admitted directed edge i to j,

$$J_{i\to j}=\left\lfloor M_i/2^{s_{ij}}\right\rfloor,\quad s_{ij}\ge3,$$

$$\widetilde M_i=M_i-\sum_jJ_{i\to j}+\sum_jJ_{j\to i}.$$

Every output cell gathers from the *old* state; no endpoint writes into its neighbor. Closed/inactive cells retain their mass. No clipping hides negative counts and no new mass is invented at newly sampled geometry.

Next, the local reaction uses integer transfers

$$A_i=\lfloor\widetilde U_i/64\rfloor,\qquad B_i=\lfloor\widetilde V_i/128\rfloor,$$

$$U_i'=\widetilde U_i-A_i+B_i,\qquad V_i'=\widetilde V_i-B_i+A_i.$$

These are chosen graph-model transport and reaction laws, not calibrated molecular kinetics. Nonnegative integer coefficients make their conservation and positivity exact. The initial total mass must lie in 1 through 2^32-1.

## 5. Sensing, bounded memory and the one-bit word

The post-reaction local material observation is

$$b_i=\begin{cases}\lfloor D U_i'/(U_i'+V_i')\rfloor,&U_i'+V_i'>0,\\D/2,&U_i'+V_i'=0.\end{cases}$$

Combine field and material, update fast state, then update memory:

$$v_i=\lfloor(3a_i^n+b_i)/4\rfloor,\quad
z_i'=\lfloor(3z_i^n+v_i)/4\rfloor,\quad
m_i'=\lfloor(15m_i^n+z_i')/16\rfloor.$$

The supplied implementation deliberately uses the new fast state in the memory update. The field sample for the current step still used incoming memory. Thus material, memory, bits and geometry participate in a causal loop without reading partially updated neighbors.

Set k_i = z_i'. The codec is

$$q_i^n=\mathbf1\{r_i^n+k_i\ge D\},\qquad
r_i'=r_i^n+k_i-Dq_i^n,$$

$$K_i'=K_i^n+k_i,\qquad Q_i'=Q_i^n+q_i^n.$$

The latch uses threshold H = 49 in field-code units:

$$\ell_i'=\begin{cases}1,&F_i^n\le-H,\\0,&F_i^n\ge H,\\\ell_i^n,&-H<F_i^n<H.\end{cases}$$

The event is e_i = old-latch XOR new-latch; raw occupancy is o_i = 1{F_i <= 0}. Occupancy and a latch can legitimately disagree inside the hysteresis band. Those bits are not interchangeable.

Four planes pack pulses, latches, events and occupancies, each 32 cells per unsigned 32-bit word in least-significant-bit-first cell order. A fifth storage plane holds one 0/1 parity value per pulse word, in a 32-bit container. Parity is not mixed into the pulse-density count. It detects odd bit flips in a word, not all corruption or malicious changes.

After each step, the exact global pulse count P_n controls growth. If the dwell has elapsed, a level remains and 4 P_n >= N, increment the generation once and record the new last-growth step. This newly selected generation affects the following lookup. Supplied dwell is 16 steps. The finite pre-baked atlas ends at generation four.

## 6. Unified Theorem U3-D

**Statement.** Fix an admitted complete seed, valid run options, immutable LUT bytes, and the transition laws above. Assume fault-free execution of the specified integer operations, nonaliasing old/new buffers, ordered stage execution and the declared texture point-read semantics. Then through the admitted step budget:

1. The next state and ordered output are uniquely determined; replay is exact.
2. All represented masses remain nonnegative and their global sum is invariant.
3. Fast state and memory remain in [0,D], residuals in [0,D-1], and the stated integer widths suffice.
4. Every pulse and latch is binary. For every cell and every prefix t,
   $$D\sum_{n<t}q_i^n-\sum_{n<t}k_i^n=-r_i^t,$$
   so the dyadic count discrepancy lies in (-1,0].
5. Packing/unpacking is an exact encoding of each declared Boolean plane; events telescope in XOR and parity obeys its stated odd-error rule.
6. The described CUDA stage partition admits a schedule-independent realization of the same finite transition as the CPU reference. On conforming compiler/runtime/hardware execution, CPU and GPU therefore produce identical canonical states and words.
7. Computational self-feedback is a genuine causal input for the supplied witness. Removing or intervening on that input can change subsequent states; the reported one-bit output alone is not a sufficient full-state quotient.

Part 6 is an implementation-correctness target supported by the dependency argument below, not a claim that this delivery has executed or mechanically verified the CUDA compiler/hardware. Native device compilation, full equality tests and instrumentation remain explicit hardware obligations.

## 7. Supporting proof family

### D1. Finite address and arithmetic closure

The validated dimensions give N <= 2^22 and at most 5N LUT elements. The largest flattened LUT index fits unsigned 32 bits. Its y coordinate is less than 10240 and x less than 2048; adding one half to either integer is exactly representable in binary32. Hence texel-center address construction introduces no coordinate rounding for this admitted domain. The step/phase product is also within unsigned 32 bits.

The memory offset has magnitude at most 32768 even at the smallest admitted divisor. Field and drive intermediate expressions fit signed 64 bits (indeed their stated bounds fit signed 32 here). Recurrence numerators are at most 16D. The codec sum is at most 2D-1. The initial mixer alone intentionally wraps unsigned 32-bit products; wrap is not an accidental mass or codec operation.

### D2. Integer transport positivity and conservation

Each donor has at most four neighbors and every divisor is at least eight. Therefore total outflow is at most 4 floor(M_i/8) <= M_i/2 <= M_i. Remaining mass and incoming terms are nonnegative. Sum the update over all cells: each directed J appears once negatively at its source and once positively at its destination. Every term cancels, so the species total is unchanged even when the realized gates differ at the next step.

The result is not a global contraction theorem for state-dependent geometry. It is a conservation/positivity theorem for each realized update.

### D3. Reaction positivity and conservation

A <= U-tilde and B <= V-tilde. Subtracting the source's own transfer cannot make a species negative, and the reverse transfer is nonnegative. Adding the two updates cancels A and B exactly. Combining D2 and D3 proves invariant total represented mass. Every individual species count is at most the total, so the accepted initial bound ensures every stored count fits unsigned 32 bits. Intermediate gather sums and products use unsigned 64 bits.

### D4. Invariance of bounded observation and recurrent states

For nonzero total, 0 <= U'/(U'+V') <= 1; the chosen integer material observation is therefore in [0,D]. Its zero-total convention is also in that interval. A clipped field drive lies there by construction. Convex weighted integer averages, rounded downward, preserve [0,D]. Apply this first to v, then z', then m'. Induction starts at z=m=D/2.

### D5. Exact prefix certificate

For 0 <= r < D and 0 <= k <= D, the sum r+k lies in [0,2D-1]. Subtracting D exactly when this sum is at least D leaves a residual in [0,D-1], with q in {0,1}. The identity Dq = k+r-r' telescopes over steps. Initial residual is zero, giving DQ-K = -r at every prefix. Dividing by D gives -1 < Q-K/D <= 0. No floating-point error estimate is needed for this dyadic certificate.

There are at most 4096 steps, so K <= 2^28 per cell and global K <= 2^50. The chosen unsigned 64-bit totals do not overflow. This is a certificate relative to integer k, not recovery of the original continuous geometry or the whole state.

### D6. Hysteresis and event identities

Positive H makes the two outer threshold conditions disjoint; the open middle band inherits a valid previous bit. Hence the next latch is binary, including at both specified equalities. Repeated XOR of events cancels every intermediate latch twice, leaving initial-latch XOR final-latch. Memory in the middle band is intentional rather than nondeterminism.

### D7. Bit packing and parity

Distinct cell offsets in a word use distinct powers of two. Extracting bit j after the sum/OR returns the original Boolean at position j. The word value stays within unsigned 32 bits, including bit 31. XOR reduction of all data bits defines parity. Flipping an odd number of data bits changes parity; an even number can preserve it. This is neither encryption nor authentication. The file SHA-256 manifest separately checks delivery integrity against an expected digest, not against an attacker who can replace both files and manifest.

### D8. Ordered stages and CPU/GPU equality

Preparation reads only incoming cells, incoming packed words, incoming control and immutable atlas data, then writes one sample per cell. Advancement reads those completed samples and old cells, then writes one new cell per thread. No cell writes into a neighbor. All launched lanes execute all four warp ballots; padded lanes contribute false. Each plane word has exactly one lane-zero writer, and only complete valid words are stored.

The fixed 256-thread summary uses synchronized shared-memory reductions. Addition is exact in the proven range, independent of grouping. It updates global control only after the cell transition has completed. Sequential launches in one stream and explicit host copies order stages. The next iteration reads swapped buffers rather than in-place updates. Therefore every stage implements the scalar laws without schedule-dependent read/write choices. If the compiler/runtime/device honor these operations and texture semantics, induction gives CPU/GPU equality. Actual local execution must test this conditional conclusion; the written argument is not an nvcc or silicon proof.

### D9. Causal computational self-feedback witness

The previous pulse is read from the engine's own packed result and appears in the next angular address and direct drive. For identical incoming states up to a selected read, flip that read at a cell whose clipping has not erased the effect. The resulting drive/address can differ, and thus the next fast state can differ. The supplied verification experiment at cell 7, step 3 observes this state difference while all earlier states match. Independent Python and C++ traces agree on that experiment. A separate pulse-feedback ablation changes the delivered bit trace.

This proves the specific operational feedback witness, not that every perturbation must change every trajectory or that a self-referential bitstream has experiences. Equal total numbers of ones can coexist with different timing and states.

### D10. Why the emitted bit is not the full machine

Consider two admissible accumulator states that have just emitted q=0 but retain residuals 0 and D-1. Feed both the same next k=1. Their next pulses are 0 and 1 respectively. Thus equality of the last emitted bit does not force equality of the next emitted bit under common input. The one-bit projection fails the exact quotient criterion retained from Edition 3.0. The complete finite seed, residual, memory, material, latches, generation and history cannot be silently discarded.

Combining D1-D10 establishes the stated mathematical conclusions and the conditional implementation relationship. Executable checks exercise finite cases. A future hardware pass adds device evidence; it does not turn the consciousness interpretation into an empirical result.
