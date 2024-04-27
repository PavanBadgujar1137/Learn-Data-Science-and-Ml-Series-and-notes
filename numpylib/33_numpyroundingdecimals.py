# Rounding decimals ; there are 5 ways of rounding of the decimals in numpy: 
# truncation
# fix
# rounding 
# floor
# ceil

# truncations : trunc() and fix()
# here we are truncating the below array, these commands remove the decimals and return the float number closest to zero.
import numpy as np
x=np.trunc([-3.1666, 3.6667])
print(x)

# fix() example : remove the decimal point
import numpy as np
x=np.fix([-3.1666, 3.6667])
print(x)

# rounding: the around() function increments preceding digit or decimal by nearest to 1 : if n>5 = 1 or n<5 =0
import numpy as np
x=np.around(4.366,2)
print(x)

# floor() - round off decimals to the lower integer.
import numpy as np
x=np.floor([3.1666, 3.6667])
print(x)

# ceil() - round off decimals to the upper integer.
import numpy as np
x=np.ceil([-3.1666, 3.6667])
print(x)