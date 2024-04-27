# finding GCD(Greatest common denominotor), also know as HCF(Highest Common Factor)

# here we will find the HCF of the below 2 numbers:
import numpy as np
x=6
y=9
z=np.gcd(x,y)
print(z) # asswer will be 3 beacuse that is the highest number and both number can ber divided by (6/3=2 and 9/3=3)

# finding the GCD in an array
import numpy as np

x=np.array([10,16,18,40,100])
y=np.gcd.reduce(x)
print(y)
# it will return 2 because 2 is the highest number of al values that can be divided in between array.