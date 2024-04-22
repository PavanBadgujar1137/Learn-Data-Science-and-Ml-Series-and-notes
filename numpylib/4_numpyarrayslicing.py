# slicing array - divide in part part - slicing in python means taking elements from one given index to another index.
# [start:end],[start:end:step] 

# now we will slice an elemets from 1 to 5:
import numpy as np
x=np.array([1,2,3,4,5,6,7,8,9])
print(x[1:5])

# Now we will slice from index 4 to the end value
import numpy as np
x=np.array([1,2,3,4,5,6,7,8,9])
print(x[4:])

# now we will slice the element from the begining to index 4
import numpy as np
x=np.array([1,2,3,4,5,6,7,8,9])
print(x[:4])

# Negative slicing - index 3 to end 
import numpy as np
x=np.array([1,2,3,4,5,6,7])
print(x[-3:-1])

# step: you will use step value to determine the step of the slicing
# return every other value from index 1 to 5
import numpy as np
x=np.array([1,2,3,4,5,6,7])
print(x[1:5:2])

# now return every other number from the entire array
import numpy as np
x=np.array([1,2,3,4,5,6,7,8,9])
print(x[::3])

# slicing 2-D Array
import numpy as np
x=np.array([[1,2,3,4,5],[6,7,8,9,10]])
print(x[1,1:4])

# another example
import numpy as np
x=np.array([[1,2,3,4,5],[6,7,8,9,10]])
print(x[0:2,2])

# another example tough 2-D - print from both index 1:4
import numpy as np
x=np.array([[1,2,3,4,5],[6,7,8,9,10]])
print(x[0:2,1:4])