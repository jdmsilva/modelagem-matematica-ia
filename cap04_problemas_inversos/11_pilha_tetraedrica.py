#!/usr/bin/env python3
import argparse,pandas as pd
from modelagem_ia.packing import *
ap=argparse.ArgumentParser(); ap.add_argument('--kmax',type=int,default=25); x=ap.parse_args(); rows=[]
for k in range(1,x.kmax+1):
 e=tetra_packing_density(k); rows.append(dict(k=k,T_k=tetrahedral_number(k),a_k=tetra_container_edge(k),V=tetra_container_volume(k),densidade=e,vazio=1-e))
df=pd.DataFrame(rows); print(df.head(10)); print('Kepler',kepler_density(),'vazio',kepler_void_fraction()); df.to_csv('pilha_tetraedrica.csv',index=False)
