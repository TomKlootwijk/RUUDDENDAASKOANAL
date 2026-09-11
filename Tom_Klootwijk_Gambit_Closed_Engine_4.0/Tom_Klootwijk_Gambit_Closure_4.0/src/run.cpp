#include "closure/engine.hpp"
#include <filesystem>
#include <iostream>
#include <stdexcept>
#include <sstream>
namespace closure {
static uint32_t num(const std::string& s){
    if(s.empty() || s.find_first_not_of("0123456789")!=std::string::npos)throw std::runtime_error("Unsigned decimal required");
    auto n=std::stoull(s);if(n>UINT32_MAX)throw std::runtime_error("Option overflow");return uint32_t(n);
}
Arguments parse(int argc,char** argv){
    Arguments a;for(int i=1;i<argc;++i){std::string k=argv[i];
        if(k=="--inspect"){a.inspect=true;continue;}
        if(k=="--help"){std::cout<<"(--asset FILE | --resume CAPSULE) --out NEW_DIR [--steps 1..4096] [--backend native|gates] [--feedback 0|1 (new seeds only)] [GPU: --fetch texture|global --block 32|64|128|256|512] [--inspect]\n";std::exit(0);}
        if(i+1==argc)throw std::runtime_error("Missing value for "+k);
        std::string v=argv[++i];
        if(k=="--asset")a.asset=v;else if(k=="--resume")a.resume=v;else if(k=="--out")a.out=v;
        else if(k=="--steps")a.steps=num(v);else if(k=="--backend")a.backend=v;
        else if(k=="--feedback"){a.feedback=num(v);a.feedback_set=true;}else if(k=="--fetch")a.fetch=v;else if(k=="--block")a.block=num(v);
        else throw std::runtime_error("Unknown option: "+k);
    }
    if(a.inspect)return a;
    if((a.asset.empty()==a.resume.empty()) || a.out.empty() || !a.steps || a.steps>4096 || a.feedback>1 ||
       (a.backend!="native" && a.backend!="gates") || (!a.resume.empty() && a.feedback_set) ||
       (a.fetch!="texture" && a.fetch!="global") || a.block<32 || a.block>512 || (a.block&(a.block-1)))
       throw std::runtime_error("Invalid run arguments; use --help");
    return a;
}
static void put32(std::ostream& f,uint32_t v){for(int j=0;j<4;++j)f.put(char((v>>(8*j))&255));}
static void put64(std::ostream& f,uint64_t v){put32(f,uint32_t(v));put32(f,uint32_t(v>>32));}
int write_run(Engine& e,const Arguments& a,const Advance& advance,const std::string& backend,const std::string& extra){
    namespace fs=std::filesystem;
    if(fs::exists(a.out))throw std::runtime_error("Output path already exists; an unused directory is required");
    fs::create_directories(a.out);write_bytes(a.out+"/initial.gbc",capsule(e));
    std::vector<uint64_t> k(e.cells.size()),q(e.cells.size());std::vector<uint32_t> r0;for(auto c:e.cells)r0.push_back(c.residual);
    std::ofstream words(a.out+"/words.bin",std::ios::binary),summary(a.out+"/summary.csv",std::ios::binary);
    if(!words || !summary)throw std::runtime_error("Output open failed");
    words.write("GBWORD40",8);for(auto v:{e.asset.p.width,e.asset.p.height,a.steps,5u,uint32_t(e.cells.size()/32)})put32(words,v);
    summary<<"tick,phase,level,cooldown,pulses,latches,mass_u,mass_v,input_sum,pulse_sum\n";
    for(uint32_t t=0;t<a.steps;++t){advance(e);uint64_t pulses=0,latches=0,mu=0,mv=0,sk=0,sq=0;
        for(size_t i=0;i<e.cells.size();++i){auto c=e.cells[i];auto bit=(c.flags>>1)&1u;k[i]+=c.z;q[i]+=bit;
            if(uint64_t(gambit::D)*q[i]+c.residual!=uint64_t(r0[i])+k[i])throw std::runtime_error("Prefix count certificate failed");
            pulses+=bit;latches+=c.flags&1;mu+=c.u;mv+=c.v;sk+=k[i];sq+=q[i];}
        for(auto w:e.words)put32(words,w);
        summary<<t<<','<<e.clock.phase<<','<<e.clock.level<<','<<e.clock.cooldown<<','<<pulses<<','<<latches<<','<<mu<<','<<mv<<','<<sk<<','<<sq<<'\n';
    }
    words.flush();summary.flush();if(!words || !summary)throw std::runtime_error("Trace write failed");
    write_bytes(a.out+"/final.gbc",capsule(e));
    std::ofstream counts(a.out+"/counts.bin",std::ios::binary);counts.write("GBCOUNT4",8);put32(counts,uint32_t(e.cells.size()));
    for(size_t i=0;i<e.cells.size();++i){put32(counts,r0[i]);put64(counts,k[i]);put64(counts,q[i]);}
    counts.flush();if(!counts)throw std::runtime_error("Count write failed");
    std::ofstream meta(a.out+"/run.json");meta<<"{\"schema\":\"gambit-closure-4.0\",\"backend\":"<<gambit::quote_json(backend)
       <<",\"status\":\"PASS\",\"steps_in_segment\":"<<a.steps<<",\"autonomous_transition\":true,\"physical_actuators\":false"
       <<(extra.empty()?",\"gpu_verified\":false":extra)<<"}\n";
    if(!meta)throw std::runtime_error("Metadata write failed");
    std::cout<<"PASS backend="<<backend<<" cells="<<e.cells.size()<<" segment="<<a.steps<<" phase="<<e.clock.phase<<" level="<<e.clock.level<<" mass="<<e.mass0<<'\n';return 0;
}
} // namespace closure
