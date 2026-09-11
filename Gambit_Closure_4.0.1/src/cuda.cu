// Tom Klootwijk Gambit 4.0: conditional CUDA realization of the closed transition.
// Revision 4.0.1: CUDA error handling and update diagnostics repaired.
// Native CUDA under NVIDIA's runtime/driver; not driverless bare-metal firmware.
#include "closure/engine.hpp"
#include <cuda_runtime.h>
#include <algorithm>
#include <iostream>
#include <stdexcept>
#include <sstream>
namespace {
inline void check_cuda(cudaError_t result,const char* expression){
    if(result!=cudaSuccess)throw std::runtime_error(std::string(expression)+": "+cudaGetErrorString(result));
}
#define CU(call) check_cuda((call),#call)
using namespace closure;
template<class T>struct Buffer{
    T* p=nullptr;size_t n=0;explicit Buffer(size_t count):n(count){CU(cudaMalloc(reinterpret_cast<void**>(&p),sizeof(T)*n));}
    ~Buffer(){if(p)cudaFree(p);} Buffer(const Buffer&)=delete;Buffer&operator=(const Buffer&)=delete;
};
__device__ uint32_t fetch_lut(uint32_t idx,Params p,cudaTextureObject_t tex,const uint32_t* global){
    return tex?tex2D<unsigned int>(tex,float(idx%p.width)+0.5f,float(idx/p.width)+0.5f):global[idx];
}
__global__ void probe(uint32_t* out,uint32_t count,Params p,cudaTextureObject_t tex,const uint32_t* global){auto i=blockIdx.x*blockDim.x+threadIdx.x;if(i<count)out[i]=fetch_lut(i,p,tex,global);}
__global__ void prepare(const Cell* old,const uint32_t* previous,Sample* samples,Params p,Clock c,uint32_t feedback,cudaTextureObject_t tex,const uint32_t* global){
    auto i=blockIdx.x*blockDim.x+threadIdx.x;if(i>=gambit::nodes(p))return;
    auto q=(previous[i/32]>>(i%32))&1u;
    auto x=(i%p.width+c.phase+(feedback?q*p.feedback_angle:0u))&(p.width-1u);
    auto idx=(c.level*p.height+i/p.width)*p.width+x;
    samples[i]=gambit::make_sample(fetch_lut(idx,p,tex,global),old[i],q,p,{feedback,-1,-1});
}
__global__ void advance(const Cell* old,Cell* next,const Sample* samples,uint32_t* words,Params p){
    auto i=blockIdx.x*blockDim.x+threadIdx.x;auto n=gambit::nodes(p),nw=gambit::nwords(p);Cell c{};
    if(i<n){c=gambit::advance_cell(i,old,samples,p);c.total_input=0;c.total_output=0;next[i]=c;}
    // Every lane in each launched full warp executes every ballot. Padded lanes vote false.
    auto pulse=__ballot_sync(0xffffffffu,i<n && ((c.flags>>1)&1u));
    auto latch=__ballot_sync(0xffffffffu,i<n && (c.flags&1u));
    auto event=__ballot_sync(0xffffffffu,i<n && ((c.flags>>3)&1u));
    auto inside=__ballot_sync(0xffffffffu,i<n && ((c.flags>>2)&1u));
    if((threadIdx.x&31u)==0u && i<n){auto k=i/32;words[k]=pulse;words[nw+k]=latch;words[2*nw+k]=event;words[3*nw+k]=inside;words[4*nw+k]=gambit::parity32(pulse);}
}
struct Session{
    Buffer<Cell> a,b;Buffer<Sample> samples;Buffer<uint32_t> words;
    Buffer<uint32_t>* global=nullptr;cudaArray_t array=nullptr;cudaTextureObject_t tex=0;
    Params p;uint32_t block;bool readback=false;
    Session(const Engine& e,const Arguments& args):a(e.cells.size()),b(e.cells.size()),samples(e.cells.size()),words(e.words.size()),p(e.asset.p),block(args.block){
        try{
            CU(cudaMemcpy(a.p,e.cells.data(),e.cells.size()*sizeof(Cell),cudaMemcpyHostToDevice));
            CU(cudaMemcpy(words.p,e.words.data(),e.words.size()*4,cudaMemcpyHostToDevice));
            if(args.fetch=="texture"){
                auto channel=cudaCreateChannelDesc<unsigned int>();CU(cudaMallocArray(&array,&channel,p.width,p.height*p.levels));
                CU(cudaMemcpy2DToArray(array,0,0,e.asset.texels.data(),p.width*4,p.width*4,p.height*p.levels,cudaMemcpyHostToDevice));
                cudaResourceDesc resource{};resource.resType=cudaResourceTypeArray;resource.res.array.array=array;
                cudaTextureDesc desc{};desc.addressMode[0]=cudaAddressModeClamp;desc.addressMode[1]=cudaAddressModeClamp;
                desc.filterMode=cudaFilterModePoint;desc.readMode=cudaReadModeElementType;desc.normalizedCoords=0;
                CU(cudaCreateTextureObject(&tex,&resource,&desc,nullptr));
            }else{global=new Buffer<uint32_t>(e.asset.texels.size());CU(cudaMemcpy(global->p,e.asset.texels.data(),e.asset.texels.size()*4,cudaMemcpyHostToDevice));}
            Buffer<uint32_t> check(e.asset.texels.size());probe<<<(check.n+255)/256,256>>>(check.p,uint32_t(check.n),p,tex,global?global->p:nullptr);CU(cudaGetLastError());
            std::vector<uint32_t> h(check.n);CU(cudaMemcpy(h.data(),check.p,h.size()*4,cudaMemcpyDeviceToHost));
            if(h!=e.asset.texels)throw std::runtime_error("GPU full-LUT point-read mismatch");readback=true;
        }catch(...){cleanup();throw;}
    }
    void cleanup(){if(tex){cudaDestroyTextureObject(tex);tex=0;}if(array){cudaFreeArray(array);array=nullptr;}delete global;global=nullptr;}
    ~Session(){cleanup();}
    void tick(Engine& e){
        const auto grid=(e.cells.size()+block-1)/block;
        prepare<<<grid,block>>>(a.p,words.p,samples.p,p,e.clock,e.feedback,tex,global?global->p:nullptr);CU(cudaGetLastError());
        advance<<<grid,block>>>(a.p,b.p,samples.p,words.p,p);CU(cudaGetLastError());
        std::vector<Cell> next(e.cells.size());std::vector<uint32_t> packed(e.words.size());
        CU(cudaMemcpy(next.data(),b.p,next.size()*sizeof(Cell),cudaMemcpyDeviceToHost));
        CU(cudaMemcpy(packed.data(),words.p,packed.size()*4,cudaMemcpyDeviceToHost));
        e.accept(std::move(next)); // Host integer control and per-cell invariants; same specified T_sigma.
        if(packed!=e.words)throw std::runtime_error("GPU ballot packing mismatch");std::swap(a.p,b.p);
    }
};
}
int main(int argc,char** argv){try{
    using namespace closure;auto args=parse(argc,argv);cudaDeviceProp d{};CU(cudaGetDeviceProperties(&d,0));CU(cudaSetDevice(0));
    int driver=0,runtime=0;CU(cudaDriverGetVersion(&driver));CU(cudaRuntimeGetVersion(&runtime));size_t free=0,total=0;CU(cudaMemGetInfo(&free,&total));
    if(args.inspect){std::cout<<"{\"device\":"<<gambit::quote_json(d.name)<<",\"compute_major\":"<<d.major<<",\"compute_minor\":"<<d.minor<<",\"driver\":"<<driver<<",\"runtime\":"<<runtime<<",\"total_vram\":"<<total<<",\"free_vram\":"<<free<<"}\n";return 0;}
    if(d.major!=12 || d.minor!=0 || d.warpSize!=32 || args.block>uint32_t(d.maxThreadsPerBlock))throw std::runtime_error("Target requires compute capability 12.0, warp32 and admitted block size");
    if(args.backend!="native")throw std::runtime_error("Boolean ALU backend is a CPU conformance oracle, not a CUDA option");
    auto e=args.resume.empty()?Engine(gambit::read_asset(args.asset),args.feedback):from_capsule(read_bytes(args.resume));
    uint64_t estimate=e.cells.size()*(2*sizeof(Cell)+sizeof(Sample))+e.words.size()*4+e.asset.texels.size()*8;
    if(estimate>uint64_t(e.asset.p.device_budget_mib)*1024*1024 || estimate>uint64_t(free)*3/5)throw std::runtime_error("Estimated working set exceeds memory contract");
    if(e.asset.p.width>uint32_t(d.maxTexture2D[0]) || e.asset.p.height*e.asset.p.levels>uint32_t(d.maxTexture2D[1]))throw std::runtime_error("Texture size outside device limit");
    Engine reference=e;Session session(e,args);uint32_t step=0;
    auto checked=[&](Engine& state){reference.tick();session.tick(state);gambit::compare_states(state.cells,reference.cells,step);
        if(state.words!=reference.words || state.clock.phase!=reference.clock.phase || state.clock.level!=reference.clock.level || state.clock.cooldown!=reference.clock.cooldown)throw std::runtime_error("GPU/native closed-transition mismatch at step "+std::to_string(step));
        ++step;};
    auto extra=std::string(",\"gpu_verified\":true,\"every_step_cpu_comparison\":true,\"full_lut_readback\":true,\"host_control_update\":true,\"device\":")+gambit::quote_json(d.name)+",\"fetch\":"+gambit::quote_json(args.fetch);
    return write_run(e,args,checked,"cuda_checked",extra);
}catch(const std::exception& e){std::cerr<<"FAIL: "<<e.what()<<'\n';return 1;}}
