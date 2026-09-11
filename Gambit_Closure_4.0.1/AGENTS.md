# Automated verification contract — Gambit Closure 4.0

Read `README.md`, `docs/BINARY_FORMAT.md`, `docs/VERIFICATION.md` and the U4 statement
before interpreting a result. The model is offline numerical research only.

## Required actions

1. Check `SHA256SUMS.txt` without modifying any source, asset or expected digest.
2. Run `python tools/verify.py --cpu-only --formal` in a new output directory.
3. For requested target-GPU verification, run
   `python tools/verify.py --hardware --formal --sanitizers --profile` on the actual
   RTX 5070 Ti Laptop. Record the detected device, compiler, driver and all logs.
4. Inspect the generated verification JSON and its command logs. Report scope and
   exact failures or blocked prerequisites. Keep CPU, Boolean, SMT and GPU evidence
   separate. The two expected SAT targets are intentional counterexamples.

## Do not

Do not replace goldens with newly generated outputs to obtain PASS. Do not relabel
BLOCKED as PASS, claim a CPU run tested CUDA, infer texture-cache performance from
source, or claim that a bit trace proves consciousness. Do not install tools,
modify drivers, alter GPU power settings or contact external services automatically.
Do not add audio output, physical drivers or an actuator path.

A requested source change must be a separate proposed revision with a diff and
newly disclosed evidence, not a hidden alteration of this frozen release. Never
claim machine-checked verification of the entire implementation: solver targets
are listed explicitly and solver proof logs have no independent second checker.

## Entry points

- Native transition: `src/engine.cpp`, inherited primitives `include/gambit/model.hpp`.
- Boolean arithmetic: `include/closure/boolean.hpp`, `src/boolean.cpp`.
- Canonical serialization and SHA-256: `src/capsule.cpp`.
- CUDA realization: `src/cuda.cu`; CPU reference equality is checked per update.
- Independent numerical model: `tools/reference.py`.
- Frozen expected digests: `assets/closure_goldens.json`.
- Formal targets: `formal/obligations.json`, `formal/targets/`.

Use unused output directories. Final capsules are sufficient for restart without
external LUT files, but are not signed evidence of reachable history. The software
and its specification remain required to interpret a capsule.
