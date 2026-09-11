#pragma once
// Executable bit-register ALU. Every stored digit is 0/1, LSB first.
// Loops, array addressing and host conversion are infrastructure; this is not a
// claim that the host CPU, its instructions or its physical registers are 1-bit.
#include <array>
#include <cstdint>
#include <stdexcept>
namespace closure::bits {
using Bit=uint8_t;
inline Bit Not(Bit a){return a^Bit(1);}
inline Bit And(Bit a,Bit b){return a&b;}
inline Bit Or(Bit a,Bit b){return a|b;}
inline Bit Xor(Bit a,Bit b){return a^b;}
inline Bit select(Bit s,Bit a,Bit b){return Or(And(s,a),And(Not(s),b));}
template<size_t W> struct Word {
    std::array<Bit,W> b{};
    static Word from(uint64_t v){Word x;for(size_t i=0;i<W;++i)x.b[i]=i<64?Bit((v>>i)&1u):0;return x;}
    uint64_t value()const{uint64_t v=0;for(size_t i=0;i<W && i<64;++i)v|=uint64_t(b[i])<<i;return v;}
};
template<size_t W> Word<W> mux(Bit s,const Word<W>& a,const Word<W>& b){Word<W> r;for(size_t i=0;i<W;++i)r.b[i]=select(s,a.b[i],b.b[i]);return r;}
template<size_t W> Word<W> add(const Word<W>& a,const Word<W>& b){Word<W> r;Bit c=0;for(size_t i=0;i<W;++i){auto x=Xor(a.b[i],b.b[i]);r.b[i]=Xor(x,c);c=Or(And(a.b[i],b.b[i]),And(x,c));}return r;}
template<size_t W> Word<W> neg(const Word<W>& a){Word<W> n;for(size_t i=0;i<W;++i)n.b[i]=Not(a.b[i]);return add(n,Word<W>::from(1));}
template<size_t W> Word<W> sub(const Word<W>& a,const Word<W>& b){return add(a,neg(b));}
template<size_t W> Bit eq(const Word<W>& a,const Word<W>& b){Bit r=1;for(size_t i=0;i<W;++i)r=And(r,Not(Xor(a.b[i],b.b[i])));return r;}
template<size_t W> Bit lt(const Word<W>& a,const Word<W>& b){Bit borrow=0;for(size_t i=0;i<W;++i)borrow=Or(And(Not(a.b[i]),b.b[i]),And(Not(Xor(a.b[i],b.b[i])),borrow));return borrow;}
template<size_t W> Word<W> shl(const Word<W>& a,size_t k){Word<W> r;for(size_t i=k;i<W;++i)r.b[i]=a.b[i-k];return r;}
template<size_t W> Word<W> shr(const Word<W>& a,size_t k){Word<W> r;for(size_t i=0;i+k<W;++i)r.b[i]=a.b[i+k];return r;}
template<size_t V,size_t W> Word<V> extend(const Word<W>& a){Word<V> r;for(size_t i=0;i<V && i<W;++i)r.b[i]=a.b[i];return r;}
template<size_t W> Word<W> mul(const Word<W>& a,const Word<W>& b){Word<W> r;for(size_t i=0;i<W;++i)r=add(r,mux(b.b[i],shl(a,i),Word<W>{}));return r;}
template<size_t W> Word<W> divu(const Word<W>& a,const Word<W>& d){
    if(eq(d,Word<W>{}))throw std::runtime_error("Boolean division by zero");
    Word<W> q;Word<W+1> r;const auto divisor=extend<W+1>(d);
    for(size_t k=W;k>0;--k){r=shl(r,1);r.b[0]=a.b[k-1];Bit ge=Not(lt(r,divisor));r=mux(ge,sub(r,divisor),r);q.b[k-1]=ge;}
    return q;
}
// Signed two's-complement division, truncation toward zero, positive denominator.
template<size_t W> Word<W> div_signed_positive(const Word<W>& a,const Word<W>& d){auto s=a.b[W-1];auto mag=mux(s,neg(a),a);auto q=divu(mag,d);return mux(s,neg(q),q);}
template<size_t W> Bit signed_lt(const Word<W>& a,const Word<W>& b){auto sa=a.b[W-1],sb=b.b[W-1];return select(Xor(sa,sb),sa,lt(a,b));}
} // namespace closure::bits
