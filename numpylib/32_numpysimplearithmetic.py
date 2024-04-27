# arithmetic operstors : +, -, /, * 
# By using ufunction also take addition arguments like , where , dtype and out
# here now we will use add()
import numpy as np
x=np.array([10,11,12,13,14,15])
y=np.array([20,21,22,23,24,25])
z=np.add(x,y)
print(z)

# example of substracting the value
import numpy as np
x=np.array([10,11,12,13,14,15])
y=np.array([20,21,22,23,24,25])
z=np.subtract(x,y)
print(z)

# example of multiplication
import numpy as np
x=np.array([10,11,12,13,14,15])
y=np.array([20,21,22,23,24,25])
z=np.multiply(x,y)
print(z)

# example of division
import numpy as np
x=np.array([10,11,12,13,14,15])
y=np.array([20,21,22,23,24,25])
z=np.divide(x,y)
print(z)

# power() function raises the value from the 1st array to the power of the values of the second aray and return the resilts in the new array
import numpy as np
x=np.array([10,20,30,40,50,60])
y=np.array([3,4,5,2,5,6])
z=np.power(x,y)
print(z)

# remainder - mod() and  remainder() functions returns the reminder of the 1st array corresponding to the 2nd array, an result in the new array
import numpy as np
x=np.array([10,20,30,40,50,60])
y=np.array([3,5,7,2,5,9])
z=np.mod(x,y)
print(z)

# by using reminder(): boths answer are same
import numpy as np
x=np.array([10,20,30,40,50,60])
y=np.array([3,5,7,2,5,9])
z=np.remainder(x,y)
print(z)

# quotient and mod(reminder)
## the divmod() function return both the quotient and mod
import numpy as np
x=np.array([10,20,30,40,50,60])
y=np.array([3,5,7,2,5,9])
z=np.divmod(x,y)
print(z)

# absolute() and abs() - do he same operation but here we should use absolute() to avoid confusion with python inbuild function math.abs()
import numpy as np
x=np.array([-1,-2,-3,-4,-5])
y=np.absolute(x)
print(y)