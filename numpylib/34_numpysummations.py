# summations : difference : addition is done between two argiuments whereas summation happpens over an element.

# addition the 2 array
import numpy as np
x=np.array([1,2,3])
y=np.array([1,2,3])
z=np.add(x,y)
print(z)


# sum the values in 2 arrayss
import numpy as np
x=np.array([1,2,3])
y=np.array([1,2,3])
z=np.sum([x,y])
print(z)

# summation over an axis : if you specify axis = 1, numpy will sum the number in each array.
import numpy as np
x=np.array([1,2,3])
y=np.array([1,2,3])
z=np.sum([x,y], axis=1)
print(z)

# cummulative sum: means partially adding the element in array.
# example:  [1,2,3,4] would be [1,1+2,1+2+3,1+2+3+4]- [1,3,6,10] represent by cumsum()
import numpy as np
x=np.array([1,2,3])
y=np.cumsum(x)
print(y)