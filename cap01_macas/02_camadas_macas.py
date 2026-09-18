#!/usr/bin/env python3
import numpy as np,matplotlib.pyplot as plt,importlib.util
from pathlib import Path
S=[1,13,57,153,323,587,967,1483,2007,2457,2784,2952,2990,2996]
def A(n): return 1+3*n*(n+1)
def P(n): return 3*(2*n-1)
def Q(n): return 3*n*n
def main():
 print([(n,A(n),P(n),Q(n)) for n in range(1,8)]); p=Path(__file__).with_name('01_logistica_macas.py'); s=importlib.util.spec_from_file_location('l',p); l=importlib.util.module_from_spec(s); s.loader.exec_module(l); t=np.linspace(0,18,400); plt.plot(t,l.logistic(t),label='logistica'); plt.plot(np.arange(len(S))*(12/8.8),S,'o-',label='camadas'); plt.legend(); plt.grid(alpha=.3); plt.savefig('comparacao_logistica_camadas.png',dpi=180)
if __name__=='__main__': main()
