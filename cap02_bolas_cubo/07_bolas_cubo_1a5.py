#!/usr/bin/env python3
import math,pandas as pd
from modelagem_ia.packing import *
rows=[dict(n=1,d_n=None,r_n_L=.5,ocupacao=math.pi/6,vazio=1-math.pi/6)]
for n,d in KNOWN_D_SMALL.items():
 r=radius_in_cube_from_d(d); o=occupied_fraction_cube(n,r); rows.append(dict(n=n,d_n=d,r_n_L=r,ocupacao=o,vazio=1-o))
df=pd.DataFrame(rows); print(df); df.to_csv('bolas_cubo_1a5.csv',index=False)
