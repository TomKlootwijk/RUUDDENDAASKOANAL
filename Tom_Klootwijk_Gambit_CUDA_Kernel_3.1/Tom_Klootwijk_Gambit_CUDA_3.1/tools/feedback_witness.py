#!/usr/bin/env python3
"""Reproduce the declared computational self-feedback counterfactual, without CUDA."""
from __future__ import annotations
import argparse, dataclasses, json
from pathlib import Path
from reference import Reference, load_asset


def witness(asset: Path) -> dict:
    p, lut = load_asset(asset)
    baseline = Reference(p, lut)
    changed = Reference(p, lut, inject_step=3, inject_cell=7)
    first_state = first_pulse = None
    records = []
    prefix_equal = True
    for step in range(p['steps']):
        old_q = (baseline.words[0] >> 7) & 1
        baseline.step(); changed.step()
        same = baseline.cells == changed.cells
        pulse_changes = sum((a ^ b).bit_count() for a, b in zip(
            baseline.words[:baseline.n//32], changed.words[:changed.n//32]))
        if step < 3:
            prefix_equal = prefix_equal and same and baseline.words == changed.words
        if not same and first_state is None:
            first_state = step
        if pulse_changes and first_pulse is None:
            first_pulse = step
        records.append({
            'step': step, 'pulse_bits_different': pulse_changes,
            'changed_cells': sum(a != b for a, b in zip(baseline.cells, changed.cells)),
            'baseline_cell7': dataclasses.asdict(baseline.cells[7]),
            'intervention_cell7': dataclasses.asdict(changed.cells[7]),
            'baseline_sample7': baseline.samples[7],
            'intervention_sample7': changed.samples[7],
            'baseline_previous_q7': old_q,
        })
    if not prefix_equal or first_state != 3 or first_pulse is None:
        raise AssertionError('Declared causal feedback witness was not reproduced')
    return {
        'model': 'gambit-u3d-3.1', 'backend': 'independent_python_cpu',
        'asset': asset.name, 'intervention': {'step': 3, 'cell': 7, 'operation': 'flip only the next read of prior packed q'},
        'states_and_words_before_step3_identical': prefix_equal,
        'first_state_divergence_step': first_state,
        'first_pulse_divergence_step': first_pulse,
        'total_baseline_ones': sum(c.qo for c in baseline.cells),
        'total_intervention_ones': sum(c.qo for c in changed.cells),
        'scope': 'Causal feedback witness for this finite machine, not consciousness or universal sensitivity',
        'records': records,
    }

if __name__ == '__main__':
    ap = argparse.ArgumentParser()
    ap.add_argument('--asset', type=Path, default=Path(__file__).resolve().parents[1]/'assets/verify_xy.gblut')
    ap.add_argument('--out', type=Path, required=True)
    args = ap.parse_args()
    if args.out.exists():
        ap.error('Choose a new evidence file; existing results are not overwritten')
    result = witness(args.asset)
    args.out.parent.mkdir(parents=True, exist_ok=True)
    args.out.write_text(json.dumps(result, indent=2)+'\n')
    print('PASS: intervention affects the state at step', result['first_state_divergence_step'],
          'and packed pulse output at step', result['first_pulse_divergence_step'])
