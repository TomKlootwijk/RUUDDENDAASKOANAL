#include "closure/engine.hpp"
#include <iostream>
int main(int argc,char** argv){try{
    auto a=closure::parse(argc,argv);
    if(a.inspect){std::cout<<"{\"backend\":\"native_cpu\",\"gpu_verified\":false,\"one_bit_ALU\":\"software Boolean datapath\"}\n";return 0;}
    auto e=a.resume.empty()?closure::Engine(gambit::read_asset(a.asset),a.feedback):closure::from_capsule(closure::read_bytes(a.resume));
    return closure::write_run(e,a,[&a](closure::Engine& x){x.tick(a.backend=="gates");},a.backend);
}catch(const std::exception& e){std::cerr<<"FAIL: "<<e.what()<<'\n';return 1;}}
