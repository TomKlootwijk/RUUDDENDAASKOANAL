"""Digit-array arithmetic constructions supporting source proof C10."""
from __future__ import annotations

def bits(value:int,width:int)->tuple[int,...]:
    if type(value) is not int or type(width) is not int or width<1 or not 0<=value<1<<width:raise ValueError("Invalid unsigned word")
    return tuple(value>>j&1 for j in range(width))

def integer(word:tuple[int,...])->int:
    if not word or any(type(x) is not int or x not in (0,1) for x in word):raise ValueError("Invalid Boolean digits")
    return sum(x<<j for j,x in enumerate(word))

def full_adder(a:int,b:int,c:int)->tuple[int,int]:
    if any(type(x) is not int or x not in (0,1) for x in (a,b,c)):raise ValueError("Boolean inputs required")
    return a^b^c,(a&b)|((a^b)&c)

def add(a:tuple[int,...],b:tuple[int,...])->tuple[tuple[int,...],int]:
    if len(a)!=len(b) or not a:raise ValueError("Equal nonempty widths required")
    carry=0;out=[]
    for x,y in zip(a,b):s,carry=full_adder(x,y,carry);out.append(s)
    return tuple(out),carry

def negate(a:tuple[int,...])->tuple[int,...]:
    integer(a);return add(tuple(x^1 for x in a),(1,)+(0,)*(len(a)-1))[0]

def subtract(a:tuple[int,...],b:tuple[int,...])->tuple[int,...]:return add(a,negate(b))[0]

def less(a:tuple[int,...],b:tuple[int,...])->int:
    if len(a)!=len(b):raise ValueError("Equal widths required")
    integer(a);integer(b);borrow=0
    for x,y in zip(a,b):borrow=((x^1)&(y|borrow))|(y&borrow)
    return borrow

def multiply(a:tuple[int,...],b:tuple[int,...])->tuple[int,...]:
    if len(a)!=len(b):raise ValueError("Equal widths required")
    integer(a);integer(b);out=(0,)*len(a)
    for shift,enable in enumerate(b):out=add(out,tuple(a[j-shift]&enable if j>=shift else 0 for j in range(len(a))))[0]
    return out

def divide(a:tuple[int,...],b:tuple[int,...])->tuple[tuple[int,...],tuple[int,...]]:
    if len(a)!=len(b) or integer(b)==0:raise ValueError("Equal widths and nonzero divisor required")
    integer(a);w=len(a);r=(0,)*(w+1);d=b+(0,);q=[0]*w
    for j in range(w-1,-1,-1):
        trial=(a[j],)+r[:-1];take=less(trial,d)^1;diff=subtract(trial,d)
        r=tuple((a&take)|(b&(take^1)) for a,b in zip(diff,trial));q[j]=take
    return tuple(q),r[:w]
