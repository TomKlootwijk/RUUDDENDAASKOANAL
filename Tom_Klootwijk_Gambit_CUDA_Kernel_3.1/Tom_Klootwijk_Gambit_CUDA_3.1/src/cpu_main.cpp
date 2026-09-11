#include "gambit/host.hpp"
#include <iostream>
#include <chrono>
int main(int argc,char** argv) {try {
    using namespace gambit;auto args=parse_args(argc,argv);if(args.inspect){std::cout<<"CPU reference only; no GPU verification\n";return 0;}
    auto a=read_asset(args.asset);if(args.steps)a.p.steps=args.steps;validate(a.p);
    CpuEngine e(std::move(a),args.options);Writer w(args.out,e.a.p,e.a.p.steps);auto mass0=sum_mass(e.state);
    const auto start=std::chrono::steady_clock::now();
    for(uint32_t s=0;s<e.a.p.steps;++s){e.step();check_report(e.report,mass0);w.frame(s,e.report,e.words);}
    w.final_state(e.state,e.control);
    const auto ms=std::chrono::duration<double,std::milli>(std::chrono::steady_clock::now()-start).count();
    write_run_json(args.out,"{\"backend\":\"cpu\",\"model\":\"gambit-u3d-3.1\",\"gpu_verified\":false,\"status\":\"CPU_PASS\",\"steps\":"+std::to_string(e.a.p.steps)+",\"feedback\":"+std::to_string(args.options.feedback)+",\"inject_step\":"+std::to_string(args.options.inject_step)+",\"inject_cell\":"+std::to_string(args.options.inject_cell)+",\"wall_ms\":"+std::to_string(ms)+"}");
    std::cout<<"CPU_PASS steps="<<e.a.p.steps<<" cells="<<e.state.size()<<" mass="<<mass0<<"\n";return 0;
} catch(const std::exception& e){std::cerr<<"FAIL: "<<e.what()<<'\n';return 1;}}
