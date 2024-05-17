# what are Percentile? :                                                              
ages = [5,31,43,48,50,41,7,11,15,39,80,82,32,2,8,6,25,36,27,61,31]
# the numpy module has a method for finding thr specified percentile:
import numpy as np
ages = [5,31,43,48,50,41,7,11,15,39,80,82,32,2,8,6,25,36,27,61,31]
x=np.percentile(ages,75)
print(x)

# what is the age of 90% people younger than ?
import numpy as np
ages = [5,31,43,48,50,41,7,11,15,39,80,82,32,2,8,6,25,36,27,61,31]
x=np.percentile(ages,90)
print(x)