# now we will create numpy ndarray object.
# The array object in numpy is called ndarray
# array()

import numpy as np
x=np.array([1,2,3,4,5])
print(x)
print(type(x))

# we can also passs a list, tuple or any array like objec6t with array(). and it will be converted to ndarray.
import numpy as np
y=np.array((1,2,3,4,5))
print(y)
print(type(y))

# Dimensions in Arrays - a dimension in arrays is one level of array depth(nested array)

# 0-D Arrays - Scalars, are the elements in an array, each value in an array is a 0-D array.
# 
# Now we will create 0-D array  with a value 42
import numpy as np
x= np.array(42)
print(x)

# 1-D arrays - an arrays that has 0-D arrays as its elements is called uni directional or 1-D
import numpy as np
x=np.array([1,2,3,4,5])
print(x)

# Create a 2-D arrays Containing 2 Arrays with cetain values.
import numpy as np
x=np.array([[1,2,3],[4,5,6]])
print(x)

# Now we wil create 3-D array with two 2-D array.
import numpy as np
x=np.array([[[1,2,3],[4,5,6]],[[1,2,3],[4,5,6]]])
print(x)

# Check how many dimensions the array have : ndim attribute
import numpy as np
a=np.array(42)
b=np.array([1,2,3,4,5])
c=np.array([[1,2,3],[4,5,6]])
d=np.array([[[1,2,3],[4,5,6]],[[1,2,3],[4,5,6]]])
print(a.ndim)
print(b.ndim)
print(c.ndim)
print(d.ndim)

# Create an array with 5 dimensions and veify that it has 5 dimensions
import numpy as np
x=np.array([1,2,3,4,5], ndmin=5)
print(x)
print('number of dimensions: ', x.ndim)
