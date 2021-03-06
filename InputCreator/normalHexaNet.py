import numpy as np
import os

fileName = "normalHexaNet6"

# Precision integers
size = 5    #number of hexagons in upmost row
mmax = 10
mrow = np.arange(-mmax,mmax+1)
m = mrow.reshape((-1,1))
countf = 1001

# Geometry
h1 = np.sqrt(3)/2
Hex1 = [(-0.5, h1), (0.5, h1), (1, 0), (0.5, -h1), (-0.5, -h1), (-1, 0)] # (x, y) vertices of a single hexagon
XY = [(1.5*col + xy[0], 3*h1*row + xy[1]) for row in range(-size+1, size) for col in range( -2*size+np.abs(row)+2, 2*size-np.abs(row)-1, 2 ) for xy in Hex1 ]
x = np.array( [ xy[0] for xy in XY ] )
y = np.array( [ xy[1] for xy in XY ] )
n = len(XY)
R = np.array([0.45]*n)
gama = np.empty((n,n), dtype=np.float64)
a = np.empty((n,n), dtype=np.float64)
for i in range(n):
	for j in range(n):
		a[i,j]		= np.sqrt  ( (x[j]-x[i])**2 + (y[j]-y[i])**2  )
		gama[i,j]	= np.angle ( (x[j]-x[i])    + (y[j]-y[i]) *1j )

# Environment variables and constants
frequencies = np.linspace (0, 1, countf)
epsilon = np.array([ (1.1)**2 ]*(n))
mi = 1.
zeta = np.sqrt (mi/epsilon)

os.system("nano ./Inputs/"+fileName+".txt")
np.savez("./Inputs/"+ fileName +".npz", n=n, size=size, mmax=mmax, mrow=mrow, m=m, countf=countf, frequencies=frequencies, mi=mi, zeta=zeta, epsilon=epsilon, R=R, x=x, y=y, gama=gama, a=a)
