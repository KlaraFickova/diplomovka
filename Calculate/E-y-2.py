import numpy as np
from scipy import special as bessel # we will use only bessel functions
import matplotlib as mpl
mpl.use('Agg')
import matplotlib.pyplot as plt
from numpy import pi
from matplotlib.colors import hsv_to_rgb
import time

start = time.time()
print (start)

inputName   = "1cylinder2"
outputName  = inputName + "-" + "E-y-2"

resultsData     = np.load("./Results/"+inputName+".npz")
inputData 		= np.load("./Inputs/"+inputName+".npz")

frequencies = inputData['frequencies']
alpha 		= resultsData['alpha']				#alpha[f,n,m]
beta 		= resultsData['beta']				#beta[f,n,m]

n 		= alpha.shape[1]
mrow 	= inputData['mrow']
m 		= mrow.reshape(1,-1)
mmax 	= alpha.shape[2] // 2

epsilon = inputData['epsilon']
mi		= inputData['mi']
idx		= 83
f		= frequencies[idx]
kv 		= 2*pi * f
k 		= np.sqrt( epsilon*mi )*kv

x0		= inputData['x']
y0		= inputData['y']
R		= inputData['R']
gama	= inputData['gama']
a		= inputData['a']

def polarR(x,y):
	return np.abs(x+1j*y)
def polarFi( x, y):
	return np.angle(x+1j*y)

#size 	= inputData['size']
X 		= np.array ( [0] )
Xleft 	= X[0]
Xright	= X[-1]
Ydown 	= -80.
Yup 	= 80.
dY 		= (-Ydown+Yup)/500.
dX		= dY
Y 		= np.arange ( Ydown, Yup, dY )

# E...[y,x,n,m]
E  = np.exp  ( 1j* kv* Y.reshape(-1,1) ) * np.ones((Y.size, X.size))
for i in range(n):
	for j in range(mrow.size):
		E += beta[idx,i,j] * \
			bessel.hankel1 ( mrow[j], kv*polarR( X.reshape(1,-1)-x0[i], Y.reshape(-1,1)-y0[i] ) )* \
			np.exp  ( 1j*mrow[j] * polarFi( X.reshape(1,-1)-x0[i], Y.reshape(-1,1)-y0[i] ) )



print (time.time() - start, "basic E computed")

for i in range(n):
	xleft 	= x0[i]-R[i]
	ixleft 	= int((xleft-Xleft)/dX)
	xright 	= x0[i]+R[i]
	ixright = int((xright-Xright)/dX)+1
	ydown 	= y0[i]-R[i]
	iydown 	= int((ydown-Ydown)/dY)
	yup 	= y0[i]+R[i]
	iyup 	= int((yup-Yup)/dY)+1

	for ix in range (ixleft, ixright) :
		for iy in range (iydown, iyup) :
			fi = polarFi( X[ix]-x0[i], Y[iy]-y0[i] )
			r = polarR( X[ix]-x0[i], Y[iy]-y0[i] )
			if r < R[i]:
				E [iy,ix] = np.sum( alpha[idx,i,:] * bessel.jv1 ( m, k[i]*r ) * \
				np.exp ( 1j*m* fi ) )


print (time.time() - start, "E inside cylinders computed")

np.savez ("./Results/" +outputName+ ".npz", E=E, X=X, Y=Y, f=f, idx=idx)
