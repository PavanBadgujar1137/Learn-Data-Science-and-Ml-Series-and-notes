# Zipf Dist: its defination like a common word in english has occurs nearly 1/5 time as of the most hindi words.
# param - a(dist param), size
# sample for zipf dist with a as z with size 2*3
from numpy import random
x=random.zipf(a=2,size=(2,3))
print(x)

# visualization of zip dist
from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns
x=random.zipf(a=2,size=1000)
sns.distplot(x[x<10],kde=False)
plt.show()
