# optimizers in scipy : they are a set of procedure defined in scify thaat either find the minimum value of a function of root of an equation.
# Optimizing function : all the algorithms which helps in minimizing the data.
# Root of an equation : x+cos(x), we will solve it via optimize.root function. 
# this function takes 2 arguments : 'func' and x0

# example:here we will fiind the root of equation: x+cos(x)
from scipy.optimize import root
from math import cos

def eqn(x):
    return x+cos(x)

myroot=root(eqn, 0)
print(myroot.x)

# here we want the info about just x but the whole root:
from scipy.optimize import root
from math import cos

def eqn(x):
    return x+cos(x)

myroot=root(eqn, 0)
print(myroot)

# Minimizing the function or data:
# high points are called maxima and low points are called minima 
# finding the minima:
# we usae scipy.optimize.minimize() . it uses 3 arguments : "fun", x0,and method: it also has some leagal value : "CG","BFGS","NEWTON-CG","L-BFGS","TNC","COBYLA","SLSQP".
# callback : functions calles after each iteration of optimization.


# Example of the above in which we will minimize the function x^2+x+2 with BFGS:
from scipy.optimize import minimize
def eqn(x):
    return x**2+x+2
mymin=minimize(eqn,0,method="BFGS")
print(mymin.x)
