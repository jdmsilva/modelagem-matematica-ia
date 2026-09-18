#!/usr/bin/env python3
import argparse,numpy as np,pandas as pd,networkx as nx
from modelagem_ia.packing import min_pair_distance
ap=argparse.ArgumentParser(); ap.add_argument('arquivo'); ap.add_argument('--tol',type=float,default=1e-5); x=ap.parse_args(); p=pd.read_csv(x.arquivo)[['x','y','z']].to_numpy(float); d=min_pair_distance(p); G=nx.Graph(); G.add_nodes_from(range(len(p)))
for i in range(len(p)):
 for j in range(i+1,len(p)):
  q=np.linalg.norm(p[i]-p[j]);
  if q<=d+x.tol: G.add_edge(i,j,distancia=float(q))
print('dmin',d,'arestas',G.number_of_edges(),'graus',dict(G.degree())); nx.write_gexf(G,'grafo_contatos.gexf')
