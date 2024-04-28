# what is set ? :  a set is a collection of unique elements.

# for creating the set we use  numpy's unique() method to find the unique elements from any array:
# here we will convert teh array with repeated elements o a set 
import numpy  as np
x=np.array([1,1,1,1,2,3,44,4,5,5,5,6,7])
y=np.unique(x)
print(y)

# to fins the unique values of 2 1d Arrys , we will use union1d() method
import  numpy as np
x=np.array([1,1,1,2,2,3,4,55,5,5])
y=np.array([1,1,1,2,2,2,3,3,4,4,5,6])
z=np.union1d(x,y)
print(z)

# to find the on;y vales that are present in both array, we will use intersect1d()
import numpy as np
x=np.array([1,2,3,4])
y=np.array([3,4,5,6])
z=np.intersect1d(x,y,assume_unique=True)
print(z)

# to find the only values that are in 1st set and NOT present in the 2nd set: use setdiff1d()
import numpy as np
x=np.array([1,2,3,4])
y=np.array([3,4,5,6])
z=np.setdiff1d(x,y,assume_unique=True)
print(z)

# to find the only values that are not present in both the sides we will used setxor1d() method
import numpy as np
x=np.array([1,2,3,4])
y=np.array([3,4,5,6])
z=np.setxor1d(x,y)
print(z)