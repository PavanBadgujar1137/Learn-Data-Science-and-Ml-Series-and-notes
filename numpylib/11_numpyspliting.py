# spliting arrays in numpy - it is reverse to joining, breaking the array.
# array_split()

# split the array in 3 parts:
import numpy as np
x=np.array([1,2,3,4,5,6])
y=np.array_split(x,3)
print(y)

# Now we will split this array in 4 parts
import numpy as np
x=np.array([1,2,3,4,5,6])
y=np.array_split(x,4)
print(y)

# split into array with index
import numpy as np
x=np.array([1,2,3,4,5,6])
y=np.array_split(x,3)
print(y[0])
print(y[1])
print(y[2])

# Splitting the 2-D array
import numpy as np
x=np.array([[1,2],[3,4],[5,6],[7,8],[9,10],[11,12]])
y=np.array_split(x,3)
print(y)

# split the 2-D array into three 2-D array
import numpy as np
x=np.array([[1,2,3],[3,4,4],[5,6,5],[7,8,6],[9,10,7],[11,12,8]])
y=np.array_split(x,3)
print(y)

# spliting the 2-D into three 2-D along with rows
import numpy as np
x=np.array([[1,2,3],[3,4,4],[5,6,5],[7,8,6],[9,10,7],[11,12,8]])
y=np.array_split(x,3,axis=1)
print(y)

# alternate solutopn is using the hsplit(), opposite hstack()
import numpy as np
x=np.array([[1,2,3],[3,4,4],[5,6,5],[7,8,6],[9,10,7],[11,12,8]])
y=np.hsplit(x,3)
print(y)

