#include "closure/engine.hpp"
#include <algorithm>
#include <stdexcept>
#include <utility>
namespace closure {
Engine::Engine(Asset a,uint32_t enabled):asset(std::move(a)),feedback(enabled) {
    gambit::validate(asset.p);
    if(feedback>1) throw std::runtime_error("Feedback must be 0 or 1");
    if(asset.texels.size()!=size_t(gambit::nodes(asset.p))*asset.p.levels)throw std::runtime_error("LUT size mismatch");
    cells=gambit::initialize(asset); scratch.resize(cells.size()); samples.resize(cells.size());
    mass0=gambit::sum_mass(cells); clock={0,asset.p.start_level,0}; pack_words(); validate_state();
}
void Engine::validate_state() const {
    const auto& p=asset.p;
    if(feedback>1 || cells.size()!=gambit::nodes(p) || clock.phase>=p.width ||
       clock.level<p.start_level || clock.level>=p.levels || clock.cooldown>p.growth_dwell)
        throw std::runtime_error("Invalid operational control/state dimensions");
    uint64_t mass=0;
    for(const auto& c:cells){
        if(c.z>gambit::D || c.memory>gambit::D || c.residual>=gambit::D || c.flags>15 ||
           c.total_input!=0 || c.total_output!=0)throw std::runtime_error("Invalid operational cell (audit counters must be zero)");
        mass+=uint64_t(c.u)+c.v;
    }
    if(!mass0 || mass0>UINT32_MAX || mass!=mass0)throw std::runtime_error("Mass invariant failed");
}
void Engine::pack_words() {
    const uint32_t nw=uint32_t(cells.size()/32); words.assign(5*nw,0);
    for(uint32_t i=0;i<cells.size();++i){const auto f=cells[i].flags;auto k=i/32,b=i%32;
        words[k]|=((f>>1)&1)<<b; words[nw+k]|=(f&1)<<b;
        words[2*nw+k]|=((f>>3)&1)<<b; words[3*nw+k]|=((f>>2)&1)<<b;
    }
    for(uint32_t k=0;k<nw;++k) words[4*nw+k]=gambit::parity32(words[k]);
}
void Engine::accept(std::vector<Cell> next,bool gates) {
    if(next.size()!=cells.size())throw std::runtime_error("Next-state length mismatch");
    uint64_t pulses=0;
    for(size_t i=0;i<cells.size();++i){auto& c=next[i]; const auto q=(c.flags>>1)&1u;
        if(uint64_t(gambit::D)*q+c.residual!=uint64_t(cells[i].residual)+c.z)
            throw std::runtime_error("Local pulse certificate failed");
        pulses+=q;c.total_input=0;c.total_output=0;
    }
    if(gates)clock=gate_clock(clock,gate_count(next),asset.p);
    else {
        clock.phase=(clock.phase+asset.p.phase_stride)&(asset.p.width-1u);
        clock.cooldown=std::min(clock.cooldown+1u,asset.p.growth_dwell);
        if(clock.level+1u<asset.p.levels && clock.cooldown==asset.p.growth_dwell &&
           pulses*asset.p.growth_divisor>=cells.size()){++clock.level;clock.cooldown=0;}
    }
    cells.swap(next);validate_state();pack_words();
}
void Engine::tick(bool gates,int32_t inject_read) {
    const auto& p=asset.p;const auto n=gambit::nodes(p);
    if(inject_read<-1 || inject_read>=int32_t(n))throw std::runtime_error("Intervention cell out of range");
    for(uint32_t i=0;i<n;++i){
        uint32_t q=(words[i/32]>>(i%32))&1u; if(int32_t(i)==inject_read)q^=1u;
        const auto x=gates?gate_angle(i%p.width,clock,q,p,feedback):
          ((i%p.width+clock.phase+(feedback?q*p.feedback_angle:0u))&(p.width-1u));
        const auto tex=asset.texels[(clock.level*p.height+i/p.width)*p.width+x];
        samples[i]=gates?gate_sample(tex,cells[i],q,p,feedback):gambit::make_sample(tex,cells[i],q,p,{feedback,-1,-1});
    }
    for(uint32_t i=0;i<n;++i)scratch[i]=gates?gate_cell(i,cells,samples,p):gambit::advance_cell(i,cells.data(),samples.data(),p);
    accept(scratch,gates);
}
} // namespace closure
