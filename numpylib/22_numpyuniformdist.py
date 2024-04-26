# uniform dist - it is only need for probability
# param - a(lower bound 0.0), b(upper bound 1.0) , size 
 
from numpy import  random
x=random.uniform(size=(2,3))
print(x)

# visualization of uniform dist
from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns
sns.distplot(random.uniform(size=1000),hist=False,label='Uniform')
plt.legend()
plt.show()
