# iterating array - means going through the elements one by one or step by step. like for loop.

# iterate the element of 1-D 
import numpy as np
x=np.array([1,2,3])
for i in x:
    print(i)

# iterate the elements of 2-D
import numpy as np
x=np.array([[1,2,3],[4,5,6]])
for i in x:
    print(i)

# iterate on each scaler element of the 2-D
import numpy as np
x=np.array([[1,2,3],[4,5,6]])
for i in x:
    for j in i:
        print(j)

# Iterate a 3-D
import numpy as np
x=np.array([[[1,2,3],[4,5,6],[7,8,9],[10,11,12]]])
for i in x:
    for j in i:
        for k in j:
            print(k)

# Iterating arrays using the nditer() function
# Now we will iterate on each scalar element.
import numpy as np
x=np.array([[[1,2],[3,4],[5,6],[7,8]]])
for i in np.nditer(x):
    print(i)

# now we will iterarate with different sizes
import numpy as np
# Create a 2D array
x = np.array([[1, 2, 3,4,5,6],
              [4, 5, 6,7,8,9]])

# Iterate over selected elements of the array
for i in np.nditer(x[:, ::2]):
    print(i)
