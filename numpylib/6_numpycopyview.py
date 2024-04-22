# difference between numpy array copy vs view.
# we will make a copy, change in original array, and display both.

import numpy as np
x=np.array([1,2,3,4,5])
y=x.copy()
x[0]=42
print(x)
print(y)

# Now we will make view, change original, display both
import numpy as np
x=np.array([1,2,3,4,5])
y=x.view()
x[0]=42
print(x)
print(y)

