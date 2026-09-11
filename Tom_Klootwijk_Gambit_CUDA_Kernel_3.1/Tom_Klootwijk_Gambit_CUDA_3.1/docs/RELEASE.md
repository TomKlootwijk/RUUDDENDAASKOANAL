# Release contract and reading map

**Tom Klootwijk Gambit — Native CUDA Kernel 3.1** is an engineering companion to the *Unified Seed-Field Theorem and Theory of Consciousness, Edition 3.0*. The author attribution is **Tom Klootwijk · NL200678942 · 10-07-1990**, as supplied. The mathematical definition does not depend on the personal identifier or date.

This release turns the source corpus's log-polar field lookup, L-system geometry, binary hinges and one-bit output into a finite C++/CUDA state machine. The original double-arc addendum's page 6 presented a conceptual sampling sketch; the new source supplies allocation, texture configuration, stage ordering, integer state, packing, file formats and local verification. The source lineage is documented in [S1-S3].

The target is the **RTX 5070 Ti Laptop GPU with 12 GB GDDR7**, using a native `sm_120` build and retained `compute_120` PTX. The laptop memory specification and architecture/toolchain target are grounded in NVIDIA's documentation; the executable and verifier still query the actual installed device [H1-H3].

## What is delivered

The ZIP contains the complete native source, pre-baked XX/XY field atlases, the shared finite transition law, an independent Python reference, tests, exact CPU-generated traces, build scripts, this editable manuscript, and a Codex verification contract. The original Edition 3.0 archive is retained unchanged under `provenance/`, including its previous Python kernel and source corpus.

The main GPU source is **not precompiled**. The delivery environment lacked nvcc and an NVIDIA GPU. CPU builds and tests have passed, but CUDA compilation, target-device execution, GPU sanitizer results, texture-cache counters and throughput remain unmeasured. `DELIVERY_STATUS.json` and the raw evidence files make these states machine-readable.

## The central implemented claim

The engine reads its own previous packed output, uses it to change the next field sample and recurrent state, and emits a new certified Boolean pulse. For each cell, the integer pulse-density codec obeys the exact prefix certificate

$$65536\,Q_i(t)+r_i(t)=K_i(t),\qquad 0\le r_i(t)<65536.$$

Here Q counts emitted ones, K is the cumulative integer input and r is the retained residual. The output is one bit per cell per update. The complete state is larger: two material counts, fast state, memory, residual, flags and cumulative counters. Theorem U3-D proves properties of that specified machine and gives a conditional CPU/GPU equivalence argument.

The word **self-reference** denotes this causal output-to-input feedback. It does not assert that a generated bitstream experiences consciousness, represents all of biology, or validates a spiritual interpretation. The broader account remains in the preserved Edition 3.0 manuscript. The implementation does not silently import speculative source claims as hardware facts.

## Reading and execution order

Read the migration section for changes from the earlier floating simulation. The finite-model section gives the complete recurrence and proof family. The native-implementation and file-format sections explain texture layout, write ownership and canonical binary output. The evidence section shows measured CPU results and the one-read feedback witness. The final verification section specifies exactly what Codex or a local operator must execute on the laptop.

From the extracted project root, the complete requested local workflow is:

```text
python tools/verify.py --hardware --sanitizers --profile
```

A hosted workspace without the laptop GPU cannot complete this command's device obligations. The scripts do not install drivers, change privileged settings, alter clocks or power limits, or substitute CPU success for GPU verification. A blocked or failed stage is reported explicitly.

## Integrity, reproducibility and privacy

`SHA256SUMS.txt` indexes the release's files, excluding itself. The verifier checks that manifest before building. `assets/golden_traces.json` separately specifies the canonical CPU-derived output hashes. Extra local build/evidence directories are permitted, but changing an indexed release file fails integrity checking. The manifest detects changes relative to the distributed record; it is not a signature or independent proof of authorship.

All runs use fresh output folders. The binary writer refuses prior result artifacts rather than leaving an old success record attached to a failed run. Do not regenerate LUTs or golden files to make a mismatch disappear. Investigate the source of the mismatch and declare any intentional model change as a new revision.

This is a private-attribution edition. It includes the supplied identifier/date and the unmodified historical archive. Review those materials before public redistribution.
