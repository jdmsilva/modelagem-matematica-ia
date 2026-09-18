#!/usr/bin/env python3
from modelagem_ia.fcc import *
V,_,a=fcc_adjacency(18); c=central_vertex_index(V); k=corner_vertex_index(V); print('vertices',len(V)); print('centro',V[c],'grau',len(a[c])); print('canto',V[k],'grau',len(a[k])); print('|B(canto,12)|',bfs_ball_size(a,k,12)); print('fracao',bfs_ball_size(a,k,12)/len(V))
