# Getting some elements out of an existing array and creating new array is called filtering.
# a boolean index list is a list of boolean corresponding to indexes in the array.(True and False)
# create an array from the element on index 0 to 2:
import numpy as np
x=np.array([41,42,43,44])
y=[True,False,True,False]
z=x[y]
print(z)

# now we will create a filter array
# that will return only values higher than 42.
import numpy as np
x=np.array([41,42,43,44])
y=[]
for i in x:
    if i>42:
        y.append(True)
    else:
        y.append(False)

z=x[y]
print(y)
print(z)

# Create a filter array that will return only even elements from the original array.
import numpy as np
x=np.array([1,2,3,4,5,6,7])
y=[]
for i in x:
    if i%2==0:
        y.append(True)
    else:
        y.append(False)

z=x[y]
print(y)
print(z)

# Yes, you can also create filter directly from array
# that will return only values higher than 42.
import numpy as np
x=np.array([41,42,43,44])
y=x>42
z=x[y]
print(y)
print(z)

# Create a filter array that will return only even elements from the original array.
# Yes, you can also create filter directly from array
# that will return only values higher than 42.
import numpy as np
x=np.array([41,42,43,44])
y=x%2==0
z=x[y]
print(y)
print(z)