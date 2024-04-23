# Searching array - you can serach for a certain value and return indexes that get the match by using where.
import numpy as np
x=np.array([1,2,3,4,5,4,4])
y= np.where(x==4)
print(y)

# now we will find the indexes where the values are even:
x=np.array([1,2,3,4,5,6,7,8])
y=np.where(x%2==0)
print(y)


# now we will find the indexes where the values are odd:
x=np.array([1,2,3,4,5,6,7,8])
y=np.where(x%2!=0)
print(y)

# searchsorted() - performed binary search in array.
# we will find the index where the value 7 should be inserted.
import numpy as np
x=np.array([6,7,8,9])
y=np.searchsorted(x,7)
print(y)

# now we weill search from right side
import numpy as np
x=np.array([6,7,8,9])
y=np.searchsorted(x,7,side='right')
print(y)

# How to search multiple values:
import numpy as np
x=np.array([6,7,8,9])
y=np.searchsorted(x, [2,4,5,10])
print(y)
