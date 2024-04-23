# Permutation refers to an arrangement of elements like [3,2,1] i spermutation of [1,2,3] and vice versa.
# the numpy random module provides 2 methods : shuffle() and permutation().

# now we will randomly shuffle elements for the bellow array
# shuffle() method make changes to the original array
from numpy import random
import numpy as np
x= np.array([1,2,3,4,5])
random.shuffle(x)
print(x) 

# now we will generate a permutation of an elements for the below array
# the permutation method leaves the original array unchanged.
from numpy import random
import numpy as np
x= np.array([1,2,3,4,5])
print(random.permutation(x)) 