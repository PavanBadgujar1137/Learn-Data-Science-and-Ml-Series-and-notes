# products : use prod() function.
# here we will find the product of element of the below array.
import numpy as np
x=np.array([1,2,3,4])
y=np.prod(x)
print(y)

# product over an axis
import numpy as np
x=np.array([1,2,3,4])
y=np.array([1,2,3,4])
z=np.prod([x,y], axis=1)
print(z)

# here we will find the product of elements in 2 differences
import numpy as np
x=np.array([1,2,3,4])
y=np.array([5,6,7,8])
z=np.prod([x,y])
print(z)

# cummulative product 
# example the partiall product of [1,2,3,4] is [1,1*2,1*2*3,1*2*3*4]=> [1,2,6,24] represented by cumprod()
import numpy as np
x=np.array([1,2,3,4])
y=np.cumprod([x])
print(y)