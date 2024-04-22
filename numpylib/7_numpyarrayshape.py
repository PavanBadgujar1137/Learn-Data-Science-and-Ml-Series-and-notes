# shape of an array - the shape of an array is the no of elemenets in each dimention.
# Now we wll try to get the shape of an array.
import numpy as np
x=np.array([[1,2,3,4],[5,6,7,8]])
print(x.shape)

# (2,4) which means the array has 2 dimensions and it has 4 elements

# now we will create a 5-D array using ndmin
import numpy as np
x=np.array([1,2,3,4],ndmin=5)
print(x)
print('shape of array is ', x.shape)
