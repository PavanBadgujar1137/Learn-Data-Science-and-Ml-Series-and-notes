# Data Distribution: How do we get big data set?
# here now we will create a array containing 250 random floats betweeen 0.0 to 5.0
import numpy as np
x=np.random.uniform(0.0, 5.0,250)
print(x)

# to visualize the big data set we can draw a histogram with the data we got:
# here we will use python module matplotlib
import numpy as np
import matplotlib.pyplot as plt
x=np.random.uniform(0.0, 5.0,250)
plt.hist(x,5)
plt.show()

# Big Data Distribution 
# now we will create an array with 100000 random numbers and display them uaing tthe hist with 100 bars.
import numpy as np
import matplotlib.pyplot as plt
x=np.random.uniform(0.0, 5.0,100000)
plt.hist(x,10000)
plt.show()