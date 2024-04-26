#  binomial dist - discrete dist - binary output.
# param - n(nummber of tials), p(probability), size(shape-return array)

# given 10 trials for a coin which will generate 10 data points:
'''
from numpy import random
x=random.binomial(n=10, p=0.5, size=10)
print(x)

# visulization of binomial distribution
from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns
sns.displot(random.binomial(n=10, p=0.5, size=1000),kde=False)
plt.show() '''

# Difference between normal and binomial - normal(continues) and binomial(discrete)
# I Use 500 data point for binomial and under 100 data point for normal dist.
from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns
sns.distplot(random.normal(loc=50, scale=5, size=1000), hist=False , label='normal' )
sns.distplot(random.binomial(n=100,p=0.5,size=500),hist=False, label='Binomial')
plt.show()