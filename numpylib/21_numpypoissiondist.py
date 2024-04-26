# poission Dist - it estimate how many time an event can happen.
#  param - lam(number of occurenece or rate ), size
# generate a random 1*10 dist for the occurence 2
'''from numpy import random
x=random.poisson(lam=2, size=10)
print(x)

# Visualization of poission dist
from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns
sns.displot(random.poisson(lam=2, size=1000),kde=False)
plt.show()'''

#presenting both the plots in same figure normal and poission dist
from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns

sns.distplot(random.normal(loc=50, scale=7, size=1000), label='Normal', hist=False)
sns.distplot(random.poisson(lam=2, size=1000), label='Poisson', hist=False)
plt.legend()
plt.show()

# n*p == lam(no of ocurrence)
