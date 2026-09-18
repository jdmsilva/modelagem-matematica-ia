#!/usr/bin/env python3
import argparse,math,numpy as np,matplotlib.pyplot as plt
def calibrate_beta(T=3000,M0=1,t_cal=12,frac_cal=.8):
 A=(T-M0)/M0; return -math.log((T/(frac_cal*T)-1)/A)/(T*t_cal)
def logistic(t,T=3000,M0=1,beta=None):
 beta=calibrate_beta(T,M0) if beta is None else beta; A=(T-M0)/M0; return T/(1+A*np.exp(-beta*T*np.asarray(t)))
def t_for_fraction(f,T=3000,M0=1,beta=None):
 beta=calibrate_beta(T,M0) if beta is None else beta; A=(T-M0)/M0; return math.log(A*f/(1-f))/(beta*T)
def main():
 ap=argparse.ArgumentParser(); ap.add_argument('--T',type=int,default=3000); ap.add_argument('--M0',type=float,default=1); ap.add_argument('--t-cal',type=float,default=12); ap.add_argument('--frac-cal',type=float,default=.8); ap.add_argument('--dias',type=float,default=18); a=ap.parse_args(); b=calibrate_beta(a.T,a.M0,a.t_cal,a.frac_cal); print('beta=',b,'beta*T=',b*a.T,'t50=',t_for_fraction(.5,a.T,a.M0,b),'t99=',t_for_fraction(.99,a.T,a.M0,b)); t=np.linspace(0,a.dias,400); plt.plot(t,logistic(t,a.T,a.M0,b)); plt.scatter([a.t_cal],[a.frac_cal*a.T]); plt.grid(alpha=.3); plt.xlabel('tempo (dias)'); plt.ylabel('contaminadas'); plt.tight_layout(); plt.savefig('logistica_macas.png',dpi=180)
if __name__=='__main__': main()
