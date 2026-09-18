import math,sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parents[1]/'src'))
from modelagem_ia.packing import *
from modelagem_ia.fcc import *
assert abs(radius_in_cube_from_d(math.sqrt(3))-((3-math.sqrt(3))/4))<1e-12
assert tetrahedral_number(4)==20
assert abs(kepler_density()-math.pi/math.sqrt(18))<1e-15
V,_,a=fcc_adjacency(18); assert len(V)==2916; c=corner_vertex_index(V); assert len(a[c])==3; assert bfs_ball_size(a,c,12)==938
print('Todos os testes centrais passaram.')
