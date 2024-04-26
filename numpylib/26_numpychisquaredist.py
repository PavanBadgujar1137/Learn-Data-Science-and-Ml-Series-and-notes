# Chi Square Dist : it is basicaaly used for verify the hypothesis.
# param - df(degree of freedom), size

# sample for chi square dis with df 2 with size 2*3
from numpy import random
x=random.chisquare(df=2, size=(2,3))
print(x)

# visualization of chi square
from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns
sns.distplot(random.chisquare(df=1,size=1000), hist=False)
plt.show()