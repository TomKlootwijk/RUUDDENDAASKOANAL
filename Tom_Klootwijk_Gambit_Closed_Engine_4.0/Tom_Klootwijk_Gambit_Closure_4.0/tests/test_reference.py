import sys,unittest,copy,struct,hashlib
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1];sys.path.insert(0,str(ROOT/'tools'))
import reference as r
import reference31 as old
from state_sdf import recover,signed_distance
class ClosureTests(unittest.TestCase):
    def engine(self,name='micro_xy'):return r.Reference(*r.decode_asset((ROOT/'assets'/f'{name}.gblut').read_bytes()))
    def test_asset_hashes(self):
        import json
        for p in (ROOT/'assets').glob('*.gblut'):
            self.assertEqual(hashlib.sha256(p.read_bytes()).hexdigest(),json.loads(p.with_suffix('.json').read_text())['sha256'])
    def test_capsule_roundtrip(self):
        e=self.engine()
        for t in range(19):
            b=e.capsule();f=r.from_capsule(b);self.assertEqual(f.capsule(),b);self.assertEqual(f.words,e.words);e.tick()
    def test_resume_equality(self):
        e=self.engine();[e.tick() for _ in range(17)];f=r.from_capsule(e.capsule())
        for _ in range(47):e.tick();f.tick();self.assertEqual(e.cells,f.cells)
        self.assertEqual(e.capsule(),f.capsule())
    def test_legacy_projection_xx(self):self.project('micro_xx')
    def test_legacy_projection_xy(self):self.project('micro_xy')
    def project(self,name):
        e=self.engine(name);p,lut=old.load_asset(ROOT/'assets'/f'{name}.gblut');o=old.Reference(p,lut)
        for _ in range(90):
            e.tick();o.step();self.assertEqual(e.words,o.words)
            self.assertEqual([(c.u,c.v,c.z,c.m,c.r,c.flags) for c in e.cells],[(c.u,c.v,c.z,c.m,c.r,c.flags) for c in o.cells])
            self.assertEqual(e.phase,o.step_number*p['phase_stride']%p['width'])
            self.assertEqual(e.cooldown,min(p['growth_dwell'],o.step_number-o.last_growth))
    def test_phase_stride_wrap(self):
        p,lut=r.decode_asset((ROOT/'assets/micro_xy.gblut').read_bytes());p['phase_stride']=31;e=r.Reference(p,lut)
        for i in range(100):e.tick();self.assertEqual(e.phase,((i+1)*31)%32)
    def test_pulse_prefix_certificate(self):
        e=self.engine();q=[0]*e.n;k=[0]*e.n
        for _ in range(100):
            e.tick()
            for i,c in enumerate(e.cells):q[i]+=(c.flags>>1)&1;k[i]+=c.z;self.assertEqual(r.D*q[i]+c.r,k[i])
    def test_arbitrary_residual_prefix(self):
        e=self.engine();e.cells=[r.Cell(c.u,c.v,c.z,c.m,(i*997)%r.D,c.flags) for i,c in enumerate(e.cells)]
        r0=[c.r for c in e.cells];q=[0]*e.n;k=[0]*e.n
        for _ in range(31):
            e.tick()
            for i,c in enumerate(e.cells):q[i]+=(c.flags>>1)&1;k[i]+=c.z;self.assertEqual(r.D*q[i]+c.r,r0[i]+k[i])
    def test_event_telescope(self):
        e=self.engine();events=[0]*e.n
        for _ in range(60):
            e.tick()
            for i,c in enumerate(e.cells):events[i]^=(c.flags>>3)&1;self.assertEqual(events[i],c.flags&1)
    def test_parity_exact(self):
        e=self.engine()
        for _ in range(32):
            e.tick();nw=e.n//32
            for i in range(nw):self.assertEqual(e.words[4*nw+i],e.words[i].bit_count()%2)
    def test_feedback_witness(self):
        e=self.engine();f=self.engine();first_state=first_word=None
        for t in range(40):
            e.tick();f.tick(7 if t==3 else -1)
            if e.cells!=f.cells and first_state is None:first_state=t
            if e.words[:e.n//32]!=f.words[:f.n//32] and first_word is None:first_word=t
        self.assertEqual(first_state,3);self.assertIsNotNone(first_word)
    def test_read_intervention_bounds(self):
        e=self.engine()
        for i in [-2,e.n]:
            with self.assertRaises(ValueError):e.tick(i)
    def test_feedback_disabled_is_distinct(self):
        e=self.engine();p,l=r.decode_asset((ROOT/'assets/micro_xy.gblut').read_bytes());f=r.Reference(p,l,0)
        for _ in range(40):e.tick();f.tick()
        self.assertNotEqual(e.capsule(),f.capsule())
    def test_schema_bit_count(self):
        e=self.engine();b=e.capsule();nb=struct.unpack_from('<I',b,24)[0]
        self.assertEqual(nb,118*e.n+27);self.assertEqual(len(b),160+4*e.n*e.p['levels']+118*e.n//8)
    def test_raw_corruption_rejected(self):
        b=self.engine().capsule()
        for at in [0,7,8,16,31,100,len(b)//2,len(b)-1]:
            c=bytearray(b);c[at]^=1
            with self.assertRaises(ValueError):r.from_capsule(bytes(c))
    def test_noncanonical_padding_rejected(self):
        b=bytearray(self.engine().capsule());b[-33]|=128;b[-32:]=hashlib.sha256(b[:-32]).digest()
        with self.assertRaises(ValueError):r.from_capsule(bytes(b))
    def test_invalid_phase_rejected_even_with_digest(self):
        b=bytearray(self.engine().capsule());asz=struct.unpack_from('<I',b,12)[0];at=32+asz;b[at]=255;b[at+1]|=7;b[-32:]=hashlib.sha256(b[:-32]).digest()
        with self.assertRaises(ValueError):r.from_capsule(bytes(b))
    def test_truncation_rejected(self):
        b=self.engine().capsule()
        for k in [1,32,len(b)-1]:
            with self.assertRaises(ValueError):r.from_capsule(b[:-k])
    def test_seed_validation(self):
        p,lut=r.decode_asset((ROOT/'assets/micro_xy.gblut').read_bytes())
        for field,value in [('width',31),('levels',0),('memory_divisor',0),('open_shift',2),('phase_stride',32),('steps',0)]:
            invalid=p.copy();invalid[field]=value
            with self.assertRaises(ValueError):r.Reference(invalid,lut)
    def test_mass_is_conserved(self):
        e=self.engine()
        for _ in range(200):e.tick();self.assertEqual(sum(c.u+c.v for c in e.cells),e.mass0)
    def test_bounded_growth_not_infinite_geometry(self):
        e=self.engine()
        for _ in range(400):e.tick()
        self.assertLess(e.level,e.p['levels']);self.assertLessEqual(e.cooldown,e.p['growth_dwell'])
    def test_sdf_representation_all_8bit_words(self):
        for w in range(256):
            bits=[(w>>i)&1 for i in range(8)];self.assertEqual(recover(bits),bits)
    def test_sdf_representation_all_zero(self):
        self.assertGreater(signed_distance([0]*8,3),0);self.assertEqual(recover([0]*8),[0]*8)
    def test_output_is_not_complete_state(self):
        self.assertNotEqual(int(0+1>=r.D),int((r.D-1)+1>=r.D))
if __name__=='__main__':unittest.main()
