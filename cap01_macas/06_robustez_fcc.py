#!/usr/bin/env python3
import pandas as pd
from modelagem_ia.fcc import *
V,_,a=fcc_adjacency(18); c=central_vertex_index(V); k=corner_vertex_index(V); rows=[]
for q,f in enumerate([0,.05,.10,.20]):
 A=perturb_adjacency(a,f,2026+q); p,_=calibrate_p(A,c,.8,12,25,2026+100*q); mc,_=mean_final_size(A,p,c,12,40,3000+q); mk,_=mean_final_size(A,p,k,12,40,4000+q); rows.append(dict(remocao=f,p=p,centro=mc/len(V),canto=mk/len(V),diferenca_pp=100*(mc-mk)/len(V)))
df=pd.DataFrame(rows); print(df); df.to_csv('robustez_fcc.csv',index=False)
