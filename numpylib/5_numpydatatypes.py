# data types in python: string,int,float,boolean and complex.
# data types in numpy 
# i for integer
# b for boolean
# u for unsigned integer
# f for float 
# c for complex float 
# m for timedelta
# M for date time
# O for Object
# S for string
# U for unicode string
# V - memory

# checking the data type of numpy array - dtype
import numpy as np
x= np.array([1,2,3,4])
print(x.dtype)

# checking the data type of numpy array - string
import numpy as np
x= np.array(['Apple','banana','cherry'])
print(x.dtype)

# creating array with a defined data type: 

import numpy as np
x= np.array([1,2,3,4],dtype='S')
print(x)
print(x.dtype)

# Now we will create an array with data type of 4 byte integer
import numpy as np
x= np.array([1,2,3,4],dtype='i4')
print(x)
print(x.dtype)

# if a type is given in which the elements cannot be casted then numpy will raise error, what if a value cannot be converted?
'''import numpy as np
x= np.array(['1','2','3','a'],dtype='i')
print(x)
print(x.dtype)'''

# Converting data type on existing array - astype()
import numpy as np
x= np.array([1.1,2.1,3.1])
y=x.astype('i')
print(y)
print(y.dtype)

# Converting data type from integer to boolean
import numpy as np
x= np.array([1,0,3])
y=x.astype(bool)
print(y)
print(y.dtype)
