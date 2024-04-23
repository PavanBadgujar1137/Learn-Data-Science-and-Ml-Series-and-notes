# sort() - The numpy ndarray object has a function which is called sort(), and this will sort a specified array.
import numpy as np
x=np.array([3,2,0,1])
print(np.sort(x)) # This method like the copy() wont we change in original aray

# sort the array alphabetical
import numpy as np
x=np.array(["Apple","Cherrey","Banana"])
print(np.sort(x))

# Sort the boolean arrays:
import numpy as np
x=np.array([True,False,True])
print(np.sort(x))

# sort the 2-D array
import numpy as np
x=np.array([[3,2,4],[5,0,1]])
print(np.sort(x))
