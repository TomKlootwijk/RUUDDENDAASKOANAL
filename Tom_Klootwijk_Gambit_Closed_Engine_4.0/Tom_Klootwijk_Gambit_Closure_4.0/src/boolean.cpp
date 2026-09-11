#include "closure/engine.hpp"
#include "closure/boolean.hpp"
namespace closure {
using namespace bits;
using W=Word<64>;using S=Word<32>;
static S signed_word(int32_t n){return S::from(uint32_t(n));}
static int32_t signed_value(const S& v){const uint64_t n=v.value();return int32_t(int64_t(n&0x7fffffffULL)-(v.b[31]?int64_t(0x80000000ULL):0));}
Sample gate_sample(uint32_t texel,const Cell& cell,uint32_t q,const Params& p,uint32_t feedback){
    const auto d=sub(S::from(texel&65535),S::from(32768));
    auto m=div_signed_positive(sub(S::from(cell.memory),S::from(32768)),S::from(p.memory_divisor));
    m=mux(Bit(feedback),m,S{});
    const auto pulse=mux(Bit(feedback),mux(Bit(q),S::from(p.feedback_gain),neg(S::from(p.feedback_gain))),S{});
    auto a=add(add(S::from(texel>>16),shl(m,4)),pulse);
    a=mux(a.b[31],S{},mux(lt(S::from(gambit::D),a),S::from(gambit::D),a));
    return {signed_value(sub(d,m)),uint32_t(a.value())};
}
uint32_t gate_angle(uint32_t x,Clock c,uint32_t q,const Params& p,uint32_t feedback){
    auto a=add(add(S::from(x),S::from(c.phase)),mux(And(Bit(q),Bit(feedback)),S::from(p.feedback_angle),S{}));
    const auto mask=S::from(p.width-1);for(size_t i=0;i<32;++i)a.b[i]=And(a.b[i],mask.b[i]);return uint32_t(a.value());
}
Cell gate_cell(uint32_t i,const std::vector<Cell>& old,const std::vector<Sample>& s,const Params& p){
    W ou,iu,ov,iv; const uint32_t x=i%p.width,y=i/p.width;
    std::array<uint32_t,4> neighbors{{y*p.width+(x+p.width-1)%p.width,y*p.width+(x+1)%p.width,i,i}};
    size_t count=2;if(y)neighbors[count++]=i-p.width;if(y+1<p.height)neighbors[count++]=i+p.width;
    for(size_t a=0;a<count;++a){auto j=neighbors[a];
        const auto active=And(Not(signed_lt(S{},signed_word(s[i].field))),Not(signed_lt(S{},signed_word(s[j].field))));
        const auto b=Bit((old[i].flags|old[j].flags)&1u);
        auto flux=[&](uint32_t v){auto w=W::from(v);return mux(active,mux(b,shr(w,p.open_shift),shr(w,p.closed_shift)),W{});};
        ou=add(ou,flux(old[i].u));iu=add(iu,flux(old[j].u));ov=add(ov,flux(old[i].v));iv=add(iv,flux(old[j].v));
    }
    auto u=add(sub(W::from(old[i].u),ou),iu),v=add(sub(W::from(old[i].v),ov),iv);
    auto uv=shr(u,p.reaction_uv_shift),vu=shr(v,p.reaction_vu_shift);
    auto un=add(sub(u,uv),vu),vn=add(sub(v,vu),uv);auto total=add(un,vn);
    const auto nonzero=Not(eq(total,W{}));
    auto material=divu(shl(un,16),mux(nonzero,total,W::from(1)));
    material=mux(nonzero,material,W::from(32768));
    auto field=W::from(s[i].drive);auto drive=shr(add(add(shl(field,1),field),material),2);
    auto oldz=W::from(old[i].z);auto z=shr(add(add(shl(oldz,1),oldz),drive),2);
    auto om=W::from(old[i].memory);auto m=shr(add(sub(shl(om,4),om),z),4);
    auto sum=add(W::from(old[i].residual),z);auto q=Not(lt(sum,W::from(gambit::D)));
    auto r=sub(sum,mux(q,W::from(gambit::D),W{}));
    auto field_s=signed_word(s[i].field),threshold=S::from(p.threshold);
    auto inside=Not(signed_lt(S{},field_s));
    auto set=Not(signed_lt(neg(threshold),field_s));auto clear=Not(signed_lt(field_s,threshold));
    auto b=select(set,1,select(clear,0,Bit(old[i].flags&1u)));
    auto event=Xor(Bit(old[i].flags&1u),b);
    return {uint32_t(un.value()),uint32_t(vn.value()),uint32_t(z.value()),uint32_t(m.value()),uint32_t(r.value()),
            uint32_t(b)|(uint32_t(q)<<1)|(uint32_t(inside)<<2)|(uint32_t(event)<<3),0,0};
}
uint64_t gate_count(const std::vector<Cell>& cells){
    W count;for(const auto& c:cells)count=add(count,W::from((c.flags>>1)&1u));return count.value();
}
Clock gate_clock(Clock old,uint64_t pulses,const Params& p){
    auto phase=add(S::from(old.phase),S::from(p.phase_stride));auto mask=S::from(p.width-1);
    for(size_t i=0;i<32;++i)phase.b[i]=And(phase.b[i],mask.b[i]);
    auto cd=add(S::from(old.cooldown),S::from(1));auto dwell=S::from(p.growth_dwell);
    cd=mux(lt(dwell,cd),dwell,cd);
    auto next_level=add(S::from(old.level),S::from(1));
    auto grow=And(And(lt(next_level,S::from(p.levels)),eq(cd,dwell)),
                  Not(lt(mul(W::from(pulses),W::from(p.growth_divisor)),W::from(gambit::nodes(p)))));
    return {uint32_t(phase.value()),uint32_t(mux(grow,next_level,S::from(old.level)).value()),uint32_t(mux(grow,S{},cd).value())};
}
} // namespace closure
