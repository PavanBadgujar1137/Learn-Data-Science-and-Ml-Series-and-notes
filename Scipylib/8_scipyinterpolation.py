# What is Interpolation : it is a method for generating points between the given points. and the method of filling the values is called imputation.

# now how we can implement it in scipy? via module scipy.interpolate
# 1D interpolation: interp1d()

# here for given xs and ys interpolatevalues for 2.1,2.2,2.3........2.9:
from scipy.interpolate import interp1d
import numpy as np
xs=np.arange(10)
ys=2*xs+1
interp_func= interp1d(xs,ys)
x=interp_func(np.arange(2.1,3,0.1))
print(x)

# spline interpolation : 
# example: here now we will find the univariate spline interpolation for 2.1, 2.2,2.3 .... 2.9.
from scipy.interpolate import UnivariateSpline
import numpy as np
xs = np.arange(10)
ys= xs**2+np.sin(xs) + 1
interp_func=UnivariateSpline(xs,ys)
x=interp_func(np.arange(2.1, 3, 0.1))
print(x)

# Interpolation with Radial basis Function(RBF)

from scipy.interpolate import Rbf
import numpy as np
xs=np.arange(10)
ys=xs**2+np.sin(xs)+1
interp_func=Rbf(xs,ys)
x=interp_func(np.arange(2.1,3,0.1))

print(x)
