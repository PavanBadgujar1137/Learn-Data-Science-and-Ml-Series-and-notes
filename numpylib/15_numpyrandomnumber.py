# Random meaning - something that cannot be predicted logically.
# Now we will generate a random number from 0 to 100

from numpy import random
x=random.randint(100)
print(x)

# you can also generate float() via rand() from 0 to 1
from numpy import random 
x=random.rand()
print(x)

# you can also generate random array.
# we will generate a 1-D containing 5 int from 0 to 100
from numpy import random
x=random.randint(100, size=(5))
print(x)

# you can also generate random array.
# we will generate a 2-D array with 3 rows, each row containing 5 int from 0 to 100
from numpy import random
x=random.randint(100, size=(3,5))
print(x)

# you can also generate random array.
# we will generate a 1-D aray containing 5 random float:
from numpy import random
x=random.rand(5)
print(x)

# you can also generate random array.
# we will generate a 2-D array with 3 rows, each row containing 5 float
from numpy import random
x=random.rand(3,5)
print(x)

# you can also generate random numbers from an array 
# choice()
from numpy import random
x=random.choice([3,5,7,9,1,4,6])
print(x)

# you can also generate random numbers from an 2-D array 
# choice()
from numpy import random
x=random.choice([3,5,7,9,1,4,6], size=(3,5))
print(x)

