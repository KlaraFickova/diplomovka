import numpy as np
from numpy import pi
import os

fileName = "1dipol1test"

# Precision integers
n = 2    #pocet cylindrov
mmax = 8
mrow = np.arange(-mmax,mmax+1)
m = mrow.reshape((-1,1))
countf = 1

# Environment variables and constants
frequencies = np.array([0.838])
epsilon = np.array([ (3.5 + 0.05*1j)**2, (3.5 - 0.05*1j)**2 ]) # refractive index n=sqrt(epsilon_r * mi_r) @wiki
mi = 1.
zeta = np.sqrt (mi/epsilon)

# Geometry
R = np.array([0.45]*n)
x = np.array([0]*n)
y = np.array([0.5, -0.5])
gama = np.empty((n,n), dtype=np.float64)
a = np.empty((n,n), dtype=np.float64)
for i in range(n):
	for j in range(n):
		a[i,j]		= np.sqrt  ( (x[j]-x[i])**2 + (y[j]-y[i])**2  )
		gama[i,j]	= np.angle ( (x[j]-x[i])    + (y[j]-y[i]) *1j )

os.system("nano ./Inputs/"+fileName+".txt")
np.savez("./Inputs/"+ fileName +".npz", n=n, mmax=mmax, mrow=mrow, m=m, countf=countf, frequencies=frequencies, mi=mi, zeta=zeta, epsilon=epsilon, R=R, x=x, y=y, gama=gama, a=a)
