# Rayleigh Dist: it is used in signal processing .
# param - scale(standard deviation,how flat the distribution , default is 1.0),size

# smaple for El with sacle of 2.0 with size of(2,3)
from numpy import random
x=random.rayleigh(scale=2, size=(2,3))
print(x)

# visualization of Rayleigh dist
from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns
sns.distplot(random.rayleigh(size=1000), hist=False)
plt.show()