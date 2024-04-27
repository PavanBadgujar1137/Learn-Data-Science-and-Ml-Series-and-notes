# to create your own ufynction you have to defined a function like you do in normal functions in python, then you add it to the numpy function with frompyfunc() method.
# argument of formpyfunc() : function, inputs, outputs

# Create you own ufunc for additonal
import numpy as np
def myadd(x,y):
    return x+y

myadd= np.frompyfunc(myadd, 2,1)
print(myadd([1,2,3,4],[5,6,7,8]))

# checking if this function is ufunction or not :
import numpy as np
print(type(np.add))

# concatenate()
import numpy as np
print(type(np.concatenate))

# what if ufunction does not exist
# print(type(np.addwew))

# used ab if statement to check if the function a ufunction or not
import numpy as np
if type(np.add) == np.ufunc:
   print('yes , this function if ufunction ')
else:
    print('this function is not ufunction')


