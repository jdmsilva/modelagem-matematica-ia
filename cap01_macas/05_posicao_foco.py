#!/usr/bin/env python3
import argparse,numpy as np,pandas as pd
from modelagem_ia.fcc import *
ap=argparse.ArgumentParser(); ap.add_argument('--p',type=float,default=.290215); ap.add_argument('--passos',type=int,default=12); ap.add_argument('--focos',type=int,default=68); ap.add_argument('--runs',type=int,default=30); x=ap.parse_args(); V,_,a=fcc_adjacency(18); rows=[]
for q,i in enumerate(np.linspace(0,len(V)-1,min(x.focos,len(V)),dtype=int)):
 m,sd=mean_final_size(a,x.p,int(i),x.passos,x.runs,2026+100*q); rows.append(dict(indice=int(i),x=V[i][0],y=V[i][1],z=V[i][2],grau=len(a[i]),dist_fronteira=boundary_distance(V[i]),alcance_Rh=bfs_ball_size(a,int(i),x.passos)/len(V),S_h_media=m,dp=sd,fracao=m/len(V)))
df=pd.DataFrame(rows); df.to_csv('posicoes_foco.csv',index=False); print(df.corr(numeric_only=True)['S_h_media'].sort_values(ascending=False))
