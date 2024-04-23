# Joining the numpy array - here for this we will pass concadenate()

import numpy as np
x=np.array([1,2,3])
y=np.array([4,5,6])
c=np.concatenate((x,y))
print(c)

# joining of 2-D - arrays along with rows(axis=1)
import numpy as np
x=np.array([[1,2],[3,4]])
y=np.array([[5,6],[7,8]])
c=np.concatenate((x,y), axis=1)
print(c)

# Joining array using the stack function: 

import numpy as np
x=np.array([1,2,3])
y=np.array([4,5,6])
c=np.stack((x,y),axis=1)
print(c)

# Stacking along with rows : hstack()

import numpy as np
x=np.array([1,2,3])
y=np.array([4,5,6])
c=np.hstack((x,y))
print(c)

# Stacking along with column

import numpy as np
x=np.array([1,2,3])
y=np.array([4,5,6])
c=np.vstack((x,y))
print(c)


# Stcking along with height(depth)
# import numpy as np

import numpy as np
x=np.array([1,2,3])
y=np.array([4,5,6])
c=np.dstack((x,y))
print(c)