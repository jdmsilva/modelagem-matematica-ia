#!/usr/bin/env python3
"""Busca heuristica. O melhor encontrado nao implica otimalidade provada."""
import argparse,numpy as np
from scipy.optimize import differential_evolution
from modelagem_ia.packing import *
ap=argparse.ArgumentParser(); ap.add_argument('n',type=int); ap.add_argument('--seed',type=int,default=2026); ap.add_argument('--maxiter',type=int,default=500); x=ap.parse_args(); obj=lambda z:-min_pair_distance(np.asarray(z).reshape(x.n,3)); r=differential_evolution(obj,[(0,1)]*(3*x.n),seed=x.seed,maxiter=x.maxiter,popsize=8,polish=True); p=r.x.reshape(x.n,3); d=-r.fun; np.savetxt(f'config_cubo_n{x.n}.csv',p,delimiter=',',header='x,y,z',comments=''); print('d=',d,'r/L=',radius_in_cube_from_d(d)); print('STATUS: melhor encontrado nesta execucao; nao prova otimalidade.')
