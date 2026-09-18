#!/usr/bin/env python3
import pandas as pd
from modelagem_ia.packing import *
df=pd.DataFrame([dict(n=n,r_R=r,ocupacao=sphere_occupancy(n,r),vazio=sphere_void(n,r)) for n,r in SPHERE_RATIOS_1_13.items()]); print(df); df.to_csv('esferas_na_esfera_1a13.csv',index=False)
