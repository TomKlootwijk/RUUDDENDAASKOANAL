#include "gambit/host.hpp"
#include <iostream>
#include <stdexcept>
#include <vector>
#include <algorithm>
using namespace gambit;
static uint64_t checks=0;
static void check(bool value,const char* msg){++checks;if(!value)throw std::runtime_error(msg);}
int main(){try {
    for(uint32_t t=1;t<=64;++t)for(int32_t f=-80;f<=80;++f)for(uint32_t b=0;b<2;++b){
        const auto got=latch(b,f,t);check(got<=1,"Latch range");
        check(got==(f<=-int32_t(t)?1u:f>=int32_t(t)?0u:b),"Latch law");}
    for(uint32_t x=0;x<65536;++x){uint32_t p=0;for(uint32_t b=0;b<32;++b)p^=(x>>b)&1u;check(parity32(x)==p,"Parity law");}
    for(uint32_t a=0;a<256;++a)for(uint32_t k=0;k<=256;++k){uint32_t sum=a+k,q=sum>=256,r=sum-256*q;
        check(q<=1 && r<256 && 256*q+r==a+k,"Exhaustive 8-bit accumulator");}
    for(uint32_t r:{0u,1u,32767u,65535u})for(uint32_t k:{0u,1u,32768u,65535u,65536u}){
        const uint32_t q=uint32_t(r+k>=D),rn=r+k-D*q;check(rn<D && D*q+rn==r+k,"D=65536 edge");}
    for(uint32_t u=0;u<65536;++u){check(4u*(u>>3)<=u,"Donor bound");check((u-(u>>6))+(u>>6)==u,"Reaction conservation");}
    for(uint32_t z:{0u,1u,32768u,65535u,D})for(uint32_t k:{0u,1u,32768u,65535u,D})for(uint32_t m:{0u,32768u,D}){
        auto zn=(3*z+k)/4,mn=(15*m+zn)/16;check(zn<=D && mn<=D,"Recurrent bounds");}
    Params p{32,17,3,0,40,49,8192,256,1,3,3,5,6,7,4,4,20260911,1,256};validate(p);
    Asset a{p,std::vector<uint32_t>(nodes(p)*p.levels)};
    for(uint32_t g=0;g<p.levels;++g)for(uint32_t i=0;i<nodes(p);++i){int32_t d=int32_t((i+7*g)%23)-12;
        uint32_t drive=uint32_t(std::max(0,std::min(65535,32768-16*d)));a.texels[g*nodes(p)+i]=uint32_t(d+32768)|(drive<<16);}
    CpuEngine x(a,{1,-1,-1}),replay(a,{1,-1,-1}),open(a,{0,-1,-1}),intervene(a,{1,3,7});
    const auto mass0=sum_mass(x.state);bool differs=false,causal=false;
    for(uint32_t t=0;t<40;++t){x.step();replay.step();open.step();intervene.step();check_report(x.report,mass0);compare_states(x.state,replay.state,t);
        check(x.words==replay.words,"Replay words");differs|=(x.words!=open.words);causal|=(x.state[7].z!=intervene.state[7].z);
        if(t<3)check(x.words==intervene.words,"No anticipatory intervention");
        for(const auto& c:x.state)check(cell_errors(c)==0,"Per-cell exact certificate");}
    check(differs,"Feedback must affect output witness");check(causal,"One-bit intervention must affect self-state witness");
    check(x.control.level==p.levels-1,"Growth feedback exercised");
    for(uint32_t b=0;b<32;++b){uint32_t w=uint32_t(1)<<b;check(((w>>b)&1u)==1,"Packing bit order");}
    auto bad=p;bad.open_shift=1;bool caught=false;try{validate(bad);}catch(...){caught=true;}check(caught,"Reject invalid transport");
    std::cout<<"PASS "<<checks<<" evaluated assertions; integer contract only, no CUDA execution\n";return 0;
}catch(const std::exception& e){std::cerr<<"FAIL: "<<e.what()<<'\n';return 1;}}
