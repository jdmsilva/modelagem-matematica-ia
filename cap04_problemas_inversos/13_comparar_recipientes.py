#!/usr/bin/env python3
import argparse,pandas as pd
ap=argparse.ArgumentParser(); ap.add_argument('arquivo'); x=ap.parse_args(); df=pd.read_csv(x.arquivo); req={'n','recipiente','volume','status','fonte'}
if not req.issubset(df.columns): raise SystemExit('Colunas exigidas: '+str(sorted(req)))
w=df.loc[df.groupby('n')['volume'].idxmin()].sort_values('n'); print(w); w.to_csv('recipientes_vencedores.csv',index=False)
