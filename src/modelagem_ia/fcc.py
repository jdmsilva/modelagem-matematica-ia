from collections import deque
from itertools import permutations,product
import random,numpy as np

def fcc_vertices(m=18):
    return [(i,j,k) for i in range(m) for j in range(m) for k in range(m) if (i+j+k)%2==0]

def neighbor_offsets():
    offs=set()
    for p in set(permutations((1,1,0))):
        nz=[i for i,v in enumerate(p) if v]
        for s in product((-1,1),repeat=2):
            q=list(p); q[nz[0]]*=s[0]; q[nz[1]]*=s[1]; offs.add(tuple(q))
    return sorted(offs)
OFFSETS=neighbor_offsets()

def fcc_adjacency(m=18):
    V=fcc_vertices(m); idx={v:i for i,v in enumerate(V)}; adj=[[] for _ in V]
    for i,(x,y,z) in enumerate(V):
        for dx,dy,dz in OFFSETS:
            j=idx.get((x+dx,y+dy,z+dz))
            if j is not None: adj[i].append(j)
    return V,idx,adj

def boundary_distance(v,m=18):
    i,j,k=v; return min(i,j,k,m-1-i,m-1-j,m-1-k)

def bfs_ball_size(adj,source,h):
    seen={source}; q=deque([(source,0)])
    while q:
        u,d=q.popleft()
        if d==h: continue
        for w in adj[u]:
            if w not in seen: seen.add(w); q.append((w,d+1))
    return len(seen)

def perturb_adjacency(adj,removal_fraction,seed=2026):
    rng=random.Random(seed); edges=[(u,v) for u,ns in enumerate(adj) for v in ns if u<v]
    removed=set(rng.sample(edges,int(round(removal_fraction*len(edges)))))
    out=[set() for _ in adj]
    for u,v in edges:
        if (u,v) not in removed: out[u].add(v); out[v].add(u)
    return [sorted(s) for s in out]

def simulate_synchronous(adj,p,source,steps=12,seed=2026):
    rng=np.random.default_rng(seed); inf=np.zeros(len(adj),dtype=bool); inf[source]=True; totals=[1]
    for _ in range(steps):
        new=inf.copy()
        for i,ns in enumerate(adj):
            if inf[i]: continue
            m=sum(bool(inf[j]) for j in ns)
            if m and rng.random()<1-(1-p)**m: new[i]=True
        inf=new; totals.append(int(inf.sum()))
    return totals

def mean_final_size(adj,p,source,steps=12,runs=50,seed=2026):
    vals=[simulate_synchronous(adj,p,source,steps,seed+r)[-1] for r in range(runs)]
    return float(np.mean(vals)),float(np.std(vals,ddof=1) if len(vals)>1 else 0)

def calibrate_p(adj,source,target_fraction=.8,steps=12,runs=30,seed=2026,tol=.005,max_iter=16):
    lo,hi=0.,1.; n=len(adj); best=None
    for it in range(max_iter):
        p=(lo+hi)/2; mean,_=mean_final_size(adj,p,source,steps,runs,seed+1000*it); frac=mean/n; best=(p,frac)
        if abs(frac-target_fraction)<=tol: break
        if frac<target_fraction: lo=p
        else: hi=p
    return best

def central_vertex_index(V):
    a=np.asarray(V,float); c=a.mean(axis=0); return int(np.argmin(((a-c)**2).sum(axis=1)))

def corner_vertex_index(V):
    return V.index((0,0,0))
