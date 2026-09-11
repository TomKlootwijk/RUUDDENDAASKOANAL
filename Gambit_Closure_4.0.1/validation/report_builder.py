#!/usr/bin/env python3
"""Build the final, evidence-backed six-page verification report.

Run only after the coordinator and the independent completion audit are terminal.
Uses ReportLab; never changes source, goldens, or validation results.
"""
from __future__ import annotations

import argparse
import datetime as dt
import hashlib
import json
from pathlib import Path
import re
import sys
from xml.sax.saxutils import escape

from reportlab.lib import colors
from reportlab.lib.enums import TA_LEFT
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.units import mm
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, PageBreak,
    KeepTogether,
)

ROOT = Path(__file__).resolve().parents[1]
NAVY = colors.HexColor('#183449')
TEAL = colors.HexColor('#087F80')
INK = colors.HexColor('#263849')
MUTED = colors.HexColor('#586C7D')
PALE = colors.HexColor('#EFF5F8')
LINE = colors.HexColor('#D4E0E7')
WHITE = colors.white
# SimpleDocTemplate's default frame pads both sides by six points.
WIDTH = A4[0] - 36 * mm - 12


def read_json(path: Path):
    return json.loads(path.read_text(encoding='utf-8'))


def digest(path: Path):
    with path.open('rb') as handle:
        return hashlib.file_digest(handle, 'sha256').hexdigest()


def clean(value):
    return str(value).replace('\u2013', '-').replace('\u2014', '-').replace('\u2011', '-')


STYLES = {
    'body': ParagraphStyle('Body', fontName='Helvetica', fontSize=9.3, leading=13,
                           textColor=INK, spaceAfter=7),
    'small': ParagraphStyle('Small', fontName='Helvetica', fontSize=8, leading=11,
                            textColor=MUTED, spaceAfter=5),
    'tiny': ParagraphStyle('Tiny', fontName='Helvetica', fontSize=7.1, leading=9.5,
                           textColor=MUTED, spaceAfter=3),
    'title': ParagraphStyle('Title', fontName='Helvetica-Bold', fontSize=30,
                            leading=34, textColor=NAVY, spaceAfter=10),
    'heading': ParagraphStyle('Heading', fontName='Helvetica-Bold', fontSize=18,
                              leading=22, textColor=NAVY, spaceAfter=11),
    'sub': ParagraphStyle('Sub', fontName='Helvetica-Bold', fontSize=11,
                          leading=14, textColor=TEAL, spaceBefore=9, spaceAfter=5),
    'label': ParagraphStyle('Label', fontName='Helvetica-Bold', fontSize=9,
                            leading=12, textColor=TEAL, spaceAfter=7),
    'cell': ParagraphStyle('Cell', fontName='Helvetica', fontSize=8.2, leading=11,
                           textColor=INK, spaceAfter=0),
    'cellsmall': ParagraphStyle('CellSmall', fontName='Helvetica', fontSize=7.4,
                                leading=9.6, textColor=INK, spaceAfter=0),
    'headcell': ParagraphStyle('HeadCell', fontName='Helvetica-Bold', fontSize=8,
                               leading=10.5, textColor=WHITE, spaceAfter=0),
    'code': ParagraphStyle('Code', fontName='Courier', fontSize=7.2, leading=10,
                           textColor=INK, spaceAfter=4, splitLongWords=True),
}


def p(text, style='body'):
    return Paragraph(escape(clean(text)).replace('\n', '<br/>'), STYLES[style])


def markup(text, style='body'):
    return Paragraph(clean(text), STYLES[style])


def table(headers, rows, widths, small=False):
    style = 'cellsmall' if small else 'cell'
    data = [[p(h, 'headcell') for h in headers]] + [[p(c, style) for c in row] for row in rows]
    result = Table(data, colWidths=[WIDTH * fraction for fraction in widths], repeatRows=1, hAlign='LEFT')
    result.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), NAVY),
        ('VALIGN', (0, 0), (-1, -1), 'TOP'),
        ('LEFTPADDING', (0, 0), (-1, -1), 7),
        ('RIGHTPADDING', (0, 0), (-1, -1), 7),
        ('TOPPADDING', (0, 0), (-1, -1), 6),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 6),
        ('ROWBACKGROUNDS', (0, 1), (-1, -1), [WHITE, PALE]),
        ('LINEBELOW', (0, -1), (-1, -1), 0.5, LINE),
    ]))
    return result


def log_text(root, run, tag):
    path = root / run / 'logs' / (tag + '.txt')
    if not path.is_file():
        raise ValueError('Required command log missing: ' + str(path))
    return path.read_text(encoding='utf-8', errors='replace')


def find_exe(run, name):
    for path in (run / 'Release' / (name + '.exe'), run / (name + '.exe'), run / name):
        if path.is_file():
            return path
    raise ValueError('Missing binary ' + str(run / name))


def command(report, tag):
    matches = [item for item in report['commands'] if item['log'] == tag + '.txt']
    if len(matches) != 1:
        raise ValueError('Expected one command log: ' + tag)
    if matches[0]['returncode'] != 0:
        raise ValueError('Command is not successful: ' + tag)
    return matches[0]


def count_from_log(patterns, text, description):
    for pattern in patterns:
        match = re.search(pattern, text, re.IGNORECASE)
        if match:
            return int(match.group(1).replace(',', ''))
    raise ValueError('Could not extract ' + description + ' from actual test log')


def require_terminal_pass(report, label):
    status = report.get('status')
    if status not in ('PASS', 'GPU_CPU_EXACT_PASS', 'CPU_PASS_GPU_NOT_RUN', 'PASS_REQUESTED_SCOPE'):
        raise ValueError(label + ' has no terminal passing status: ' + str(status))


def compact(value):
    return clean(value) if isinstance(value, (str, int, float)) else json.dumps(value, ensure_ascii=True, sort_keys=True)


def short_summary(value, limit=220):
    text = compact(value)
    return text if len(text) <= limit else text[:limit - 3] + '...'


def collect(args):
    root = args.root.resolve()
    full = read_json(root / 'validation/full/verification.json')
    cpu = read_json(root / 'validation/cpu/verification.json')
    formal = read_json(root / 'validation/full/formal/report.json')
    revision = read_json(root / 'REVISION.json')
    edges_path = root / args.edges
    edges = read_json(edges_path)
    audit_path = root / args.audit
    audit = read_json(audit_path)
    for label, report in [('hardware coordinator', full), ('CPU coordinator', cpu),
                          ('formal obligations', formal), ('edge probes', edges),
                          ('completion audit', audit)]:
        require_terminal_pass(report, label)
    if full['status'] != 'GPU_CPU_EXACT_PASS' or full['scope'] != 'full':
        raise ValueError('A full passing hardware coordinator is required')
    if cpu['status'] != 'CPU_PASS_GPU_NOT_RUN' or cpu['scope'] != 'full':
        raise ValueError('A full passing CPU-only coordinator is required')
    if full.get('sanitizers') != 'PASS':
        raise ValueError('All requested sanitizers must pass')
    if full.get('profile') != 'CAPTURED_FOR_REVIEW_NOT_A_SPEED_CLAIM':
        raise ValueError('Both requested profiling captures must be complete')
    if any(item.get('returncode') != 0 for item in full['commands'] + cpu['commands']):
        raise ValueError('Coordinator contains unsuccessful or pending command')
    if any(not item.get('passed') or item['actual'] != item['expected'] for item in formal['targets']):
        raise ValueError('Formal target mismatch')
    if audit.get('protected_model_files_unchanged') is not True:
        raise ValueError('Completion audit has not confirmed unchanged model files')
    if any(item.get('status') != 'PASS' for item in audit.get('checks', [])):
        raise ValueError('Completion audit contains a non-passing check')
    if digest(root / 'SHA256SUMS.txt') != audit['source_manifest_sha256']:
        raise ValueError('Current revision manifest differs from completion audit')
    for item in audit['binaries'].values():
        if digest(root / item['path']) != item['sha256']:
            raise ValueError('Audited binary has changed: ' + item['path'])
    if any(item.get('status') != 'PASS' for item in edges['cases'].values()):
        raise ValueError('Edge case mismatch')
    if any(item['returncode'] != item['expected_returncode'] for item in edges['commands']):
        raise ValueError('Unexpected edge-probe return code')
    if edges.get('wrapper_contract', {}).get('status') != 'PASS':
        raise ValueError('CUDA wrapper contract has not passed')
    if not isinstance(edges.get('diagnostics'), dict) or set(edges['diagnostics']) != {'cell', 'clock'}:
        raise ValueError('Both isolated mismatch diagnostics must be present')
    if any(item.get('status') != 'PASS' for item in edges['diagnostics'].values()):
        raise ValueError('A diagnostic fault check did not pass')
    goldens = read_json(root / 'assets/closure_goldens.json')['cases']
    if set(goldens) - set(full['cases']) or set(goldens) - set(cpu['cases']):
        raise ValueError('Frozen profiles missing from a coordinator')
    native_checks = count_from_log([
        r'(\d[\d,]*)\s+checks', r'checks\s*[=:]\s*(\d[\d,]*)',
    ], log_text(root, 'validation/full', 'native_tests'), 'native checks')
    python_tests = count_from_log([r'Ran\s+(\d+)\s+tests?'],
        log_text(root, 'validation/full', 'python_tests'), 'Python test count')
    python_log = log_text(root, 'validation/full', 'python_tests')
    python_breakdown = {
        'model': len(re.findall(r'^test_\S+ \(test_reference\.ClosureTests\.[^)]+\) \.\.\. ok$', python_log, re.MULTILINE)),
        'coordinator': len(re.findall(r'^test_\S+ \(test_verify\.VerificationWorkflowTests\.[^)]+\) \.\.\. ok$', python_log, re.MULTILINE)),
    }
    if sum(python_breakdown.values()) != python_tests:
        raise ValueError('Python per-class counts do not match the test summary')
    gpu_runs = []
    for item in full['commands']:
        argv = item['argv']
        if '--out' in argv and Path(argv[0]).name.lower() in ('gambit_cuda.exe', 'gambit_cuda'):
            dest = Path(argv[argv.index('--out') + 1])
            run = read_json(dest / 'run.json')
            if not all(run.get(key) is True for key in ('gpu_verified', 'every_step_cpu_comparison', 'full_lut_readback')):
                raise ValueError('GPU run lacks per-step/readback evidence: ' + str(dest))
            gpu_runs.append((dest, run))
    for name, golden in goldens.items():
        if not full['cases'][name].get('golden_match') or not cpu['cases'][name].get('golden_match'):
            raise ValueError('Unconfirmed golden: ' + name)
        for filename, expected in golden['files'].items():
            for run in ('validation/full', 'validation/cpu'):
                if digest(root / run / 'native' / name / filename) != expected:
                    raise ValueError('Current golden bytes mismatch: ' + name + '/' + filename)
    nvcc = log_text(root, 'validation/full', 'nvcc_version')
    smi = log_text(root, 'validation/full', 'nvidia_smi')
    configure = log_text(root, 'validation/full', 'cuda_configure')
    compiler_match = re.search(r'CXX compiler identification is ([^\r\n]+)', configure)
    nvcc_match = re.search(r'release\s+([^,\r\n]+),\s+V([^\r\n]+)', nvcc)
    driver_match = re.search(r'Driver Version:\s*([^\s|]+)', smi)
    if not all([compiler_match, nvcc_match, driver_match]):
        raise ValueError('Cannot extract toolchain/driver identification from logs')
    sanitizers = []
    for name in ('memcheck', 'racecheck', 'initcheck', 'synccheck'):
        command(full, 'sanitize_' + name)
        text = log_text(root, 'validation/full', 'sanitize_' + name)
        lines = [line.strip().lstrip('=').strip() for line in text.splitlines()
                 if 'SUMMARY' in line and ('error' in line.lower() or 'hazard' in line.lower())]
        if not lines:
            raise ValueError('Sanitizer summary absent: ' + name)
        if name == 'racecheck':
            if not any('0 hazards displayed (0 errors, 0 warnings)' in line for line in lines):
                raise ValueError('Racecheck did not record zero hazards/errors/warnings')
        elif not any(re.search(r'ERROR SUMMARY:\s*0 errors', line) for line in lines):
            raise ValueError('Sanitizer did not record zero errors: ' + name)
        sanitizers.append((name, 'PASS', '\n'.join(lines)))
    profiles = []
    for fetch in ('texture', 'global'):
        command(full, 'profile_' + fetch)
        path = root / 'validation/full' / ('ncu_' + fetch + '.ncu-rep')
        if not path.is_file() or path.stat().st_size == 0:
            raise ValueError('Missing profiling artifact: ' + str(path))
        profiles.append((fetch, path, path.stat().st_size, digest(path)))
    original_root = Path(args.original_root).resolve()
    original_manifest = original_root / 'SHA256SUMS.txt'
    entries = []
    for line in original_manifest.read_text().splitlines():
        expected, name = line.split('  ', 1)
        if digest(original_root / name) != expected:
            raise ValueError('Original frozen file changed: ' + name)
        entries.append((name, expected))
    original_golden = digest(original_root / 'assets/closure_goldens.json')
    revised_golden = digest(root / 'assets/closure_goldens.json')
    if original_golden != revised_golden:
        raise ValueError('Original golden manifest was changed')
    revision_entries = []
    for line in (root / 'SHA256SUMS.txt').read_text().splitlines():
        expected, name = line.split('  ', 1)
        if digest(root / name) != expected:
            raise ValueError('Revision file changed after its manifest: ' + name)
        revision_entries.append((name, expected))
    return locals()


def build(args):
    d = collect(args)
    root, full, cpu, formal = (d[k] for k in ('root', 'full', 'cpu', 'formal'))
    story = []
    add = story.append
    def section(number, title):
        if number != 1:
            add(PageBreak())
        add(p('VERIFICATION RECORD  /  ' + str(number).zfill(2), 'label'))
        add(p(title, 'title' if number == 1 else 'heading'))

    section(1, 'Gambit Closure 4.0.1')
    add(p('CUDA repair and final verification', 'sub'))
    add(p('Verified on the requested NVIDIA GPU. The revised CUDA executable compiles, '
          'matches the CPU reference throughout the disclosed runs, and passes all four '
          'requested Compute Sanitizer modes. Both fresh formal and full CPU runs pass.'))
    add(Spacer(1, 3 * mm))
    add(table(['Verification scope', 'Recorded result'], [
        ['Hardware coordinator', full['status']],
        ['Separate CPU coordinator', cpu['status']],
        ['Native / Python tests', f"{d['native_checks']:,} native checks; {d['python_tests']} Python methods "
         f"({d['python_breakdown']['model']} numerical + {d['python_breakdown']['coordinator']} coordinator)"],
        ['Frozen trajectories', f"{len(d['goldens'])} complete profiles; exact consensus-file hashes"],
        ['CUDA equality and LUT readback', f"{len(d['gpu_runs'])} checked coordinator executions"],
        ['SMT obligations', f"{len(formal['targets'])} expected results; solver status {formal['status']}"],
        ['Compute Sanitizer', full['sanitizers'] + ' - memcheck, racecheck, initcheck, synccheck'],
        ['Nsight Compute', 'Texture and global reports captured for review'],
        ['Independent completion audit', d['audit']['status']],
    ], [.43, .57]))
    add(Spacer(1, 4 * mm))
    add(p('What this establishes', 'sub'))
    add(p('The repaired implementation meets the executed conformance and instrumentation '
          'checks described in this report. SMT results concern the submitted algebraic '
          'targets; they are separate evidence from CPU and GPU execution.'))
    add(p('It is not a machine-checked proof of the complete implementation, compiler, runtime '
          'or physical GPU. The solver logs have no independent second proof checker. '
          'The numerical results make no claim about subjective consciousness or physical perpetual operation.', 'small'))
    add(p('Revision root', 'sub'))
    add(p(str(root), 'code'))
    add(p('All evidence paths in this report are relative to that directory. '
          'The original 4.0 release remains separately preserved.', 'small'))

    section(2, 'Repairs and actual execution environment')
    add(p('Confirmed compilation defect', 'sub'))
    add(p('The original CU(call) macro declared a local variable named e. In CUDA calls '
          'containing the Engine argument e, that declaration shadowed the argument '
          'inside its own initializer. NVCC rejected the frozen source. The revised '
          'checker receives the completed cudaError_t result in an inline function; '
          'the macro now forwards the expression without introducing a local variable.'))
    add(p('Diagnostic accuracy', 'sub'))
    add(p('The CUDA comparison now tracks the update index within the segment. A mismatch '
          'after the first update is attributed to that update, rather than always reporting zero. '
          'The evidence suite checks the failure path as well as matching executions.'))
    add(p('Reproducible Windows verification', 'sub'))
    add(p('The coordinator accepts an explicit CUDA toolset for CMake, resolves supported '
          'NVIDIA forwarding launchers to their executable, and records per-command and '
          'per-stage status. This makes toolkit selection and instrumentation failures visible '
          'in the saved JSON and logs. CMake aligns host and CUDA targets on the static MSVC '
          'runtime. Consult the revision diff for the exact changes.'))
    device = full['device']
    rows = [
        ['GPU', device['device']],
        ['Compute capability', str(device['compute_major']) + '.' + str(device['compute_minor'])],
        ['Total VRAM reported by CUDA', f"{device['total_vram']:,} bytes"],
        ['NVIDIA driver', d['driver_match'].group(1)],
        ['CUDA compiler', 'Toolkit ' + d['nvcc_match'].group(1) + '; nvcc ' + d['nvcc_match'].group(2)],
        ['Host C++ compiler', d['compiler_match'].group(1)],
        ['Python / platform', full['python'] + ' / ' + full['platform']],
        ['CMake CUDA toolset', full.get('cmake_cuda_toolset')],
        ['Formal solver', formal['solver_version']],
    ]
    add(Spacer(1, 2 * mm))
    add(table(['Component', 'Observed identity'], rows, [.32, .68]))
    add(Spacer(1, 2 * mm))
    add(p('Source records: REVISION.json; revision diff; validation/full/logs/cuda_build.txt; '
          'validation/full/logs/cuda_configure.txt; validation/full/logs/device.txt; '
          'validation/full/logs/nvidia_smi.txt; validation/full/logs/nvcc_version.txt.', 'small'))

    section(3, 'Exact CPU and GPU conformance')
    add(p(f"The fresh full coordinator ran {d['native_checks']:,} native checks and "
          f"{d['python_tests']} Python methods: {d['python_breakdown']['model']} numerical reference methods "
          f"and {d['python_breakdown']['coordinator']} coordinator regressions. Each frozen profile below matched all "
          'of its expected consensus-file digests. The independent Python model and Boolean '
          'ALU were also compared on the four smaller profiles.'))
    rows = []
    for name, g in d['goldens'].items():
        c = full['cases'][name]
        modes = 'native + CUDA'
        if c.get('independent_python') and c.get('boolean_ALU'):
            modes += ' + Python + gates'
        rows.append([name, g['steps'], f"{c['cells']:,}", len(g['files']), modes])
    add(table(['Frozen profile', 'Updates', 'Cells', 'Files', 'Compared realizations'], rows,
              [.20, .11, .14, .08, .47]))
    add(p('Consensus files', 'sub'))
    add(p('initial.gbc, final.gbc, words.bin, counts.bin and summary.csv. Equality is byte '
          'for byte, with the expected hashes read from the original frozen manifest. '
          'run.json identifies execution scope and is outside this five-file equality target.'))
    add(p('CUDA execution matrix', 'sub'))
    block_commands = [c for c in full['commands'] if c['log'].startswith('cuda_verify_xy_')]
    variants = []
    for c in block_commands:
        argv = c['argv']
        variants.append(argv[argv.index('--fetch') + 1] + ' / block ' + argv[argv.index('--block') + 1])
    add(p('verify_xy variants: ' + '; '.join(variants) + '.'))
    add(p('Every checked CUDA execution reads back the full LUT and compares each update '
          'against the CPU implementation. The coordinator also runs a fresh repeated process, '
          'forces the PTX JIT path, restores a CPU-generated checkpoint into CUDA, and captures '
          'PTX plus SASS from the built executable.'))
    add(table(['Additional check', 'Evidence'], [
        ['17 + 47 checkpoint continuation', full['checkpoint_split_17_47']],
        ['Invalid command-line cases', str(full['negative_cli_cases']) + ' rejected'],
        ['Fresh-process repeat', 'cuda_repeat.txt - exit ' + str(command(full, 'cuda_repeat')['returncode'])],
        ['Forced PTX JIT', 'cuda_forced_ptx.txt - exit ' + str(command(full, 'cuda_forced_ptx')['returncode'])],
        ['CUDA capsule restart', 'cuda_resume.txt - exit ' + str(command(full, 'cuda_resume')['returncode'])],
    ], [.47, .53]))
    add(Spacer(1, 2 * mm))
    add(p('Results cover the disclosed profiles and probes. They do not exhaust every admitted '
          'state. Trace auditing checks emitted pulse/event/parity identities and endpoint '
          'count certificates; it does not reconstruct every past activity input.', 'small'))

    section(4, 'Fresh formal solver results')
    unsat = sum(t['actual'] == 'unsat' for t in formal['targets'])
    sat = sum(t['actual'] == 'sat' for t in formal['targets'])
    add(p(f"{formal['solver_version']}: {unsat} expected UNSAT results and {sat} expected SAT "
          'counterexamples. Each target returned its expected result with no solver error.'))
    rows = [[t['name'], t['expected'].upper(), t['actual'].upper()] for t in formal['targets']]
    formal_table = table(['Submitted SMT target', 'Expected', 'Observed'], rows, [.66, .17, .17], small=True)
    formal_table.setStyle(TableStyle([('TOPPADDING', (0, 1), (-1, -1), 3.5),
                                     ('BOTTOMPADDING', (0, 1), (-1, -1), 3.5)]))
    add(formal_table)
    add(Spacer(1, 3 * mm))
    add(p('The SAT targets are intentional: the last emitted bit does not uniquely determine '
          'the next state, and two data-bit flips can preserve parity. These are constructive '
          'counterexamples to stronger claims, rather than failing obligations.', 'small'))
    add(p('The formulas and expectations were not altered. Obligations establish their stated '
          'algebraic propositions in Z3 semantics; they do not model the whole C++/CUDA program. '
          'For example, the restoring-divider target checks eight-bit arithmetic.', 'small'))
    add(p('Source: formal/obligations.json. Results and solver proof/model text: '
          'validation/full/formal/report.json and the adjacent target logs. '
          'The independently repeated initial run is under validation/formal_initial/.', 'tiny'))

    section(5, 'Instrumentation and additional probes')
    add(p('Compute Sanitizer on the actual GPU', 'sub'))
    add(table(['Mode', 'Result', 'Exact log summary'], d['sanitizers'], [.20, .14, .66]))
    add(Spacer(1, 2 * mm))
    add(p('The coordinator invoked each mode with --error-exitcode 1 on an eight-update '
          'verify_xy run. These checks are evidence for those instrumented executions; '
          'their finite coverage remains distinct from a proof of every possible run.', 'small'))
    add(p('Additional boundary and failure-path evidence', 'sub'))
    add(p('Edge-probe status: ' + d['edges']['status'] + '. Source report: ' + args.edges.as_posix() + '.'))
    cases = d['edges']['cases']
    exact_cases = [name for name, result in cases.items() if 'five_file_sha256' in result]
    rejected_cases = [name for name, result in cases.items() if result.get('rejected_without_output')]
    diag = d['edges']['diagnostics']
    add(table(['Probe group', 'Observed evidence'], [
        ['Additional exact comparisons', str(len(exact_cases)) + ': block 64 and feedback-off native/Python/texture/global comparisons'],
        ['Invalid CUDA arguments', str(len(rejected_cases)) + ' rejected without creating output directories'],
        ['CUDA error handling', 'Wrapper contract passed; process-local hidden device reported its CUDA error'],
        ['Injected cell-state mismatch', diag['cell']['diagnostic']],
        ['Injected clock mismatch', diag['clock']['diagnostic']],
    ], [.37, .63], small=True))
    add(p('Faults were inserted only into isolated diagnostic copies. Both stopped after '
          'three successful updates and produced no final capsule or completed-run record. '
          'The production source and expected outputs remained unchanged.', 'small'))
    add(p('Nsight Compute captures', 'sub'))
    add(table(['Fetch path', 'Captured artifact', 'Bytes'], [
        [fetch, str(path.relative_to(root)).replace('\\', '/'), f'{size:,}']
        for fetch, path, size, sha in d['profiles']
    ], [.18, .58, .24], small=True))
    add(Spacer(1, 2 * mm))
    add(p('Both captures are available for inspection. No texture-cache speedup or throughput '
          'advantage is inferred. This implementation copies state to the host and compares it '
          'per update, so the verification run is not a throughput benchmark.'))
    add(p('Logs: validation/full/logs/sanitize_*.txt and profile_*.txt. '
          'The .ncu-rep files preserve the collected device metrics.', 'small'))

    section(6, 'Reproduction and evidence identity')
    add(p('Run from the revision root, with the installed toolchain on PATH. '
          'Choose unused output directories on every run. The supplied Z3 directory is '
          'local to this revision and was unpacked from an existing cached wheel after approval.'))
    add(p("$env:PATH=(Join-Path (Get-Location) 'local_tools/z3-4.15.4.0/bin')+';'+$env:PATH", 'code'))
    add(p('python tools/verify.py --cpu-only --formal --out validation/reproduce_cpu', 'code'))
    add(p('python tools/verify.py --hardware --formal --sanitizers --profile '
          '--cmake-cuda-toolset cuda=12.8 --out validation/reproduce_full', 'code'))
    add(p('Additional regressions use tools/verify_gpu_edges.py with --cpu, --gpu, --contract, '
          '--out and --diagnostics; fault builds also require --core-lib and --host-compiler '
          '(see the script\'s --help). All ' + str(len(d['edges']['commands'])) +
          ' exact command argument arrays, including compiler and executable paths, are recorded '
          'in validation/gpu_edges/verification.json.', 'small'))
    add(p('Preserved release and fixed expectations', 'sub'))
    add(p(f"All {len(d['entries'])} files in the original frozen 4.0 manifest still match. "
          f"The revision manifest independently matches {len(d['revision_entries'])} entries. "
          'The expected output manifest is identical in both directories.'))
    add(p('After the main runs, only README wording and revision patch/metadata were corrected. '
          'The audit confirms all compiled sources, tests, verification tools and inputs match '
          'the tested snapshot: validation/full/verified_source_manifest.txt.', 'small'))
    add(p('assets/closure_goldens.json  SHA-256', 'tiny'))
    add(p(d['revised_golden'], 'code'))
    add(p('Exact source and executable identities', 'sub'))
    artifacts = [root / 'src/cuda.cu', root / 'tools/verify.py', root / 'SHA256SUMS.txt',
                 find_exe(root / 'validation/full/cuda_build', 'gambit_cuda'),
                 find_exe(root / 'validation/full/build', 'gambit')]
    for artifact in artifacts:
        add(p(artifact.relative_to(root).as_posix(), 'tiny'))
        add(p(digest(artifact), 'code'))
    add(p('Evidence entry points', 'sub'))
    add(table(['Record', 'Purpose'], [
        ['REVISION.json and REVISION.patch', 'Disclosed source changes and base identity'],
        ['validation/full/verification.json', 'Hardware run, stages, commands and profile results'],
        ['validation/cpu/verification.json', 'Separate full CPU and formal execution'],
        [args.edges.as_posix(), 'Boundary and failure-path probes'],
        [args.audit.as_posix(), 'Independent completion audit'],
        ['local_tools/z3-4.15.4.0/PROVENANCE.json', 'Offline solver archive and extracted-file hashes'],
    ], [.56, .44], small=True))
    add(Spacer(1, 2 * mm))
    add(p('Hashes bind the identified bytes to this record. They do not establish authorship, '
          'authenticity, or reachable state history. Keep the logs and source beside the PDF '
          'when reproducing or reviewing this result.', 'tiny'))

    output = root / args.output
    output.parent.mkdir(parents=True, exist_ok=True)
    generated = dt.datetime.now(dt.timezone.utc).strftime('%Y-%m-%d %H:%M UTC')
    def decorate(canvas, doc):
        canvas.saveState()
        width, height = A4
        canvas.setFillColor(TEAL)
        canvas.rect(18 * mm, height - 16 * mm, width - 36 * mm, 1.1 * mm, fill=1, stroke=0)
        canvas.setStrokeColor(LINE)
        canvas.line(18 * mm, 17 * mm, width - 18 * mm, 17 * mm)
        canvas.setFont('Helvetica', 7)
        canvas.setFillColor(MUTED)
        canvas.drawString(18 * mm, 12 * mm, 'GAMBIT CLOSURE 4.0.1  |  FINAL VERIFICATION  |  ' + generated)
        canvas.drawRightString(width - 18 * mm, 12 * mm, str(doc.page) + ' / 6')
        canvas.restoreState()
    doc = SimpleDocTemplate(str(output), pagesize=A4, rightMargin=18 * mm,
        leftMargin=18 * mm, topMargin=23 * mm, bottomMargin=23 * mm,
        title='Gambit Closure 4.0.1 - Final Verification', author='Codex',
        subject='Evidence-backed CUDA repair and verification on RTX 5070 Ti Laptop GPU',
        pageCompression=1)
    doc.build(story, onFirstPage=decorate, onLaterPages=decorate)
    from pypdf import PdfReader
    reader = PdfReader(str(output))
    if len(reader.pages) != 6:
        raise ValueError(f'Layout overflow: expected 6 pages, produced {len(reader.pages)}; inspect and correct before delivery')
    text = '\n'.join(page.extract_text() or '' for page in reader.pages)
    for token in ('GPU_CPU_EXACT_PASS', 'CPU_PASS_GPU_NOT_RUN', 'one_bit_not_sufficient', d['revised_golden']):
        if token not in text:
            raise ValueError('PDF text check failed for ' + token)
    evidence = {'output': str(output), 'sha256': digest(output), 'pages': len(reader.pages),
                'generated_utc': generated, 'builder_sha256': digest(Path(__file__)),
                'source_reports': {str(path.relative_to(root)): digest(path) for path in (
                    root / 'validation/full/verification.json', root / 'validation/cpu/verification.json',
                    root / 'validation/full/formal/report.json', d['edges_path'], d['audit_path'], root / 'REVISION.json')},
                'visual_review': 'REQUIRED - render every page and inspect before delivery'}
    (root / 'validation/pdf_build_record.json').write_text(json.dumps(evidence, indent=2) + '\n')
    print(json.dumps(evidence, indent=2))


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--root', type=Path, default=ROOT)
    parser.add_argument('--original-root', type=Path, default=Path(
        r'C:\RUUDDENDAASKOANAL\Tom_Klootwijk_Gambit_Closed_Engine_4.0\Tom_Klootwijk_Gambit_Closure_4.0'))
    parser.add_argument('--edges', type=Path, default=Path('validation/gpu_edges/verification.json'))
    parser.add_argument('--audit', type=Path, default=Path('validation/completion_audit.json'))
    parser.add_argument('--output', type=Path, default=Path('output/pdf/Gambit_Closure_4.0.1_Verification.pdf'))
    args = parser.parse_args()
    build(args)


if __name__ == '__main__':
    main()
