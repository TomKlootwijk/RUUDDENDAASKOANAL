#pragma once
#include "model.hpp"
#include <vector>
#include <string>
#include <fstream>
#include <memory>
namespace gambit {
struct Asset { Params p; std::vector<uint32_t> texels; };
struct RunArgs {
    std::string asset, out="run", fetch="texture";
    uint32_t steps=0,block=256,device=0;
    Options options{1u,-1,-1};
    bool verify=false, inspect=false;
};
Asset read_asset(const std::string& path);
void validate(const Params& p);
RunArgs parse_args(int argc,char** argv);
std::vector<Cell> initialize(const Asset& a);
struct CpuEngine {
    Asset a; Options options; Control control; Report report{};
    std::vector<Cell> state, next; std::vector<Sample> samples;
    std::vector<uint32_t> words;
    explicit CpuEngine(Asset asset,Options opts);
    void step();
};
struct Writer {
    std::string dir; std::ofstream words_file,summary_file;
    Writer(const std::string& path,const Params& p,uint32_t steps);
    void frame(uint32_t step,const Report& r,const std::vector<uint32_t>& words);
    void final_state(const std::vector<Cell>& s,const Control& c);
};
void check_report(const Report& r,uint64_t mass0);
void compare_states(const std::vector<Cell>& a,const std::vector<Cell>& b,uint32_t step);
void write_run_json(const std::string& dir,const std::string& json);
std::string quote_json(const std::string& s);
uint64_t sum_mass(const std::vector<Cell>& s);
} // namespace
