# finding LCM(Lowest common multiple)
# here we will find the LCM of the 2 numbers :

import numpy as np
x=4
y=6
z=np.lcm(x,y)
print(z)
# the answers of the above is 12 because the LCM of both numbers (4*3=12 and 6*12)

# finding the LCM in array
import numpy as np
x=np.array([3,6,9])
y=np.lcm.reduce(x) # the reduce method will used the ufunc, in this case the lcm() function on each element and it will reduce the array by 1 dimension
print(y)

# here we will find the LCM of all of an array where the array contains all integers from 1 to 10
import numpy as np
x=np.arange(1,11)
y=np.lcm.reduce(x)
print(y)