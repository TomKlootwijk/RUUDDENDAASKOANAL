#include "closure/engine.hpp"
#include <algorithm>
#include <filesystem>
#include <iomanip>
#include <sstream>
#include <stdexcept>
#include <cstring>
namespace closure {
// Direct implementation of the SHA-256 algorithm specified in FIPS 180-4.
// Integrity against an expected digest, not a signature or proof of provenance.
static uint32_t rotr(uint32_t x,unsigned n){return (x>>n)|(x<<(32-n));}
std::array<uint8_t,32> sha256(const std::vector<uint8_t>& data){
    static const uint32_t k[64]={
        0x428a2f98,0x71374491,0xb5c0fbcf,0xe9b5dba5,0x3956c25b,0x59f111f1,0x923f82a4,0xab1c5ed5,
        0xd807aa98,0x12835b01,0x243185be,0x550c7dc3,0x72be5d74,0x80deb1fe,0x9bdc06a7,0xc19bf174,
        0xe49b69c1,0xefbe4786,0x0fc19dc6,0x240ca1cc,0x2de92c6f,0x4a7484aa,0x5cb0a9dc,0x76f988da,
        0x983e5152,0xa831c66d,0xb00327c8,0xbf597fc7,0xc6e00bf3,0xd5a79147,0x06ca6351,0x14292967,
        0x27b70a85,0x2e1b2138,0x4d2c6dfc,0x53380d13,0x650a7354,0x766a0abb,0x81c2c92e,0x92722c85,
        0xa2bfe8a1,0xa81a664b,0xc24b8b70,0xc76c51a3,0xd192e819,0xd6990624,0xf40e3585,0x106aa070,
        0x19a4c116,0x1e376c08,0x2748774c,0x34b0bcb5,0x391c0cb3,0x4ed8aa4a,0x5b9cca4f,0x682e6ff3,
        0x748f82ee,0x78a5636f,0x84c87814,0x8cc70208,0x90befffa,0xa4506ceb,0xbef9a3f7,0xc67178f2};
    uint32_t h[8]={0x6a09e667,0xbb67ae85,0x3c6ef372,0xa54ff53a,0x510e527f,0x9b05688c,0x1f83d9ab,0x5be0cd19};
    auto msg=data;const uint64_t bits=uint64_t(data.size())*8;msg.push_back(0x80);
    while(msg.size()%64!=56)msg.push_back(0);
    for(int i=7;i>=0;--i)msg.push_back(uint8_t(bits>>(8*i)));
    for(size_t pos=0;pos<msg.size();pos+=64){uint32_t w[64];
        for(size_t t=0;t<16;++t){w[t]=0;for(int j=0;j<4;++j)w[t]=(w[t]<<8)|msg[pos+4*t+j];}
        for(size_t t=16;t<64;++t){auto s0=rotr(w[t-15],7)^rotr(w[t-15],18)^(w[t-15]>>3);auto s1=rotr(w[t-2],17)^rotr(w[t-2],19)^(w[t-2]>>10);w[t]=w[t-16]+s0+w[t-7]+s1;}
        uint32_t a=h[0],b=h[1],c=h[2],d=h[3],e=h[4],f=h[5],g=h[6],z=h[7];
        for(size_t t=0;t<64;++t){auto s1=rotr(e,6)^rotr(e,11)^rotr(e,25);auto ch=(e&f)^((~e)&g);auto t1=z+s1+ch+k[t]+w[t];auto s0=rotr(a,2)^rotr(a,13)^rotr(a,22);auto maj=(a&b)^(a&c)^(b&c);auto t2=s0+maj;
            z=g;g=f;f=e;e=d+t1;d=c;c=b;b=a;a=t1+t2;}
        h[0]+=a;h[1]+=b;h[2]+=c;h[3]+=d;h[4]+=e;h[5]+=f;h[6]+=g;h[7]+=z;
    }
    std::array<uint8_t,32> out{};for(size_t i=0;i<8;++i)for(size_t j=0;j<4;++j)out[i*4+j]=uint8_t(h[i]>>(24-8*j));return out;
}
std::string hex_digest(const std::vector<uint8_t>& data){auto h=sha256(data);std::ostringstream o;for(auto c:h)o<<std::hex<<std::setw(2)<<std::setfill('0')<<unsigned(c);return o.str();}
static void put(std::vector<uint8_t>& b,uint32_t n){for(unsigned j=0;j<4;++j)b.push_back(uint8_t(n>>(8*j)));}
static uint32_t get(const std::vector<uint8_t>& b,size_t& p){if(p+4>b.size())throw std::runtime_error("Truncated integer");uint32_t n=0;for(unsigned j=0;j<4;++j)n|=uint32_t(b[p++])<<(8*j);return n;}
static std::vector<uint8_t> asset_bytes(const Asset& a){
    std::vector<uint8_t> b={'G','B','L','U','T','3','1',0};put(b,1);put(b,gambit::PARAM_COUNT);
    const auto& p=a.p;const uint32_t params[]={p.width,p.height,p.levels,p.start_level,p.steps,p.threshold,p.feedback_gain,p.memory_divisor,p.phase_stride,p.feedback_angle,p.open_shift,p.closed_shift,p.reaction_uv_shift,p.reaction_vu_shift,p.growth_dwell,p.growth_divisor,p.seed,p.pair,p.device_budget_mib};
    for(auto x:params)put(b,x);
    for(auto x:a.texels)put(b,x);
    return b;
}
struct BitWriter{
    std::vector<uint8_t> bytes;size_t pos=0;
    void put(uint64_t v,unsigned width){if(width<64 && v>=(uint64_t(1)<<width))throw std::runtime_error("Bit field overflow");for(unsigned j=0;j<width;++j){if(pos%8==0)bytes.push_back(0);bytes[pos/8]|=uint8_t(((v>>j)&1)<<(pos%8));++pos;}}
};
struct BitReader{
    const std::vector<uint8_t>& b;size_t base,pos=0;
    uint32_t get(unsigned width){uint32_t v=0;for(unsigned j=0;j<width;++j){if(base+pos/8>=b.size())throw std::runtime_error("Truncated bits");v|=uint32_t((b[base+pos/8]>>(pos%8))&1)<<j;++pos;}return v;}
};
std::vector<uint8_t> capsule(const Engine& e){
    e.validate_state();const auto a=asset_bytes(e.asset);BitWriter s;
    s.put(e.clock.phase,11);s.put(e.clock.level,3);s.put(e.clock.cooldown,13);
    for(const auto& c:e.cells){s.put(c.u,32);s.put(c.v,32);s.put(c.z,17);s.put(c.memory,17);s.put(c.residual,16);s.put(c.flags,4);}
    std::vector<uint8_t> out={'G','B','C','L','O','S','4','0'};
    put(out,1);put(out,uint32_t(a.size()));put(out,e.feedback);put(out,uint32_t(e.mass0));put(out,uint32_t(s.pos));put(out,0);
    out.insert(out.end(),a.begin(),a.end());out.insert(out.end(),s.bytes.begin(),s.bytes.end());auto h=sha256(out);out.insert(out.end(),h.begin(),h.end());return out;
}
Engine from_capsule(const std::vector<uint8_t>& b){
    if(b.size()<160 || b.size()>256u*1024u*1024u)throw std::runtime_error("Capsule size outside contract");
    auto pre=std::vector<uint8_t>(b.begin(),b.end()-32);auto h=sha256(pre);
    if(!std::equal(h.begin(),h.end(),b.end()-32))throw std::runtime_error("Capsule SHA-256 mismatch");
    if(std::string(b.begin(),b.begin()+8)!="GBCLOS40")throw std::runtime_error("Capsule magic mismatch");
    size_t at=8;auto version=get(b,at),asz=get(b,at),feedback=get(b,at),mass=get(b,at),nbits=get(b,at),reserved=get(b,at);
    if(version!=1 || reserved || feedback>1 || asz<92 || uint64_t(32)+asz+(uint64_t(nbits)+7)/8+32!=b.size())throw std::runtime_error("Capsule header mismatch");
    if(std::string(b.begin()+at,b.begin()+at+8)!=std::string("GBLUT31\0",8))throw std::runtime_error("Embedded asset magic mismatch");
    at+=8;
    if(get(b,at)!=1 || get(b,at)!=19)throw std::runtime_error("Embedded asset format mismatch");
    uint32_t p[19];for(auto& n:p)n=get(b,at);Asset a;a.p={p[0],p[1],p[2],p[3],p[4],p[5],p[6],p[7],p[8],p[9],p[10],p[11],p[12],p[13],p[14],p[15],p[16],p[17],p[18]};
    gambit::validate(a.p);auto n=gambit::nodes(a.p);
    if(asz!=92u+4u*n*a.p.levels || nbits!=27u+118u*n)throw std::runtime_error("Capsule payload dimensions mismatch");
    a.texels.resize(size_t(n)*a.p.levels);for(auto& v:a.texels)v=get(b,at);
    Engine e(std::move(a),feedback);if(mass!=e.mass0)throw std::runtime_error("Initial mass descriptor mismatch");BitReader r{b,at};
    e.clock={r.get(11),r.get(3),r.get(13)};
    for(auto& c:e.cells)c={r.get(32),r.get(32),r.get(17),r.get(17),r.get(16),r.get(4),0,0};
    if((b[b.size()-33]>>(nbits%8))!=0)throw std::runtime_error("Noncanonical bit padding");
    e.validate_state();e.pack_words();return e;
}
std::vector<uint8_t> read_bytes(const std::string& path){
    auto n=std::filesystem::file_size(path);if(n>256u*1024u*1024u)throw std::runtime_error("Input file exceeds 256 MiB");
    std::ifstream f(path,std::ios::binary);if(!f)throw std::runtime_error("Cannot open input");std::vector<uint8_t>b(size_t(n),0);if(!f.read(reinterpret_cast<char*>(b.data()),std::streamsize(n)))throw std::runtime_error("Short file read");return b;
}
void write_bytes(const std::string& path,const std::vector<uint8_t>& b){std::ofstream f(path,std::ios::binary);if(!f || !f.write(reinterpret_cast<const char*>(b.data()),std::streamsize(b.size())))throw std::runtime_error("File write failed");}
} // namespace closure
