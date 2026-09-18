#!/usr/bin/env python3
import argparse,pandas as pd
from modelagem_ia.packing import *
ap=argparse.ArgumentParser(); ap.add_argument('--r',type=float,default=1.); x=ap.parse_args(); rows=[dict(n=1,L=2*x.r,V=(2*x.r)**3)]
for n,d in KNOWN_D_SMALL.items(): L=min_cube_edge_from_d(d,x.r); rows.append(dict(n=n,L=L,V=L**3))
df=pd.DataFrame(rows); print(df); df.to_csv('problema_inverso_cubo.csv',index=False)
