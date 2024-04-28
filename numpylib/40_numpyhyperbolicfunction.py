# Hyperbolic function: numpy provides the ufuncs like sinh(), cosh(), and tanh() that takes values in radian and produce the corresponding sinh, cosh and tanh values.
# here we will find the value of a sinh of pi/2.
import numpy as np
x=np.sinh(np.pi/2)
print(x)

# we will now find the cosh values in arrays
import numpy as np
x=np.array([np.pi/2,np.pi/3,np.pi/4,np.pi/5])
y=np.cosh(x)
print(y)

# finsing the angles: 
# here we can also find the angles: arcsinh(), arccosh(), and arctanh()
# that takes values in radian and produce the corresponding sinh, cosh and tanh values.

# we wull now find then angle of 1.0
import numpy as np
x=np.arcsinh(1.0)
print(x)

# angles of each values in an array:
import numpy as np
x=np.array([0.1,0.2,0.5])
y=np.arctanh(x)
print(y)