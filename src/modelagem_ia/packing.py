import math,numpy as np
KNOWN_D_SMALL={2:math.sqrt(3),3:math.sqrt(2),4:math.sqrt(2),5:math.sqrt(5)/2}
def radius_in_cube_from_d(d,L=1.): return d*L/(2*(1+d))
def min_cube_edge_from_d(d,r=1.): return 2*r*(1+1/d)
def occupied_fraction_cube(n,r,L=1.): return n*(4/3)*math.pi*r**3/L**3
def tetrahedral_number(k): return k*(k+1)*(k+2)//6
def tetra_container_edge(k,r=1.): return 2*r*(k-1+math.sqrt(6))
def tetra_container_volume(k,r=1.):
    a=tetra_container_edge(k,r); return math.sqrt(2)/12*a**3
def tetra_packing_density(k): return tetrahedral_number(k)*(4/3)*math.pi/tetra_container_volume(k)
def kepler_density(): return math.pi/(3*math.sqrt(2))
def kepler_void_fraction(): return 1-kepler_density()
SPHERE_RATIOS_1_13={1:1.,2:.5,3:2*math.sqrt(3)-3,4:math.sqrt(6)-2,5:math.sqrt(2)-1,6:math.sqrt(2)-1,7:.385914,8:1/(1+math.sqrt(2+1/math.sqrt(2))),9:1/(1+math.sqrt(3)),10:.353049,11:.344577,12:.344577,13:1/3}
def sphere_occupancy(n,r): return n*r**3
def sphere_void(n,r): return 1-sphere_occupancy(n,r)
def min_pair_distance(points):
    p=np.asarray(points,float); d=float('inf')
    for i in range(len(p)-1):
        q=p[i+1:]-p[i]; d=min(d,float(np.sqrt((q*q).sum(axis=1)).min()))
    return d
