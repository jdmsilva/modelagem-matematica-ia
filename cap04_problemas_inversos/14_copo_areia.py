#!/usr/bin/env python3
import argparse,pandas as pd
from modelagem_ia.packing import kepler_void_fraction
ap=argparse.ArgumentParser(); ap.add_argument('arquivo'); x=ap.parse_args(); df=pd.read_csv(x.arquivo); df['porosidade_exp']=df.V_agua/df.V_copo; df['diferenca_Kepler']=df.porosidade_exp-kepler_void_fraction(); print('Kepler-vazio',kepler_void_fraction()); print(df); print('media',df.porosidade_exp.mean()); df.to_csv('copo_areia_analisado.csv',index=False)
