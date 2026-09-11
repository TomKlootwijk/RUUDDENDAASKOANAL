// Native CUDA implementation. No Python, neural runtime, floating reduction, or atomics.
#include <cuda_runtime.h>
#include "gambit/host.hpp"
#include <iostream>
#include <sstream>
#include <stdexcept>
#include <chrono>
#include <algorithm>
using namespace gambit;
static void cuda_check(cudaError_t e,const char* what) {
    if(e!=cudaSuccess)throw std::runtime_error(std::string(what)+": "+cudaGetErrorString(e));
}
#define CUDA_OK(x) cuda_check((x),#x)
template<class T> struct DeviceBuffer {
    T* data=nullptr;
    explicit DeviceBuffer(size_t n){CUDA_OK(cudaMalloc(reinterpret_cast<void**>(&data),n*sizeof(T)));}
    ~DeviceBuffer(){if(data)cudaFree(data);}
    DeviceBuffer(const DeviceBuffer&)=delete; DeviceBuffer& operator=(const DeviceBuffer&)=delete;
};
struct Texture {
    cudaArray_t array=nullptr; cudaTextureObject_t object=0;
    Texture(const Asset& a){
        try {
            const cudaChannelFormatDesc channel=cudaCreateChannelDesc<unsigned int>();
            CUDA_OK(cudaMallocArray(&array,&channel,a.p.width,a.p.height*a.p.levels));
            const size_t pitch=size_t(a.p.width)*sizeof(uint32_t);
            CUDA_OK(cudaMemcpy2DToArray(array,0,0,a.texels.data(),pitch,pitch,a.p.height*a.p.levels,cudaMemcpyHostToDevice));
            cudaResourceDesc r{};r.resType=cudaResourceTypeArray;r.res.array.array=array;
            cudaTextureDesc t{};t.addressMode[0]=cudaAddressModeClamp;t.addressMode[1]=cudaAddressModeClamp;
            t.filterMode=cudaFilterModePoint;t.readMode=cudaReadModeElementType;t.normalizedCoords=0;
            CUDA_OK(cudaCreateTextureObject(&object,&r,&t,nullptr));
        } catch(...) {if(object)cudaDestroyTextureObject(object);if(array)cudaFreeArray(array);throw;}
    }
    ~Texture(){if(object)cudaDestroyTextureObject(object);if(array)cudaFreeArray(array);}
    Texture(const Texture&)=delete;Texture& operator=(const Texture&)=delete;
};
__device__ inline uint32_t fetch_texel(cudaTextureObject_t tex,const uint32_t* global,uint32_t k,uint32_t width) {
    // The only floating point in model sampling is an exact integer-to-center address.
    // All admitted x,y are < 2^23, so x+0.5f and y+0.5f are exactly representable.
    return tex ? tex2D<unsigned int>(tex,float(k%width)+0.5f,float(k/width)+0.5f) : global[k];
}
__global__ void gambit_texture_probe(cudaTextureObject_t tex,const uint32_t* global,uint32_t* out,uint32_t count,uint32_t width) {
    const uint32_t i=blockIdx.x*blockDim.x+threadIdx.x;
    if(i<count)out[i]=fetch_texel(tex,global,i,width);
}
__global__ void gambit_prepare(cudaTextureObject_t tex,const uint32_t* global,const Cell* old,
                                const uint32_t* words,Sample* sample,const Control* control,Params p,Options o) {
    const uint32_t i=blockIdx.x*blockDim.x+threadIdx.x;
    if(i>=nodes(p))return;
    const Control c=*control;const uint32_t q=feedback_bit(i,words,c,o);
    const uint32_t k=lut_index(i,p,c,q,o);
    sample[i]=make_sample(fetch_texel(tex,global,k,p.width),old[i],q,p,o);
}
__global__ void gambit_advance(const Cell* old,Cell* next,const Sample* sample,uint32_t* words,Params p) {
    const uint32_t i=blockIdx.x*blockDim.x+threadIdx.x;
    const uint32_t n=nodes(p),nw=nwords(p);Cell x{};
    if(i<n){x=advance_cell(i,old,sample,p);next[i]=x;}
    // No early exit: every launched warp executes every ballot, including padded lanes.
    const uint32_t pulse=__ballot_sync(0xffffffffu,i<n && ((x.flags>>1)&1u));
    const uint32_t hinge=__ballot_sync(0xffffffffu,i<n && (x.flags&1u));
    const uint32_t event=__ballot_sync(0xffffffffu,i<n && ((x.flags>>3)&1u));
    const uint32_t inside=__ballot_sync(0xffffffffu,i<n && ((x.flags>>2)&1u));
    if((threadIdx.x&31u)==0u && (i>>5)<nw){
        const uint32_t w=i>>5;words[w]=pulse;words[nw+w]=hinge;words[2*nw+w]=event;
        words[3*nw+w]=inside;words[4*nw+w]=parity32(pulse);
    }
}
__global__ void gambit_summarize(const Cell* state,Control* c,Report* out,Params p) {
    __shared__ Report part[256];const uint32_t t=threadIdx.x;Report r{};
    for(uint32_t i=t;i<nodes(p);i+=256u){const Cell x=state[i];r.mass_u+=x.u;r.mass_v+=x.v;
        r.pulses+=(x.flags>>1)&1u;r.latches+=x.flags&1u;r.total_input+=x.total_input;
        r.total_output+=x.total_output;r.errors|=cell_errors(x);}
    part[t]=r;__syncthreads();
    for(uint32_t stride=128;stride;stride>>=1){
        if(t<stride){const Report b=part[t+stride];part[t].mass_u+=b.mass_u;part[t].mass_v+=b.mass_v;
            part[t].pulses+=b.pulses;part[t].latches+=b.latches;part[t].total_input+=b.total_input;
            part[t].total_output+=b.total_output;part[t].errors|=b.errors;}
        __syncthreads();
    }
    if(t==0){Control v=*c;Report result=part[0];finish_control(v,result,p);*c=v;*out=result;}
}
static std::string device_json(const cudaDeviceProp& p,int driver,int runtime,size_t free_bytes) {
    std::ostringstream o;o<<"\"device\":"<<quote_json(p.name)<<",\"compute_major\":"<<p.major<<",\"compute_minor\":"<<p.minor
    <<",\"total_vram_bytes\":"<<p.totalGlobalMem<<",\"free_vram_before_bytes\":"<<free_bytes
    <<",\"driver_api_version\":"<<driver<<",\"runtime_version\":"<<runtime
    <<",\"multiprocessors\":"<<p.multiProcessorCount<<",\"warp_size\":"<<p.warpSize;
    return o.str();
}
int main(int argc,char** argv){try {
    const auto args=parse_args(argc,argv);int count=0;CUDA_OK(cudaGetDeviceCount(&count));
    if(args.device>=uint32_t(count))throw std::runtime_error("Requested CUDA device not available");
    CUDA_OK(cudaSetDevice(args.device));cudaDeviceProp prop{};CUDA_OK(cudaGetDeviceProperties(&prop,args.device));
    int driver=0,runtime=0;CUDA_OK(cudaDriverGetVersion(&driver));CUDA_OK(cudaRuntimeGetVersion(&runtime));
    size_t free_bytes=0,total_bytes=0;CUDA_OK(cudaMemGetInfo(&free_bytes,&total_bytes));
    const auto hw=device_json(prop,driver,runtime,free_bytes);
    if(args.inspect){std::cout<<"{"<<hw<<"}\n";return 0;}
    if(prop.major!=12 || prop.minor!=0)throw std::runtime_error("This release targets compute capability 12.0; verify/rebuild an explicit port for another GPU");
    if(prop.warpSize!=32 || args.block>uint32_t(prop.maxThreadsPerBlock))throw std::runtime_error("Unsupported launch shape");
    auto a=read_asset(args.asset);if(args.steps)a.p.steps=args.steps;validate(a.p);const Params p=a.p;
    if(args.options.inject_cell>=int32_t(nodes(p)))throw std::runtime_error("Injection cell out of bounds");
    const auto n=nodes(p),nw=nwords(p);const uint64_t lut_bytes=uint64_t(a.texels.size())*4;
    // Includes a temporary full-LUT readback probe in verification mode. Context/driver overhead is not included.
    const uint64_t budget=uint64_t(n)*(2*sizeof(Cell)+sizeof(Sample))+uint64_t(nw)*40+lut_bytes*(args.verify?2u:1u)+sizeof(Control)+sizeof(Report);
    if(budget>uint64_t(p.device_budget_mib)*1024*1024 || budget>uint64_t(free_bytes)*3/5)
        throw std::runtime_error("Allocation estimate exceeds declared cap or 60% of currently free VRAM");
    if(args.fetch=="texture" && (p.width>uint32_t(prop.maxTexture2D[0]) || p.height*p.levels>uint32_t(prop.maxTexture2D[1])))
        throw std::runtime_error("LUT exceeds device 2-D texture dimensions");
    std::unique_ptr<Texture> texture;std::unique_ptr<DeviceBuffer<uint32_t>> global;
    if(args.fetch=="texture")texture=std::make_unique<Texture>(a);
    else {global=std::make_unique<DeviceBuffer<uint32_t>>(a.texels.size());CUDA_OK(cudaMemcpy(global->data,a.texels.data(),lut_bytes,cudaMemcpyHostToDevice));}
    const cudaTextureObject_t tex=texture?texture->object:0;const uint32_t* gp=global?global->data:nullptr;
    if(args.verify){DeviceBuffer<uint32_t> probe(a.texels.size());std::vector<uint32_t> back(a.texels.size());
        gambit_texture_probe<<<uint32_t((a.texels.size()+255)/256),256>>>(tex,gp,probe.data,uint32_t(a.texels.size()),p.width);CUDA_OK(cudaGetLastError());
        CUDA_OK(cudaMemcpy(back.data(),probe.data,lut_bytes,cudaMemcpyDeviceToHost));
        if(back!=a.texels)throw std::runtime_error("Exhaustive LUT fetch/readback mismatch");}
    auto initial=initialize(a);const auto mass0=sum_mass(initial);
    DeviceBuffer<Cell> d0(n),d1(n);DeviceBuffer<Sample> ds(n);DeviceBuffer<uint32_t> w0(5*nw),w1(5*nw);
    DeviceBuffer<Control> dc(1);DeviceBuffer<Report> dr(1);Control ctrl{0,p.start_level,0};
    CUDA_OK(cudaMemcpy(d0.data,initial.data(),size_t(n)*sizeof(Cell),cudaMemcpyHostToDevice));
    CUDA_OK(cudaMemset(w0.data,0,size_t(5*nw)*4));CUDA_OK(cudaMemcpy(dc.data,&ctrl,sizeof(ctrl),cudaMemcpyHostToDevice));
    Cell *old=d0.data,*next=d1.data;uint32_t *oldwords=w0.data,*newwords=w1.data;
    std::unique_ptr<CpuEngine> oracle;if(args.verify)oracle=std::make_unique<CpuEngine>(a,args.options);
    Writer writer(args.out,p,p.steps);std::vector<Cell> state(n);std::vector<Sample> samples(args.verify?n:0);
    std::vector<uint32_t> words(5*nw);Report report{};
    const auto begin=std::chrono::steady_clock::now();
    for(uint32_t s=0;s<p.steps;++s){
        const uint32_t blocks=(n+args.block-1u)/args.block;
        gambit_prepare<<<blocks,args.block>>>(tex,gp,old,oldwords,ds.data,dc.data,p,args.options);CUDA_OK(cudaGetLastError());
        gambit_advance<<<blocks,args.block>>>(old,next,ds.data,newwords,p);CUDA_OK(cudaGetLastError());
        gambit_summarize<<<1,256>>>(next,dc.data,dr.data,p);CUDA_OK(cudaGetLastError());
        CUDA_OK(cudaMemcpy(&report,dr.data,sizeof(report),cudaMemcpyDeviceToHost));check_report(report,mass0);
        CUDA_OK(cudaMemcpy(words.data(),newwords,size_t(5*nw)*4,cudaMemcpyDeviceToHost));
        if(oracle){oracle->step();CUDA_OK(cudaMemcpy(state.data(),next,size_t(n)*sizeof(Cell),cudaMemcpyDeviceToHost));
            CUDA_OK(cudaMemcpy(samples.data(),ds.data,size_t(n)*sizeof(Sample),cudaMemcpyDeviceToHost));
            compare_states(state,oracle->state,s);
            for(uint32_t i=0;i<n;++i)if(samples[i].field!=oracle->samples[i].field || samples[i].drive!=oracle->samples[i].drive)
                throw std::runtime_error("CPU/GPU sample mismatch");
            if(words!=oracle->words)throw std::runtime_error("CPU/GPU packed words mismatch");
            const auto& r=oracle->report;
            if(report.mass_u!=r.mass_u || report.mass_v!=r.mass_v || report.pulses!=r.pulses || report.latches!=r.latches ||
               report.total_input!=r.total_input || report.total_output!=r.total_output || report.level_used!=r.level_used ||
               report.level_next!=r.level_next || report.growth!=r.growth || report.errors!=r.errors)throw std::runtime_error("CPU/GPU report mismatch");
            CUDA_OK(cudaMemcpy(&ctrl,dc.data,sizeof(ctrl),cudaMemcpyDeviceToHost));
            if(ctrl.step!=oracle->control.step || ctrl.level!=oracle->control.level || ctrl.last_growth!=oracle->control.last_growth)
                throw std::runtime_error("CPU/GPU control mismatch");
        }
        writer.frame(s,report,words);std::swap(old,next);std::swap(oldwords,newwords);
    }
    CUDA_OK(cudaDeviceSynchronize());CUDA_OK(cudaMemcpy(state.data(),old,size_t(n)*sizeof(Cell),cudaMemcpyDeviceToHost));
    CUDA_OK(cudaMemcpy(&ctrl,dc.data,sizeof(ctrl),cudaMemcpyDeviceToHost));writer.final_state(state,ctrl);
    const double wall_ms=std::chrono::duration<double,std::milli>(std::chrono::steady_clock::now()-begin).count();
    std::ostringstream meta;meta<<"{\"backend\":\"cuda\",\"model\":\"gambit-u3d-3.1\",\"status\":\""<<(args.verify?"GPU_CPU_EXACT_PASS":"GPU_INVARIANTS_PASS")
        <<"\",\"gpu_verified\":"<<(args.verify?"true":"false")<<",\"lut_readback_verified\":"<<(args.verify?"true":"false")
        <<","<<hw<<",\"fetch\":"<<quote_json(args.fetch)<<",\"block\":"<<args.block<<",\"steps\":"<<p.steps
        <<",\"feedback\":"<<args.options.feedback<<",\"inject_step\":"<<args.options.inject_step<<",\"inject_cell\":"<<args.options.inject_cell
        <<",\"allocation_upper_estimate_bytes\":"<<budget<<",\"wall_ms_including_io_and_oracle\":"<<wall_ms<<"}";
    write_run_json(args.out,meta.str());std::cout<<(args.verify?"GPU_CPU_EXACT_PASS":"GPU_INVARIANTS_PASS")<<" mass="<<mass0<<"\n";return 0;
} catch(const std::exception& e){std::cerr<<"FAIL: "<<e.what()<<'\n';return 1;}}
