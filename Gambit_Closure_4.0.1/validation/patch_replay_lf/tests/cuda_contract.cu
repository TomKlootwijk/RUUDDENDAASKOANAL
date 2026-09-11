// Regression proof for the production CUDA error wrapper. No device is required.
// Including the production translation unit prevents a copied helper from drifting.
#define main gambit_cuda_program_main
#include "../src/cuda.cu"
#undef main

int main(){try{
    int e=0;
    CU((++e,cudaSuccess));
    if(e!=1)throw std::runtime_error("Successful CUDA expression was not evaluated exactly once");
    bool caught=false;
    try{CU((++e,cudaErrorInvalidValue));}
    catch(const std::runtime_error& failure){
        caught=true;
        const auto expected=std::string("(++e,cudaErrorInvalidValue): ")+cudaGetErrorString(cudaErrorInvalidValue);
        if(failure.what()!=expected)throw std::runtime_error("CUDA failure lost expression or runtime error description");
    }
    if(!caught || e!=2)throw std::runtime_error("Failed CUDA expression did not throw after exactly one evaluation");
    // The wrapper must also remain usable as one statement in an if/else.
    if(e==2)CU((++e,cudaSuccess));else throw std::runtime_error("Unexpected branch");
    if(e!=3)throw std::runtime_error("CUDA wrapper statement contract failed");
    std::cout<<"PASS CUDA wrapper: local e preserved; success/failure evaluated once; exact error text; if/else statement\n";
    return 0;
}catch(const std::exception& failure){std::cerr<<"FAIL: "<<failure.what()<<'\n';return 1;}}
