from __future__ import annotations
import itertools
import math
import unittest
from tkuft.uuid import *
from tkuft.identity import *
from tkuft.wrap import AddressChart
from tkuft.engine import integer_chart_fixture,tick,latch_step
from tkuft.core import seal

class UUIDTests(unittest.TestCase):
    def test_source_equation(self):self.assertEqual(uu_id(2,1,3,5),1)
    def test_relational_trichotomy(self):self.assertEqual([relation(x,1) for x in (0,1,2)],["<","=",">"])
    def test_orientation_symmetry(self):
        for d,t in ((1,3),(2,-4),(.25,.5)):self.assertEqual(boundary_delta(d,t),boundary_delta(2*t-d,t))
    def test_commutative(self):
        for a,b in itertools.product((0,.25,1,5),repeat=2):self.assertEqual(uu_fold((a,b)),uu_fold((b,a)))
    def test_associative(self):
        for a,b,c in itertools.product((0,.25,1,5),repeat=3):self.assertEqual(uu_fold((uu_fold((a,b)),c)),uu_fold((a,uu_fold((b,c)))))
    def test_idempotent(self):
        for a in (0,.25,1,5):self.assertEqual(uu_fold((a,a)),a)
    def test_empty_identity(self):self.assertTrue(math.isinf(uu_fold(())))
    def test_nonnegative_domain(self):
        with self.assertRaises(ValueError):uu_fold((1,-1))
    def test_nonfinite(self):
        for x in (math.nan,math.inf):
            with self.assertRaises(ValueError):boundary_delta(x,1)
    def test_sphere_boundary_exact(self):
        h=SphereHorizon("s",(0,0),2)
        for p in ((0,0),(2,0),(3,4)):
            self.assertEqual(h.delta(p),abs(math.hypot(*p)-2))
    def test_union_zero_set(self):
        a=SphereHorizon("a",(0,),1);b=SphereHorizon("b",(3,),1);u=TaggedUnion((a,b))
        for x in (-2,-1,0,1,2,3,4,5):self.assertEqual(u.evaluate((x,))["value"]==0,a.delta((x,))==0 or b.delta((x,))==0)
    def test_epsilon_union(self):
        a=SphereHorizon("a",(0,),1);b=SphereHorizon("b",(3,),1);u=TaggedUnion((a,b))
        for k in range(100):
            x=k/10-2;self.assertEqual(u.evaluate((x,))["value"]<=.3,a.delta((x,))<=.3 or b.delta((x,))<=.3)
    def test_tie_witnesses(self):
        u=TaggedUnion((SphereHorizon("b",(2,),1),SphereHorizon("a",(0,),1)))
        self.assertEqual(u.evaluate((1,))["witnesses"],["a","b"])
    def test_duplicate_geometry_retains_ids(self):
        u=TaggedUnion((SphereHorizon("a",(0,),1),SphereHorizon("b",(0,),1)))
        self.assertEqual(len(u.layers),2);self.assertEqual(u.evaluate((0,))["witnesses"],["a","b"])
    def test_id_conflict(self):
        with self.assertRaises(ValueError):TaggedUnion((SphereHorizon("a",(0,),1),SphereHorizon("a",(1,),1)))
    def test_empty_tagged(self):self.assertEqual(TaggedUnion(()).evaluate((0,))["status"],"empty")
    def test_tagged_merge(self):
        a=TaggedUnion((SphereHorizon("a",(0,),1),));b=TaggedUnion((SphereHorizon("b",(2,),1),));self.assertEqual(a.merge(b).evaluate((1,)),b.merge(a).evaluate((1,)))
    def test_solid_union_is_distinct(self):
        u=TaggedUnion((SphereHorizon("inner",(0,0),1),SphereHorizon("outer",(0,0),2)))
        self.assertEqual(u.evaluate((1,0))["value"],0);self.assertEqual(abs(math.dist((1,0),(0,0))-2),1)
    def test_source_and_horizon_bits(self):
        self.assertEqual(source_bit(0),0);self.assertEqual(horizon_bit(0,1),1)
        self.assertEqual(source_bit(1),1);self.assertEqual(horizon_bit(1,1),0)
    def test_open_hinge_equivalence(self):
        for f in range(-1000,1001):
            for old in (0,1):
                d,t=open_engine_sample(f);self.assertEqual(open_latch(old,d,t,49),latch_step(old,f,49))
    def test_scalar_delta_loses_side(self):
        self.assertEqual(boundary_delta(-50,0),boundary_delta(50,0));self.assertNotEqual(latch_step(0,-50,49),latch_step(0,50,49))
    def test_distance_lipschitz(self):
        h=SphereHorizon("s",(0,0),1)
        for k in range(100):
            a=(k/10,.2);b=(k/10+.03,.24);self.assertLessEqual(abs(h.delta(a)-h.delta(b)),math.dist(a,b)+1e-12)

class StateHorizonTests(unittest.TestCase):
    def test_all_eight_bit_words(self):
        for n in range(256):
            b=tuple(n>>j&1 for j in range(8));h=StateHorizon(b)
            self.assertEqual(h.decode(),b);self.assertEqual(h.decode(1.5),b)
    def test_zero_anchor(self):
        h=StateHorizon((0,)*8);self.assertEqual(h.evaluate(0),.25);self.assertEqual(h.evaluate(3),2.75)
    def test_active_center_nonzero(self):self.assertEqual(StateHorizon((1,)).evaluate(3),.25)
    def test_boundary_zero(self):
        h=StateHorizon((1,0,1))
        for x in (-.25,.25,2.75,3.25,8.75,9.25):self.assertEqual(h.evaluate(x),0)
    def test_direct_min_agreement(self):
        h=StateHorizon((0,1,0,1,1,0,0,1))
        for k in range(600):
            x=k/20-1;self.assertAlmostEqual(h.evaluate(x),min(abs(abs(x-c)-.25) for c in h.active_centres()))
    def test_invalid_decoder(self):
        for t in (0,.249,2.75,3):
            with self.assertRaises(ValueError):StateHorizon((1,)).decode(t)
    def test_query_error_margin(self):
        h=StateHorizon((0,1,0,1,1,0,0,1))
        for j,b in enumerate(h.bits,1):
            for error in (-1.249,1.249):self.assertEqual(int(h.evaluate(3*j)+error<=1.5),b)
    def test_full_state_roundtrip(self):
        seed,s=integer_chart_fixture();self.assertEqual(decode_horizon(seed,encode_horizon(seed,s)),s)
    def test_sixteen_conjugate_updates(self):
        seed,s=integer_chart_fixture();h=encode_horizon(seed,s)
        for _ in range(16):
            s,d=tick(seed,s);h,hd=tick_horizon(seed,h);self.assertEqual(decode_horizon(seed,h),s);self.assertEqual(d,hd)
    def test_pulse_addresses(self):
        seed,s=integer_chart_fixture()
        for _ in range(8):
            s,_=tick(seed,s);h=encode_horizon(seed,s)
            for i,c in enumerate(s.cells):self.assertEqual(int(h.evaluate(3*previous_pulse_position(i))<=.25),c.pulse)
    def test_canonical_positions(self):self.assertEqual(cell_bit_position(0,0),28);self.assertEqual(previous_pulse_position(0),143);self.assertEqual(previous_pulse_position(7),969)
    def test_bitwise_or_history_projection(self):
        a=(0,1,0,1);b=(1,0,0,1);ha,hb=StateHorizon(a),StateHorizon(b);hc=StateHorizon(tuple(x|y for x,y in zip(a,b)))
        for k in range(100):
            x=k/5-1;self.assertAlmostEqual(hc.evaluate(x),min(ha.evaluate(x),hb.evaluate(x)))

class TemporalTests(unittest.TestCase):
    def test_zero_decay_integral(self):self.assertEqual(integrate_segments(((1,2),(2,3)),0)["integral"],8)
    def test_constant_retention(self):
        got=integrate_segments(((1,2),(2,2)),.5);self.assertAlmostEqual(got["integral"],4*(1-math.exp(-1.5)));self.assertAlmostEqual(got["normalized_mean"],2)
    def test_segment_composition(self):
        a=integrate_segments(((1,2),(2,4)),.3)["integral"];b=absorbing_step(absorbing_step(0,2,1,.3),4,2,.3);self.assertAlmostEqual(a,b)
    def test_order_matters(self):self.assertNotEqual(integrate_segments(((1,2),(1,4)),.5)["integral"],integrate_segments(((1,4),(1,2)),.5)["integral"])
    def test_empty_integral(self):self.assertEqual(integrate_segments((),.5)["integral"],0);self.assertIsNone(integrate_segments((),.5)["normalized_mean"])
    def test_negative_decay(self):
        with self.assertRaises(ValueError):integrate_segments(((1,2),),-.1)
    def test_empty_history(self):self.assertEqual(history_envelope([], (0,),0)["status"],"empty")
    def test_causal_history_selection(self):
        events=[{"id":"a","time":0,"centre":[0],"threshold":1},{"id":"b","time":2,"centre":[3],"threshold":1}]
        self.assertEqual(history_envelope(events,(4,),1)["value"],3);self.assertEqual(history_envelope(events,(4,),2)["value"],0)
    def test_history_min_monotonic(self):
        events=[{"id":str(i),"time":i,"centre":[i],"threshold":.5} for i in range(4)]
        values=[history_envelope(events,(3,),t)["value"] for t in range(4)];self.assertEqual(values,sorted(values,reverse=True))
    def test_continuity_not_transitive(self):
        path=continuity_path(((0,),(.75,),(1.5,)),1);self.assertTrue(path["continuous"]);self.assertGreater(math.dist((0,),(1.5,)),1)
    def test_continuity_break(self):self.assertFalse(continuity_path(((0,),(2,)),1)["continuous"])
    def test_single_state(self):self.assertTrue(continuity_path(((0,),),0)["continuous"])

class LineageTests(unittest.TestCase):
    def build(self):
        h=Lineage();h.append("a",0,[],{"label":"synthetic root"});h.append("b",1,["a"],{});h.append("c",1,["a"],{});h.append("d",2,["b","c"],{});return h
    def test_split_merge(self):self.assertEqual(self.build().ancestors("d"),("a","b","c"))
    def test_restore(self):
        h=self.build();self.assertEqual(Lineage(h.records()).records(),h.records())
    def test_missing_parent(self):
        with self.assertRaises(ValueError):Lineage().append("x",0,["missing"],{})
    def test_duplicate(self):
        h=self.build()
        with self.assertRaises(ValueError):h.append("a",3,["d"],{})
    def test_nonmonotone_time(self):
        h=self.build()
        with self.assertRaises(ValueError):h.append("e",1,["d"],{})
    def test_payload_tamper(self):
        rows=self.build().records();rows[0]["payload"]["x"]=1
        with self.assertRaises(ValueError):Lineage(rows)
    def test_parent_tamper(self):
        rows=self.build().records();rows[-1]["parent_hashes"][0]="sha256:"+"0"*64;rows[-1]=seal(rows[-1])
        with self.assertRaises(ValueError):Lineage(rows)
    def test_read_isolation(self):
        h=self.build();rows=h.records();rows[0]["payload"]["x"]=1;self.assertNotIn("x",h.records()[0]["payload"])

class WrapTests(unittest.TestCase):
    def test_address_count(self):self.assertEqual(AddressChart().count,7579)
    def test_control_axis(self):self.assertEqual(AddressChart().centre(1),(0,0,0))
    def test_first_cell(self):self.assertEqual(AddressChart().centre(28),(.03125,0,0))
    def test_local_layer(self):
        c=AddressChart();self.assertAlmostEqual(c.centre(29)[2],1/64);self.assertEqual(c.address(29)["local_bit"],1)
    def test_unique_addresses(self):
        c=AddressChart();self.assertEqual(len({c.centre(j) for j in range(1,c.count+1)}),c.count)
    def test_separation(self):
        c=AddressChart();self.assertAlmostEqual(c.minimum_separation,2/32*math.sin(math.pi/32));self.assertAlmostEqual(c.horizon_radius,c.minimum_separation/4)
    def test_3d_bit_queries(self):
        c=AddressChart();bits=tuple(int(j in (1,28,143,969,7579)) for j in range(1,c.count+1))
        for j in (1,2,27,28,29,143,144,969,970,7579):self.assertEqual(int(c.unsigned_field(bits,c.centre(j))<=c.horizon_radius+1e-14),bits[j-1])
    def test_origin_chart_flag(self):self.assertTrue(AddressChart().raw_logpolar(0,0)["core"])
    def test_wrap_bounds(self):
        with self.assertRaises(ValueError):AddressChart().centre(0)
