import numpy as np
from numpy import pi
import os

fileName = "1cylinder0"

# Precision integers
n = 1    #pocet cylindrov
mmax = 10
mrow = np.arange(-mmax,mmax+1)
m = mrow.reshape((-1,1))
countf = 5001

# Environment variables and constants
frequencies = np.linspace (0, 1, countf)
epsilon = np.array([ 80 ]*n)
mi = 1.
zeta = np.sqrt (mi/epsilon)

# Geometry
R = np.array([0.45]*n)
x = np.arange(n)
y = np.array([0]*n)
gama = np.empty((n,n), dtype=np.float64)
a = np.empty((n,n), dtype=np.float64)
for i in range(n):
	for j in range(n):
		a[i,j]		= np.sqrt  ( (x[j]-x[i])**2 + (y[j]-y[i])**2  )
		gama[i,j]	= np.angle ( (x[j]-x[i])    + (y[j]-y[i]) *1j )


os.system("nano ./Inputs/"+fileName+".txt")
np.savez("./Inputs/"+ fileName +".npz", n=n, mmax=mmax, mrow=mrow, m=m, countf=countf, frequencies=frequencies, mi=mi, zeta=zeta, epsilon=epsilon, R=R, x=x, y=y, gama=gama, a=a)
