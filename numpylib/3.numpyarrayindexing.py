# 1-D Array indexing is athe same as accessing an array emenets. 
# start with 0, second 1

import numpy as np
x=np.array([1,2,3,4])
print(x[1])

# we can get the third and fourth elements from addding them
import numpy as np
x=np.array([1,2,3,4])
print(x[2]+x[3])

# Accesing the 2-D - it is like a rows and columns.
import numpy as np
x=np.array([[1,2,3,4,5],[6,7,8,9,10]])
print('2nd element in the first rows', x[0][1])
print(x[1][4])

# Accessing the 3-D - same as accessing 
import numpy as np
x=np.array([[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]]])
# print(x[0][1][2])
print(x[0,1,2])
