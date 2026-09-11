#include "gambit/host.hpp"
#include <stdexcept>
#include <filesystem>
#include <limits>
#include <sstream>
#include <iostream>
#include <algorithm>
#include <cstdlib>
#include <utility>
namespace gambit {
static void put32(std::ostream& f,uint32_t x) { for(int k=0;k<4;++k) f.put(char((x>>(8*k))&255)); }
static void put64(std::ostream& f,uint64_t x) { put32(f,uint32_t(x)); put32(f,uint32_t(x>>32)); }
static uint32_t get32(std::istream& f) {
    uint32_t x=0; for(int k=0;k<4;++k){int b=f.get(); if(b==EOF) throw std::runtime_error("Truncated asset");x|=uint32_t(b)<<(8*k);}return x;
}
static uint32_t number(const std::string& s) {
    if(s.empty() || s.find_first_not_of("0123456789")!=std::string::npos) throw std::runtime_error("Expected unsigned decimal: "+s);
    size_t n=0;const auto v=std::stoull(s,&n);if(n!=s.size() || v>UINT32_MAX) throw std::runtime_error("Numeric option overflow");return uint32_t(v);
}
void validate(const Params& p) {
    if(p.width<32 || p.width>2048 || (p.width&(p.width-1u)) || p.height<2 || p.height>2048 ||
       p.levels<1 || p.levels>5 || p.start_level>=p.levels || p.steps<1 || p.steps>4096 ||
       p.threshold<1 || p.threshold>32767 || p.feedback_gain>16384 || p.memory_divisor<1 || p.memory_divisor>65536 ||
       p.phase_stride>=p.width || p.feedback_angle>=p.width || p.open_shift<3 || p.open_shift>16 ||
       p.closed_shift<p.open_shift || p.closed_shift>16 || p.reaction_uv_shift<1 || p.reaction_uv_shift>16 ||
       p.reaction_vu_shift<1 || p.reaction_vu_shift>16 || p.growth_dwell<1 || p.growth_dwell>4096 ||
       p.growth_divisor<1 || p.growth_divisor>65536 || p.pair>1 || p.device_budget_mib<16 || p.device_budget_mib>4096)
        throw std::runtime_error("Asset parameters violate finite-kernel contract");
}
Asset read_asset(const std::string& path) {
    std::ifstream f(path,std::ios::binary);if(!f) throw std::runtime_error("Cannot open asset: "+path);
    char magic[8];f.read(magic,8);if(!f || std::string(magic,8)!=std::string("GBLUT31\0",8)) throw std::runtime_error("Bad LUT magic");
    if(get32(f)!=1 || get32(f)!=PARAM_COUNT) throw std::runtime_error("Unsupported LUT format");
    Asset a;uint32_t p[PARAM_COUNT];for(auto& v:p)v=get32(f);
    a.p={p[0],p[1],p[2],p[3],p[4],p[5],p[6],p[7],p[8],p[9],p[10],p[11],p[12],p[13],p[14],p[15],p[16],p[17],p[18]};
    validate(a.p);const size_t count=size_t(nodes(a.p))*a.p.levels;
    const auto expected=uintmax_t(16+PARAM_COUNT*4)+uintmax_t(count)*4;
    if(std::filesystem::file_size(path)!=expected) throw std::runtime_error("LUT length does not match validated dimensions");
    a.texels.resize(count);for(auto& v:a.texels)v=get32(f);return a;
}
RunArgs parse_args(int argc,char** argv) {
    RunArgs a;
    for(int i=1;i<argc;++i){std::string k=argv[i];
        if(k=="--verify"){a.verify=true;continue;}
        if(k=="--inspect"){a.inspect=true;continue;}
        if(k=="--help") {std::cout<<"--asset FILE --out DIR [--steps N] [--block 32|64|128|256|512] [--fetch texture|global] [--feedback 0|1] [--inject-step N --inject-cell N] [--device N] [--verify] [--inspect]\n";std::exit(0);}
        if(i+1>=argc)throw std::runtime_error("Missing argument for "+k);
        std::string v=argv[++i];
        if(k=="--asset")a.asset=v;else if(k=="--out")a.out=v;else if(k=="--fetch")a.fetch=v;
        else if(k=="--steps"){a.steps=number(v);if(!a.steps)throw std::runtime_error("steps must be positive");}else if(k=="--block")a.block=number(v);else if(k=="--device")a.device=number(v);
        else if(k=="--feedback")a.options.feedback=number(v);
        else if(k=="--inject-step"){auto n=number(v);if(n>4095)throw std::runtime_error("Injection step too large");a.options.inject_step=int32_t(n);}
        else if(k=="--inject-cell"){auto n=number(v);if(n>4194303)throw std::runtime_error("Injection cell too large");a.options.inject_cell=int32_t(n);}
        else throw std::runtime_error("Unknown option: "+k);
    }
    if(!a.inspect && a.asset.empty())throw std::runtime_error("--asset is required");
    if(a.steps>4096 || a.options.feedback>1 || (a.fetch!="texture" && a.fetch!="global") ||
       a.block<32 || a.block>512 || (a.block&(a.block-1u)) ||
       ((a.options.inject_cell<0)!=(a.options.inject_step<0)))throw std::runtime_error("Invalid execution option");
    return a;
}
std::vector<Cell> initialize(const Asset& a) {
    std::vector<Cell> v(nodes(a.p));for(uint32_t i=0;i<v.size();++i)v[i]=initial_cell(i,a.texels[size_t(a.p.start_level)*v.size()+i],a.p);
    auto mass=sum_mass(v);if(!mass || mass>UINT32_MAX)throw std::runtime_error("Initial total mass must be in 1..2^32-1");return v;
}
uint64_t sum_mass(const std::vector<Cell>& s){uint64_t m=0;for(const auto& c:s)m+=uint64_t(c.u)+c.v;return m;}
CpuEngine::CpuEngine(Asset asset,Options opts):a(std::move(asset)),options(opts),control{0,a.p.start_level,0},state(initialize(a)),next(state.size()),samples(state.size()),words(5*nwords(a.p),0u) {
    if(options.inject_cell>=int32_t(nodes(a.p)))throw std::runtime_error("Injection cell out of bounds");
}
void CpuEngine::step() {
    const Params& p=a.p;const auto n=nodes(p),nw=nwords(p);
    for(uint32_t i=0;i<n;++i){auto q=feedback_bit(i,words.data(),control,options);samples[i]=make_sample(a.texels[lut_index(i,p,control,q,options)],state[i],q,p,options);}
    std::fill(words.begin(),words.end(),0u);report={};
    for(uint32_t i=0;i<n;++i){const Cell v=advance_cell(i,state.data(),samples.data(),p);next[i]=v;
        auto w=i>>5,b=i&31u;words[w]|=((v.flags>>1)&1u)<<b;words[nw+w]|=(v.flags&1u)<<b;
        words[2*nw+w]|=((v.flags>>3)&1u)<<b;words[3*nw+w]|=((v.flags>>2)&1u)<<b;
        report.mass_u+=v.u;report.mass_v+=v.v;report.pulses+=(v.flags>>1)&1u;report.latches+=v.flags&1u;
        report.total_input+=v.total_input;report.total_output+=v.total_output;report.errors|=cell_errors(v);
    }
    for(uint32_t w=0;w<nw;++w)words[4*nw+w]=parity32(words[w]);
    state.swap(next);finish_control(control,report,p);
}
Writer::Writer(const std::string& path,const Params& p,uint32_t steps):dir(path) {
    std::filesystem::create_directories(path);
    for(const char* name:{"words.bin","state.bin","summary.csv","run.json"})
        if(std::filesystem::exists(std::filesystem::path(path)/name))throw std::runtime_error("Output directory contains prior artifacts; select a new --out directory");
    words_file.open(path+"/words.bin",std::ios::binary);summary_file.open(path+"/summary.csv",std::ios::binary);
    if(!words_file || !summary_file)throw std::runtime_error("Cannot create output files");
    words_file.write("GBWORD31",8);for(uint32_t x:{p.width,p.height,steps,5u,nwords(p)})put32(words_file,x);
    summary_file<<"step,level_used,level_next,growth,pulses,latches,mass_u,mass_v,total_input,total_output,errors\n";
}
void Writer::frame(uint32_t step,const Report& r,const std::vector<uint32_t>& words) {
    for(auto x:words)put32(words_file,x);
    summary_file<<step<<','<<r.level_used<<','<<r.level_next<<','<<r.growth<<','<<r.pulses<<','<<r.latches<<','<<r.mass_u<<','<<r.mass_v<<','<<r.total_input<<','<<r.total_output<<','<<r.errors<<'\n';
    if(!words_file || !summary_file)throw std::runtime_error("Trace output failed");
}
void Writer::final_state(const std::vector<Cell>& s,const Control& c) {
    std::ofstream f(dir+"/state.bin",std::ios::binary);f.write("GBSTAT31",8);put32(f,uint32_t(s.size()));
    for(const auto& x:s){for(uint32_t v:{x.u,x.v,x.z,x.memory,x.residual,x.flags})put32(f,v);put64(f,x.total_input);put64(f,x.total_output);}
    put32(f,c.step);put32(f,c.level);put32(f,c.last_growth);
    f.close();words_file.close();summary_file.close();
    if(!f || !words_file || !summary_file)throw std::runtime_error("Final trace/state flush failed");
}
void check_report(const Report& r,uint64_t mass0) {
    if(r.errors || r.mass_u+r.mass_v!=mass0)throw std::runtime_error("Invariant certificate failed");
}
void compare_states(const std::vector<Cell>& a,const std::vector<Cell>& b,uint32_t step) {
    if(a.size()!=b.size())throw std::runtime_error("State size mismatch");
    for(size_t i=0;i<a.size();++i){const auto& x=a[i];const auto& y=b[i];
        if(x.u!=y.u || x.v!=y.v || x.z!=y.z || x.memory!=y.memory || x.residual!=y.residual || x.flags!=y.flags || x.total_input!=y.total_input || x.total_output!=y.total_output)
            throw std::runtime_error("CPU/GPU state mismatch at step "+std::to_string(step)+", cell "+std::to_string(i));}
}
std::string quote_json(const std::string& s) {
    std::ostringstream o;o<<'"';for(unsigned char c:s){if(c=='"'||c=='\\')o<<'\\'<<char(c);else if(c<32)o<<'?';else o<<char(c);}o<<'"';return o.str();
}
void write_run_json(const std::string& dir,const std::string& json) {std::ofstream f(dir+"/run.json");f<<json<<'\n';f.close();if(!f)throw std::runtime_error("Cannot write run metadata");}
} // namespace
