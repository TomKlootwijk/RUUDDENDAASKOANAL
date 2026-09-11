from __future__ import annotations
import itertools
import json
import math
import random
import unittest
from dataclasses import replace
from tkuft.core import *
from tkuft.engine import *
from tkuft.codec import *
from tkuft import boolean as alu

def definition(key="d:a",deps=()):
    return seal({"id":key,"kind":"example","domain":"integer","codomain":"integer","dependencies":list(deps),"evaluation_phase":3,"parameters":{},"provenance":{"origin":"v2-construction"}})

class CanonicalRegistryTests(unittest.TestCase):
    def test_key_order(self):self.assertEqual(canonical_bytes({"b":2,"a":1}),canonical_bytes({"a":1,"b":2}))
    def test_utf8(self):self.assertEqual(canonical_bytes({"x":"drieëntwintig"}).decode(),'{"x":"drieëntwintig"}')
    def test_content_hash_exclusion(self):
        a=definition();b=dict(a,content_hash="changed");self.assertEqual(content_hash(a),content_hash(b))
    def test_change_detection(self):
        a=definition();a["parameters"]["x"]=1;self.assertFalse(verify(a))
    def test_nan(self):
        with self.assertRaises(ValueError):canonical_bytes({"x":math.nan})
    def test_order(self):self.assertEqual(Registry([definition("c",["b"]),definition("a"),definition("b",["a"])]).definition_order(),("a","b","c"))
    def test_order_tie(self):self.assertEqual(Registry([definition("z"),definition("a")]).definition_order(),("a","z"))
    def test_missing_dependency(self):
        with self.assertRaises(ValueError):Registry([definition("a",["b"])])
    def test_cycle(self):
        with self.assertRaises(ValueError):Registry([definition("a",["b"]),definition("b",["a"])])
    def test_duplicate(self):
        with self.assertRaises(ValueError):Registry([definition(),definition()])
    def test_isolation(self):
        r=Registry([definition()]);d=r.definition_at("d:a");d["parameters"]["x"]=5;self.assertTrue(r.verify_definition("d:a"))
    def test_queries(self):
        r=Registry([definition()]);x={"definition_ref":"d:a","literal":19};self.assertEqual(r.instances_of("d:a",[x]),[x]);self.assertEqual(r.explain_reference("d:a")["evaluation_phase"],3)
    def test_invalid_phase(self):
        d=definition();d["evaluation_phase"]=10
        with self.assertRaises(ValueError):Registry([seal(d)])
    def test_author_record(self):self.assertEqual(AUTHOR,{"name":"Tom Klootwijk","identifier":"NL200678942","date_of_birth":"10-07-1990"})

class CorpusGeometryTests(unittest.TestCase):
    def test_radix_thresholds(self):
        for b in (2,3,10,16):
            for k in range(1,10):
                self.assertEqual(len(radix_digits(b**k-1,b)),k);self.assertEqual(len(radix_digits(b**k,b)),k+1)
    def test_active_bits(self):
        self.assertEqual(active_bits(19),(0,1,4))
        for n in range(1000):self.assertEqual(sum(1<<k for k in active_bits(n)),n)
    def test_pascal(self):
        for n in range(64):
            for k in range(n+1):self.assertEqual(pascal_parity(n,k),math.comb(n,k)%2)
    def test_triangle(self):
        p=pulse_polygon(3);area=abs(sum(p[j][0]*p[(j+1)%3][1]-p[(j+1)%3][0]*p[j][1] for j in range(3)))/2;self.assertAlmostEqual(area,3*math.sqrt(3)/4)
    def test_degenerate_counts(self):self.assertEqual(len(pulse_polygon(1)),1);self.assertAlmostEqual(math.dist(*pulse_polygon(2)),2)
    def test_rotation_fixed_pivot(self):self.assertEqual(rotate((2,3),(2,3),1.234),(2,3))
    def test_noncommutation(self):
        p=(1,0);t=lambda p:(p[0]+1,p[1]);r=lambda p:rotate(p,(0,0),math.pi/2);self.assertGreater(math.dist(t(r(p)),r(t(p))),1)
    def test_double_wrap(self):
        a=orientation_wrap(.2,1,1,0);b=orientation_wrap(a[0],1,a[1],a[2]);self.assertAlmostEqual(b[0],.2);self.assertEqual(b[1:],(1,0))
    def test_grammar_count(self):
        for seed in ("[X][X]","[X][Y]"):
            for g in range(6):
                w=grammar_word(seed,g);self.assertEqual(sum(c in "XY" for c in w),2*3**g);self.assertEqual(w.count("["),w.count("]"))
    def test_grammar_budget(self):
        with self.assertRaises(ValueError):grammar_word("[X][Y]",8,100)

class DutchTests(unittest.TestCase):
    def test_19(self):
        x=dutch_number(19);self.assertEqual(x["segments"],["ne","gen","tien"]);self.assertEqual(x["binary"],"10011");self.assertTrue(x["count_match"])
    def test_23(self):
        x=dutch_number(23);self.assertEqual(x["orthography"],"drieëntwintig");self.assertEqual(x["spoken_order"],[3,"en",20])
    def test_99(self):self.assertEqual(dutch_number(99)["pulse_count"],6)
    def test_value_invariance(self):
        for n in range(100):
            x=dutch_number(n);self.assertEqual(chart_value(x["place_order"]),n);self.assertEqual(chart_value(x["spoken_order"]),n)
    def test_exact_match_set(self):self.assertEqual([n for n in range(100) if dutch_number(n)["count_match"]],[1,2,4,8,9,18,19,20,23,40,43,45,46,47,51,53,54,58,59,70,80,83,85,86,87,91,93,94])
    def test_irregulars(self):self.assertEqual([dutch_number(n)["hinge_kind"] for n in (11,12)],["irregular","irregular"])
    def test_bounds(self):
        for n in (-1,100,True,1.5):
            with self.assertRaises(ValueError):dutch_number(n)

class BooleanTests(unittest.TestCase):
    def test_full_adder(self):
        for a,b,c in itertools.product((0,1),repeat=3):
            s,k=alu.full_adder(a,b,c);self.assertEqual(s+2*k,a+b+c)
    def test_all_byte_additions(self):
        for a in range(256):
            for b in range(256):
                s,c=alu.add(alu.bits(a,8),alu.bits(b,8));self.assertEqual(alu.integer(s)+256*c,a+b)
    def test_small_subtraction_comparison(self):
        for a in range(32):
            for b in range(32):
                aa,bb=alu.bits(a,5),alu.bits(b,5);self.assertEqual(alu.integer(alu.subtract(aa,bb)),(a-b)%32);self.assertEqual(alu.less(aa,bb),int(a<b))
    def test_small_multiplication(self):
        for a in range(32):
            for b in range(32):self.assertEqual(alu.integer(alu.multiply(alu.bits(a,5),alu.bits(b,5))),a*b%32)
    def test_small_division(self):
        for a in range(32):
            for b in range(1,32):
                q,r=alu.divide(alu.bits(a,5),alu.bits(b,5));self.assertEqual((alu.integer(q),alu.integer(r)),divmod(a,b))
    def test_wide_division(self):
        rng=random.Random(426)
        for _ in range(40):
            a,b=rng.getrandbits(64),rng.getrandbits(64) or 1;q,r=alu.divide(alu.bits(a,64),alu.bits(b,64));self.assertEqual((alu.integer(q),alu.integer(r)),divmod(a,b))
    def test_zero_divisor(self):
        with self.assertRaises(ValueError):alu.divide((0,0),(0,0))

class DynamicTests(unittest.TestCase):
    def setUp(self):self.seed,self.s=integer_chart_fixture()
    def test_initial_material(self):self.assertEqual(material(self.s),18677)
    def test_neighbours(self):
        p=self.seed.parameters
        for i in range(p.N):
            self.assertEqual(len(neighbours(i,p)),3)
            for j in neighbours(i,p):self.assertIn(i,neighbours(j,p))
    def test_truncation(self):self.assertEqual([trunc0(x,256) for x in (-257,-255,0,255,257)],[-1,0,0,0,1])
    def test_codec_edges(self):
        for r in (0,1,D//2,D-1):
            for k in (0,1,D//2,D-1,D):
                q,s=pulse_codec(r,k);self.assertTrue(0<=s<D);self.assertEqual(D*q+s,r+k)
    def test_restarted_segment(self):
        r0=r=12345;K=Q=0
        for k in (0,1,D,12345,65535)*20:q,r=pulse_codec(r,k);Q+=q;K+=k
        self.assertEqual(D*Q+r,r0+K);self.assertLess(abs(Q-K/D),1)
    def test_hysteresis(self):
        self.assertEqual(latch_step(0,-49,49),(1,1,1));self.assertEqual(latch_step(1,49,49),(0,1,0));self.assertEqual(latch_step(1,1,49),(1,0,0))
    def test_512_updates(self):
        s=self.s;K=[0]*64;Q=[0]*64;events=[0]*64
        for _ in range(512):
            s,_=tick(self.seed,s);self.assertEqual(material(s),18677)
            for i,c in enumerate(s.cells):K[i]+=c.z;Q[i]+=c.pulse;events[i]^=c.flags>>3&1
        for i,c in enumerate(s.cells):self.assertEqual(D*Q[i]+c.r,K[i]);self.assertEqual(events[i],c.latch)
    def test_determinism(self):self.assertEqual(tick(self.seed,self.s),tick(self.seed,self.s))
    def test_ablation(self):
        other,_=integer_chart_fixture(False);self.assertNotEqual(sample_all(self.seed,self.s),sample_all(other,self.s))
    def test_one_read_witness(self):
        a=b=self.s;first_s=first_q=None
        for n in range(64):
            a,_=tick(self.seed,a);b,_=tick(self.seed,b,7 if n==3 else None)
            if first_s is None and a!=b:first_s=n
            if first_q is None and pack_planes(a)["pulse"]!=pack_planes(b)["pulse"]:first_q=n
        self.assertEqual((first_s,first_q),(3,9))
    def test_control(self):
        s=self.s
        for _ in range(64):s,_=tick(self.seed,s)
        self.assertEqual((s.a,s.g,s.cooldown),(0,1,16))
    def test_last_pulse_not_sufficient(self):
        out,_=tick(self.seed,self.s);k=out.cells[0].z
        alt=replace(self.s,cells=(replace(self.s.cells[0],r=D-k),)+self.s.cells[1:])
        next_alt,_=tick(self.seed,alt)
        self.assertEqual(pack_planes(self.s)["pulse"],pack_planes(alt)["pulse"]);self.assertNotEqual(out.cells[0].pulse,next_alt.cells[0].pulse)
    def test_gather_scatter(self):
        s,_=tick(self.seed,self.s);samples=sample_all(self.seed,s);p=self.seed.parameters
        for attr in ("U","V"):
            scatter=[getattr(c,attr) for c in s.cells]
            for i,c in enumerate(s.cells):
                for j in neighbours(i,p):
                    if samples[i][0]<=0 and samples[j][0]<=0:
                        shift=p.s_open if c.latch or s.cells[j].latch else p.s_closed;amt=getattr(c,attr)>>shift;scatter[i]-=amt;scatter[j]+=amt
            gather=[]
            for i,c in enumerate(s.cells):
                total=getattr(c,attr)
                for j in neighbours(i,p):
                    if samples[i][0]<=0 and samples[j][0]<=0:
                        shift=p.s_open if c.latch or s.cells[j].latch else p.s_closed;total+=(getattr(s.cells[j],attr)>>shift)-(getattr(c,attr)>>shift)
                gather.append(total)
            self.assertEqual(scatter,gather)
    def test_invalid_dimensions(self):
        with self.assertRaises(ValueError):replace(self.seed.parameters,A=33).validate()
    def test_invalid_mass(self):
        with self.assertRaises(ValueError):validate_state(replace(self.seed,initial_mass=1),self.s)

class CodecTests(unittest.TestCase):
    def setUp(self):self.seed,self.s=integer_chart_fixture()
    def test_length(self):self.assertEqual(state_bit_count(self.seed),7579);self.assertEqual(len(encode_state(self.seed,self.s)),948)
    def test_roundtrip(self):
        for _ in range(33):
            self.s,_=tick(self.seed,self.s);self.assertEqual(decode_state(self.seed,encode_state(self.seed,self.s)),self.s)
    def test_padding(self):
        raw=bytearray(encode_state(self.seed,self.s));raw[-1]|=128
        with self.assertRaises(ValueError):decode_state(self.seed,bytes(raw))
    def test_truncation(self):
        with self.assertRaises(ValueError):decode_state(self.seed,encode_state(self.seed,self.s)[:-1])
    def test_capsule(self):self.assertEqual(decode_capsule(encode_capsule(self.seed,self.s)),(self.seed,self.s))
    def test_tamper(self):
        obj=json.loads(encode_capsule(self.seed,self.s));obj["payload"]["initial_mass"]+=1
        with self.assertRaises(ValueError):decode_capsule(json.dumps(obj).encode())
    def test_restart(self):
        a=b=self.s
        for _ in range(64):a,_=tick(self.seed,a)
        for _ in range(23):b,_=tick(self.seed,b)
        seed,b=decode_capsule(encode_capsule(self.seed,b))
        for _ in range(41):b,_=tick(seed,b)
        self.assertEqual(a,b)
    def test_bit_word(self):self.assertEqual(bits_state(self.seed,state_bits(self.seed,self.s)),self.s)
    def test_packing(self):
        s=self.s
        for _ in range(4):s,_=tick(self.seed,s)
        p=pack_planes(s)
        for i,c in enumerate(s.cells):self.assertEqual(p["pulse"][i//32]>>(i%32)&1,c.pulse)
        for word,parity in zip(p["pulse"],p["parity"]):self.assertEqual(word.bit_count()%2,parity)
    def test_even_parity_mask(self):
        for w in (0,1,123456789,65535):self.assertEqual(w.bit_count()%2,(w^3).bit_count()%2)
