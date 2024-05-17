# Normal Data Dist (Bell Curve Graph): In numpy probabiliitiy theory this kind of data list is known as normal data dist or Gaussian Data Dist,  where the values are concentrated around a given value
# a example of normal data dist:
import numpy as np
import matplotlib.pyplot as plt
x=np.random.normal(5.0,1.0, 100000)
plt.hist(x, 100)
plt.show()

#a normal data dist is also known as bell curve because of its bell shape.