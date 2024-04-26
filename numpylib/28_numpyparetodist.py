# pareto distribution - it is the ratio of 80:20 ratio. (20% factor Cause 80% outcome or result)
# param - a(shape para,),size

# sample for pareto dist with shape 2 size of (2*3)
from numpy import random
x= random.pareto(a=2,size=(2,3))
print(x)

# visualization of pareto dist
from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns
sns.distplot(random.pareto(a=2,size=1000),kde=False)
plt.show()