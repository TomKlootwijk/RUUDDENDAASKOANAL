"""V2 lossless address lift of the source's log-polar chart.

The exact 1D UU ID field keeps its own metric. This 3D lift is a separate family
of Euclidean sphere horizons, with bit layers and a dedicated control axis.
"""
from __future__ import annotations
from dataclasses import dataclass
import math
from .engine import Parameters
from .uuid import finite

@dataclass(frozen=True)
class AddressChart:
    A:int=32
    R:int=2
    layer_spacing:float=1/64
    def __post_init__(self):
        Parameters(A=self.A,R=self.R).validate()
        z=finite(self.layer_spacing)
        if z<=0:raise ValueError("Positive layer spacing required")
    @property
    def count(self)->int:return 27+118*self.A*self.R
    @property
    def minimum_separation(self)->float:
        r0=1/32
        return min(self.layer_spacing,r0,2*r0*math.sin(math.pi/self.A),r0*math.expm1(math.log(128)/(self.R-1)))
    @property
    def horizon_radius(self)->float:return self.minimum_separation/4
    @property
    def anchor(self)->tuple[float,float,float]:return 0.0,0.0,-self.layer_spacing
    def centre(self,j:int)->tuple[float,float,float]:
        if type(j) is not int or not 1<=j<=self.count:raise ValueError("Bit address outside chart")
        if j<=27:return 0.0,0.0,(j-1)*self.layer_spacing
        i,k=divmod(j-28,118);y,x=divmod(i,self.A)
        rho=math.log(1/32)+y/(self.R-1)*math.log(128);theta=2*math.pi*x/self.A
        return math.exp(rho)*math.cos(theta),math.exp(rho)*math.sin(theta),k*self.layer_spacing
    def address(self,j:int)->dict:
        c=self.centre(j)
        if j<=27:return {"global_bit":j,"kind":"control","control_bit":j-1,"cell":None,"local_bit":None,"centre":list(c)}
        cell,k=divmod(j-28,118)
        return {"global_bit":j,"kind":"cell","control_bit":None,"cell":cell,"local_bit":k,"centre":list(c)}
    def raw_logpolar(self,x:float,y:float)->dict:
        x,y=finite(x),finite(y);r=math.hypot(x,y)
        if r==0:return {"core":True,"rho":None,"theta":None}
        return {"core":False,"rho":math.log(r),"theta":math.atan2(y,x)}
    def unsigned_field(self,bits:tuple[int,...],point:tuple[float,float,float])->float:
        if len(bits)!=self.count or any(type(b) is not int or b not in (0,1) for b in bits):raise ValueError("Invalid chart word")
        if len(point)!=3:raise ValueError("A three-dimensional query is required")
        q=tuple(finite(x) for x in point);a=self.horizon_radius
        centres=[self.anchor]+[self.centre(j) for j,b in enumerate(bits,1) if b]
        return min(abs(math.dist(q,c)-a) for c in centres)
