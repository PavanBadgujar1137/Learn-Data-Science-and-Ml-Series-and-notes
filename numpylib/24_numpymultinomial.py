# Multinomial dist : it is a generalization of binomial dist.
# parameter - n(number of outcome or possibility), pvals(list of possibilities or outcomes), size(shape or outcomesreturned array)
# Draw out sample fro dice roll

from  numpy import random
x=random.multinomial(n=6, pvals=[1/6,1/6,1/6,1/6,1/6,1/6])
print(x)

# multinomial samples will not produce a single value, they will produce one value for each pvals..