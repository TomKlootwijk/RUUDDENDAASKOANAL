#pragma once
// Tom Klootwijk Gambit - finite integer CUDA specialization, engineering v3.1.
// Author attribution: Tom Klootwijk, NL200678942, 10-07-1990.
#include <cstdint>
#include <cstddef>
#ifdef __CUDACC__
#define GB_HD __host__ __device__
#else
#define GB_HD
#endif
namespace gambit {
constexpr uint32_t D = 65536u;
constexpr uint32_t PARAM_COUNT = 19u;
struct Params {
    uint32_t width, height, levels, start_level, steps, threshold;
    uint32_t feedback_gain, memory_divisor, phase_stride, feedback_angle;
    uint32_t open_shift, closed_shift, reaction_uv_shift, reaction_vu_shift;
    uint32_t growth_dwell, growth_divisor, seed, pair, device_budget_mib;
};
static_assert(sizeof(Params)==4*PARAM_COUNT, "Unexpected Params layout");
struct Cell {
    uint32_t u, v, z, memory, residual, flags;
    uint64_t total_input, total_output;
};
static_assert(sizeof(Cell)==40, "Cell must have 40-byte layout");
struct Sample { int32_t field; uint32_t drive; };
struct Control { uint32_t step, level, last_growth; };
struct Options { uint32_t feedback; int32_t inject_step, inject_cell; };
struct Report {
    uint64_t mass_u, mass_v, pulses, latches, total_input, total_output;
    uint32_t errors, level_used, level_next, growth;
};
GB_HD inline uint32_t nodes(const Params& p) { return p.width*p.height; }
GB_HD inline uint32_t nwords(const Params& p) { return nodes(p)/32u; }
GB_HD inline uint32_t clamp_d(int64_t x) {
    return x<0 ? 0u : x>int64_t(D) ? D : uint32_t(x);
}
GB_HD inline uint32_t parity32(uint32_t x) {
    x^=x>>16; x^=x>>8; x^=x>>4; x^=x>>2; x^=x>>1; return x&1u;
}
GB_HD inline uint32_t mix32(uint32_t x) {
    // Intentional, defined unsigned arithmetic modulo 2^32; not cryptography.
    x^=x>>16; x*=0x7feb352du; x^=x>>15; x*=0x846ca68bu; return x^(x>>16);
}
GB_HD inline uint32_t latch(uint32_t old_bit, int32_t f, uint32_t threshold) {
    return f<=-int32_t(threshold) ? 1u : f>=int32_t(threshold) ? 0u : old_bit;
}
GB_HD inline uint32_t feedback_bit(uint32_t i, const uint32_t* words,
                                 const Control& c, const Options& o) {
    uint32_t q=(words[i>>5]>>(i&31u))&1u;
    if(o.inject_step>=0 && c.step==uint32_t(o.inject_step) && i==uint32_t(o.inject_cell)) q^=1u;
    return q;
}
GB_HD inline uint32_t lut_index(uint32_t i, const Params& p, const Control& c,
                               uint32_t q, const Options& o) {
    const uint32_t x=i%p.width, y=i/p.width;
    const uint32_t angle=(x+c.step*p.phase_stride+(o.feedback?q*p.feedback_angle:0u))&(p.width-1u);
    return (c.level*p.height+y)*p.width+angle;
}
GB_HD inline Sample make_sample(uint32_t texel, const Cell& cell,
                                uint32_t q, const Params& p, const Options& o) {
    const int32_t d=int32_t(texel&65535u)-32768;
    // C++ signed division truncates toward zero. This rule is part of the model.
    const int32_t m=o.feedback ? (int32_t(cell.memory)-32768)/int32_t(p.memory_divisor) : 0;
    const int32_t pulse=o.feedback ? int32_t(p.feedback_gain)*(2*int32_t(q)-1) : 0;
    return {d-m,clamp_d(int64_t(texel>>16)+16*int64_t(m)+pulse)};
}
GB_HD inline Cell initial_cell(uint32_t i, uint32_t texel, const Params& p) {
    const uint32_t active=uint32_t(int32_t(texel&65535u)-32768<=0);
    const uint32_t h=mix32(i^p.seed^(p.pair*0x9e3779b9u));
    return {(64u+(h&63u))*active,(32u+((h>>6)&31u))*active,
            32768u,32768u,0u,0u,0u,0u};
}
GB_HD inline void add_edge(uint32_t i, uint32_t j, const Cell* old,
                          const Sample* s, const Params& p,
                          uint64_t& out_u, uint64_t& in_u, uint64_t& out_v, uint64_t& in_v) {
    if(s[i].field>0 || s[j].field>0) return;
    const uint32_t b=(old[i].flags|old[j].flags)&1u;
    const uint32_t shift=b?p.open_shift:p.closed_shift;
    out_u+=old[i].u>>shift; in_u+=old[j].u>>shift;
    out_v+=old[i].v>>shift; in_v+=old[j].v>>shift;
}
GB_HD inline Cell advance_cell(uint32_t i, const Cell* old, const Sample* s, const Params& p) {
    uint64_t ou=0,iu=0,ov=0,iv=0;
    const uint32_t x=i%p.width,y=i/p.width;
    add_edge(i,y*p.width+((x+p.width-1u)&(p.width-1u)),old,s,p,ou,iu,ov,iv);
    add_edge(i,y*p.width+((x+1u)&(p.width-1u)),old,s,p,ou,iu,ov,iv);
    if(y) add_edge(i,i-p.width,old,s,p,ou,iu,ov,iv);
    if(y+1u<p.height) add_edge(i,i+p.width,old,s,p,ou,iu,ov,iv);
    const uint64_t u=uint64_t(old[i].u)-ou+iu,v=uint64_t(old[i].v)-ov+iv;
    const uint64_t uv=u>>p.reaction_uv_shift,vu=v>>p.reaction_vu_shift;
    const uint64_t un=u-uv+vu,vn=v-vu+uv;
    // Exact local post-reaction material observation. Product is <= 2^48.
    const uint32_t material=(un+vn) ? uint32_t(uint64_t(D)*un/(un+vn)) : D/2u;
    const uint32_t drive=(3u*s[i].drive+material)/4u;
    const uint32_t z=(3u*old[i].z+drive)/4u;
    const uint32_t m=(15u*old[i].memory+z)/16u;
    const uint32_t a=old[i].residual+z,q=uint32_t(a>=D),r=a-q*D;
    const uint32_t b=latch(old[i].flags&1u,s[i].field,p.threshold);
    const uint32_t event=(old[i].flags&1u)^b,inside=uint32_t(s[i].field<=0);
    return {uint32_t(un),uint32_t(vn),z,m,r,
            b|(q<<1)|(inside<<2)|(event<<3),
            old[i].total_input+z,old[i].total_output+q};
}
GB_HD inline uint32_t cell_errors(const Cell& x) {
    uint32_t e=0;
    if(x.z>D || x.memory>D || x.residual>=D || x.flags>15u) e|=1u;
    if(x.total_output*uint64_t(D)+x.residual!=x.total_input) e|=2u;
    return e;
}
GB_HD inline void finish_control(Control& c, Report& r, const Params& p) {
    r.level_used=c.level; ++c.step; r.growth=0;
    if(c.level+1u<p.levels && c.step-c.last_growth>=p.growth_dwell &&
       r.pulses*uint64_t(p.growth_divisor)>=nodes(p)) {
        ++c.level; c.last_growth=c.step; r.growth=1;
    }
    r.level_next=c.level;
}
} // namespace gambit
