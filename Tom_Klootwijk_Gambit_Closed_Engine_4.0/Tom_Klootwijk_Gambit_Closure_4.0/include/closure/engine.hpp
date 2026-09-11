#pragma once
// Tom Klootwijk Gambit, Formal Closure Edition 4.0.
// Author: Tom Klootwijk | NL200678942 | 10-07-1990.
// Offline numerical research only: no audio, optical or physical actuator output.
#include "gambit/host.hpp"
#include <array>
#include <functional>
namespace closure {
using gambit::Asset; using gambit::Cell; using gambit::Sample; using gambit::Params;
struct Clock { uint32_t phase=0, level=0, cooldown=0; };
struct Engine {
    Asset asset; uint32_t feedback=1; uint64_t mass0=0; Clock clock;
    std::vector<Cell> cells, scratch;
    std::vector<Sample> samples;
    std::vector<uint32_t> words;
    explicit Engine(Asset a, uint32_t feedback_enabled=1);
    // inject_read is an explicitly external test intervention, NOT part of T_sigma.
    // Normal execution always leaves it at -1.
    void tick(bool gates=false, int32_t inject_read=-1);
    void accept(std::vector<Cell> next, bool gates=false);
    void validate_state() const;
    void pack_words();
};
Sample gate_sample(uint32_t texel,const Cell& cell,uint32_t q,const Params& p,uint32_t feedback);
Cell gate_cell(uint32_t i,const std::vector<Cell>& old,const std::vector<Sample>& s,const Params& p);
Clock gate_clock(Clock old,uint64_t pulses,const Params& p);
uint64_t gate_count(const std::vector<Cell>& cells);
uint32_t gate_angle(uint32_t x,Clock clock,uint32_t q,const Params& p,uint32_t feedback);
std::vector<uint8_t> capsule(const Engine& e);
Engine from_capsule(const std::vector<uint8_t>& bytes);
std::vector<uint8_t> read_bytes(const std::string& path);
void write_bytes(const std::string& path,const std::vector<uint8_t>& bytes);
std::array<uint8_t,32> sha256(const std::vector<uint8_t>& data);
std::string hex_digest(const std::vector<uint8_t>& data);
struct Arguments {
    std::string asset, resume, out, backend="native", fetch="texture";
    uint32_t steps=64, feedback=1, block=256; bool feedback_set=false, inspect=false;
};
Arguments parse(int argc,char** argv);
using Advance=std::function<void(Engine&)>;
int write_run(Engine& e,const Arguments& args,const Advance& advance,const std::string& backend,
              const std::string& evidence="");
} // namespace closure
