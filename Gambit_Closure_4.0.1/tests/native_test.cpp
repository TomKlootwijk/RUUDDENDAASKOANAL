#include "closure/engine.hpp"
#include "closure/boolean.hpp"
#include <iostream>
#include <random>
#include <stdexcept>
#include <algorithm>
using namespace closure;using namespace closure::bits;
static uint64_t checks=0;
static void check(bool v,const char* what){++checks;if(!v)throw std::runtime_error(what);}
static void same(const Engine& a,const Engine& b){
    check(a.clock.phase==b.clock.phase && a.clock.level==b.clock.level && a.clock.cooldown==b.clock.cooldown,"Control equality");
    gambit::compare_states(a.cells,b.cells,0);check(a.words==b.words,"Word equality");
}
static void rejected(const std::vector<uint8_t>& b){bool caught=false;try{auto e=from_capsule(b);(void)e;}catch(const std::exception&){caught=true;}check(caught,"Malformed capsule accepted");}
static void resign(std::vector<uint8_t>& b){auto pre=std::vector<uint8_t>(b.begin(),b.end()-32);auto h=sha256(pre);std::copy(h.begin(),h.end(),b.end()-32);}
int main(int argc,char** argv){try{
    if(argc!=2)throw std::runtime_error("Asset argument required");
    check(hex_digest({})=="e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855","SHA empty");
    check(hex_digest({'a','b','c'})=="ba7816bf8f01cfea414140de5dae2223b00361a396177a9cb410ff61f20015ad","SHA abc");
    check(hex_digest(std::vector<uint8_t>(1000000,'a'))=="cdc76e5c9914fb9281a1c7e284d73e67f1809a48a497200e046d39ccc7112cd0","SHA million a");
    using B=Word<8>;
    for(unsigned a=0;a<256;++a)for(unsigned b=0;b<256;++b){auto x=B::from(a),y=B::from(b);
        check(add(x,y).value()==((a+b)&255),"Exhaustive add8");check(sub(x,y).value()==((a-b)&255),"Exhaustive sub8");
        check(lt(x,y)==unsigned(a<b),"Exhaustive lt8");check(eq(x,y)==unsigned(a==b),"Exhaustive eq8");
        if(b)check(divu(x,y).value()==a/b,"Exhaustive div8");
    }
    std::mt19937_64 rng(20260911);using W=Word<64>;
    for(unsigned i=0;i<1200;++i){uint64_t a=rng(),b=rng()|1;auto x=W::from(a),y=W::from(b);
        check(add(x,y).value()==a+b,"Add64");check(sub(x,y).value()==a-b,"Sub64");check(lt(x,y)==uint8_t(a<b),"Lt64");
        check(mul(x,y).value()==a*b,"Mul64");check(divu(x,y).value()==a/b,"Div64");}
    const auto asset=gambit::read_asset(argv[1]);
    for(auto fb:{0u,1u}){
        Engine native(asset,fb),gates(asset,fb);gambit::CpuEngine legacy(asset,{fb,-1,-1});
        for(unsigned t=0;t<96;++t){native.tick();gates.tick(true);same(native,gates);legacy.step();
            auto projected=legacy.state;for(auto& c:projected){c.total_input=0;c.total_output=0;}
            gambit::compare_states(native.cells,projected,t);check(native.words==legacy.words,"3.1 packed projection");
            check(native.clock.phase==(legacy.control.step*asset.p.phase_stride)%asset.p.width,"Phase quotient");
            check(native.clock.cooldown==std::min(asset.p.growth_dwell,legacy.control.step-legacy.control.last_growth),"Cooldown quotient");
            auto cap=capsule(native);auto resumed=from_capsule(cap);check(capsule(resumed)==cap,"Canonical capsule round trip");same(native,resumed);
        }
    }
    Engine longrun(asset);for(unsigned t=0;t<10000;++t)longrun.tick();longrun.validate_state();
    check(longrun.clock.phase==(10000u*asset.p.phase_stride)%asset.p.width,"10,000-step phase closure");
    auto resumed=from_capsule(capsule(longrun));for(unsigned t=0;t<40;++t){longrun.tick();resumed.tick();same(longrun,resumed);}
    for(unsigned trial=0;trial<30;++trial){Engine a(asset);
        a.clock={uint32_t(rng()%asset.p.width),uint32_t(asset.p.start_level+rng()%(asset.p.levels-asset.p.start_level)),uint32_t(rng()%(asset.p.growth_dwell+1))};
        for(auto& c:a.cells){c.z=uint32_t(rng()%65537);c.memory=uint32_t(rng()%65537);c.residual=uint32_t(rng()%65536);c.flags=uint32_t(rng()%16);}
        // Redistribution conserves the positive initial total mass.
        for(unsigned k=0;k<64;++k){auto i=rng()%a.cells.size(),j=rng()%a.cells.size();auto amount=a.cells[i].u/3;a.cells[i].u-=amount;a.cells[j].u+=amount;}
        a.pack_words();Engine b=a;a.tick();b.tick(true);same(a,b);
    }
    for(unsigned trial=0;trial<3000;++trial){auto p=asset.p;p.memory_divisor=1+uint32_t(rng()%65536);p.feedback_gain=uint32_t(rng()%16385);
        auto c=Engine(asset).cells[0];c.memory=uint32_t(rng()%65537);auto tex=uint32_t(rng()),q=uint32_t(rng()%2),fb=uint32_t(rng()%2);
        auto a=gambit::make_sample(tex,c,q,p,{fb,-1,-1}),b=gate_sample(tex,c,q,p,fb);
        check(a.field==b.field && a.drive==b.drive,"Signed/clip sample equivalence");
    }
    Engine base(asset),fork(asset);bool different=false;
    for(int t=0;t<40;++t){base.tick();fork.tick(false,t==3?7:-1);if(base.words!=fork.words)different=true;}
    check(different,"Feedback witness did not change output");
    auto valid=capsule(base);for(size_t i=0;i<valid.size();i+=std::max<size_t>(1,valid.size()/71)){auto bad=valid;bad[i]^=1;rejected(bad);}
    auto bad=valid;bad.pop_back();rejected(bad);bad=valid;bad.push_back(0);rejected(bad);
    bad=valid;bad[28]=1;resign(bad);rejected(bad); // reserved field, even with fresh digest
    bad=valid;bad[bad.size()-33]|=128;resign(bad);rejected(bad); // padding
    bad=valid;bad[16]=2;resign(bad);rejected(bad); // feedback encoding
    check((0u+1u>=65536u)==false && (65535u+1u>=65536u)==true,"One-bit quotient counterexample");
    std::cout<<"PASS checks="<<checks<<" exhaustive_pairs_8bit=65536 random_64bit_pairs=1200 continued_ticks=10000\n";return 0;
}catch(const std::exception& e){std::cerr<<"FAIL after "<<checks<<" checks: "<<e.what()<<'\n';return 1;}}
