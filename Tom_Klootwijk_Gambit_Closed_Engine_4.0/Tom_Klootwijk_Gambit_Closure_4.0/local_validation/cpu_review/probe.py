"""Additional deterministic validation; frozen release files are read-only."""
from pathlib import Path
import hashlib, json, random, struct, subprocess, sys

ROOT = Path(__file__).resolve().parents[2]
OUT = Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT / 'tools'))
import reference as ref

EXE = ROOT / 'local_validation/20260911_cpu_formal/build/Release/gambit.exe'
results = {'scope': 'Additional deterministic CPU/native/Boolean/Python edge and malformed-capsule checks', 'cases': []}

def run_case(path, backend, steps, name):
    out = OUT / name
    command = [str(EXE), '--resume', str(path), '--steps', str(steps), '--backend', backend, '--out', str(out)]
    p = subprocess.run(command, text=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    (OUT / (name + '.log')).write_text(p.stdout, encoding='utf-8')
    return p.returncode, out

def altered(raw, at, value, width=32):
    b = bytearray(raw)
    byte, offset = divmod(at, 8)
    count = (offset + width + 7) // 8
    chunk = int.from_bytes(b[byte:byte+count], 'little')
    mask = ((1 << width) - 1) << offset
    chunk = (chunk & ~mask) | (value << offset)
    b[byte:byte+count] = chunk.to_bytes(count, 'little')
    b[-32:] = hashlib.sha256(b[:-32]).digest()
    return bytes(b)

p0, _ = ref.decode_asset((ROOT/'assets/micro_xy.gblut').read_bytes())
rng = random.Random(20260911)
for i in range(10):
    p = p0.copy()
    p.update(width=2048 if i == 9 else 32, height=2, levels=1 if i % 2 == 0 else 5,
             start_level=0, phase_stride=0 if i%3 == 0 else (2047 if i == 9 else 31),
             feedback_angle=2047 if i == 9 else 31,
             threshold=1 if i%2 else 32767,
             feedback_gain=0 if i%3 == 0 else 16384,
             memory_divisor=1 if i%2 else 65536,
             open_shift=3 if i%2 else 16, closed_shift=16,
             reaction_uv_shift=1 if i%2 else 16, reaction_vu_shift=16 if i%2 else 1,
             growth_dwell=1 if i%2 else 4096, growth_divisor=1 if i%2 else 65536,
             seed=0xffffffff if i%2 else 0)
    texels = [rng.choice([0, 0x0000ffff, 0xffff0000, 0xffffffff, 0x80008000])
              for _ in range(p['width']*p['height']*p['levels'])]
    texels[0] = 0
    e = ref.Reference(p, texels, i%2)
    masses = [0]*e.n
    masses[[0, 31, 32, e.n-1][i%4]] = e.mass0
    e.cells = [ref.Cell(mass if i%2 else 0, 0 if i%2 else mass,
                       [0, 65536, 32768][j%3], [65536, 0, 32768][j%3],
                       [0, 65535, 1][j%3], j%16) for j,mass in enumerate(masses)]
    e.phase = p['width']-1
    e.level = p['levels']-1 if i%3 else 0
    e.cooldown = p['growth_dwell'] if i%3 else 0
    e.validate(); e.pack_words()
    raw = e.capsule()
    source = OUT / f'edge_{i}.gbc'; source.write_bytes(raw)
    steps = 2 if i == 9 else 5
    for _ in range(steps): e.tick()
    expected = e.capsule()
    for backend in ('native', 'gates'):
        code, out = run_case(source, backend, steps, f'edge_{i}_{backend}')
        match = code == 0 and (out/'final.gbc').read_bytes() == expected
        results['cases'].append({'kind':'valid_boundary','case':i,'backend':backend,'cells':e.n,'steps':steps,'returncode':code,'python_final_capsule_equal':match})
        if not match: raise AssertionError(results['cases'][-1])
    print(f'Edge case {i}: native and gates equal Python', flush=True)

base = ref.Reference(*ref.decode_asset((ROOT/'assets/micro_xy.gblut').read_bytes()))
raw = base.capsule()
state = (32 + struct.unpack_from('<I', raw, 12)[0])*8
mutations = [
    ('magic',0,0,8), ('version',8*8,2,32), ('asset_length',12*8,92,32),
    ('feedback',16*8,2,32), ('mass_descriptor',20*8,base.mass0+1,32),
    ('state_bits',24*8,27+118*base.n+1,32), ('reserved',28*8,1,32),
    ('asset_magic',32*8,0,8), ('asset_version',40*8,2,32), ('asset_count',44*8,18,32),
    ('phase',state,2047,11), ('level',state+11,7,3), ('cooldown',state+14,8191,13),
    ('mass_state',state+27,0xffffffff,32), ('z_state',state+27+64,65537,17),
    ('memory_state',state+27+81,65537,17), ('padding',(len(raw)-33)*8+7,1,1),
]
for key,value in [('width',31),('height',1),('levels',0),('start_level',5),('steps',0),
                  ('threshold',0),('feedback_gain',16385),('memory_divisor',0),
                  ('phase_stride',32),('feedback_angle',32),('open_shift',2),
                  ('closed_shift',17),('reaction_uv_shift',0),('reaction_vu_shift',17),
                  ('growth_dwell',4097),('growth_divisor',0),('pair',2),('device_budget_mib',15)]:
    mutations.append((f'param_{key}',(48+4*ref.FIELDS.index(key))*8,value,32))
for name,at,value,width in mutations:
    bad = altered(raw,at,value,width)
    path = OUT/f'malformed_{name}.gbc'; path.write_bytes(bad)
    try: ref.from_capsule(bad)
    except ValueError: python_rejected = True
    else: python_rejected = False
    code,_ = run_case(path,'native',1,f'malformed_{name}_run')
    results['cases'].append({'kind':'malformed_resigned','case':name,'native_returncode':code,'python_rejected':python_rejected})
    if code != 1 or not python_rejected: raise AssertionError(results['cases'][-1])

results['status'] = 'PASS'
results['valid_boundary_executions'] = 20
results['malformed_resigned_cases'] = len(mutations)
(OUT/'probe_results.json').write_text(json.dumps(results,indent=2)+'\n',encoding='utf-8')
print(f'PASS: 20 native/gates boundary executions equal Python; {len(mutations)} rehashed malformed capsules rejected by native and Python')
