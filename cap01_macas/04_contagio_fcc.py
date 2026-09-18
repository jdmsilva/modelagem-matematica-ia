#!/usr/bin/env python3
import argparse,matplotlib.pyplot as plt
from modelagem_ia.fcc import *
ap=argparse.ArgumentParser(); ap.add_argument('--p',type=float,default=.290215); ap.add_argument('--foco',choices=['centro','canto'],default='centro'); ap.add_argument('--passos',type=int,default=12); ap.add_argument('--seed',type=int,default=2026); x=ap.parse_args(); V,_,a=fcc_adjacency(18); s=central_vertex_index(V) if x.foco=='centro' else corner_vertex_index(V); t=simulate_synchronous(a,x.p,s,x.passos,x.seed); print(t,'fracao final',t[-1]/len(V)); plt.plot(range(len(t)),t,'o-'); plt.grid(alpha=.3); plt.savefig('contagio_fcc.png',dpi=180)
