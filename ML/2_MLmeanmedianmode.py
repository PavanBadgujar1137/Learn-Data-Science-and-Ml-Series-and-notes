# Data Set: [99,86,87,43,56,76,45,35,89,77]
# in ML and in Math also there are basically three values that are actually interset to us:
# Mean: the average value
# Meadian : the mid point value
# Mode:  the most common value.

# here in this example we have speed of 13 cars
speed=[99,86,87,43,56,76,45,35,89,77,44,33,22]

# Mean: to calculate the mean, sum all the values 
# sum of all speed/cars
import numpy as np
speed=[99,86,87,43,56,76,45,35,89,77,44,44,44]
x=np.mean(speed)
print(x) # 60.92 is its avg speed

# Median: here we will find the median value
y=np.median(speed)
print(y) # 56.0 is its median value

# mode : the value that appears most number of times: we wil use scipy mode
from scipy import stats
z=stats.mode(speed)
print(z)