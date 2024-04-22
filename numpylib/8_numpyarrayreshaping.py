# reshaping - means changing the shape of an array , like adding and removing the elements.

# reshaping from 1-D to 2-D
import numpy as np
x=np.array([1,2,3,4,5,6,7,8,9,10,11,12])
y=x.reshape(4,3)
print(y)

# reshaping from 1-D to 3-D
import numpy as np
x=np.array([1,2,3,4,5,6,7,8,9,10,11,12])
y=x.reshape(2,3,2)
print(y)

# reshaping from 1-D to 3-D
'''import numpy as np
x=np.array([1,2,3,4,5,6,7,8])
y=x.reshape(3,3)
print(y)''' #  in here we cant directly devide the given array hat time we have got error remid this thing.

# Return copy or view
import numpy as np
x=np.array([1,2,3,4,5,6,7,8])
print(x.reshape(2,4).base) # view showing a original document

# unknown dimension - you are only allowed to have one unknown dimension. pass -1.

import numpy as np
x=np.array([1,2,3,4,5,6,7,8])
y=x.reshape(2,2,-1)

# Flattening the array by converting multidimentional array in 1-D.
import numpy as np
x=np.array([[1,2,3],[4,5,6]])
y=x.reshape(-1)
print(y)

# there are alot of functions for changing the shape pf an array in numpy. like flatten, ravel and also rearranging the element rot90, flip,fliplr,flipud, they all are actually comes under advanced numpy.

