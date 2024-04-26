# Exponential dist : it is used fro describing the time till next event that is like failure or success.
# param - scale(inverse of rate(see lam poission dist..))
# here we will draw a sample for exponential dist with 2.0 scale and *3 size
from numpy import random
x=random.exponential(scale=2, size=(2,3))
print(x)

# visualization of exponential dist
from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns
sns.distplot(random.exponential(size=1000),label='Exponential',hist=False)
plt.show()

