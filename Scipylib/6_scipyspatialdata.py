# Working with spatial data : it refers to data that as represented in a geometric space.
# Tringulation : one method to generate these tringulation through teh point is delaunay() tringulation.
# here now we will create a tringulation from some points:
'''import numpy as np
from scipy.spatial import Delaunay
import matplotlib.pyplot as plt

x= np.array([[2,4],[3,4],[3,0],[2,2],[4,1]])
simplices=Delaunay(x).simplices
plt.triplot(x[:,0], x[:,1], simplices)
plt.scatter(x[:,0], x[:,1], color='r')
plt.show()

# Convex HULL :  it is basically the smallest poligon that covers all of the given point:
import numpy as np
from scipy.spatial import ConvexHull
import matplotlib.pyplot as plt
x= np.array([[2,4],[3,4],[3,0],[2,2],[4,1],[1,2],[5,0],[3,1],[1,2],[0,2]])
hull = ConvexHull(x)
hull_points=hull.simplices
plt.scatter(x[:,0], x[:,1])
for simplex in hull_points:
    plt.plot(x[simplex,0],x[simplex,1], 'k-')
plt.show()'''

# KDTrees : they are a data structure optimized for the nearest neighbour queries.

from scipy.spatial import KDTree
x=[(1,-1),(2,3),(-2,3),(2,-3)]
tree=KDTree(x)
res= tree.query((1,1))
print(res)

# Distance matrix:  it is used to find the various types of distance between twopointsthere are basically 2 types: Euclidean Distance, Cosine Distance.
#Euclidean Distance : 
from scipy.spatial.distance import euclidean
p1=(1,0)
p2=(10,2)
x=euclidean(p1,p2)
print(x)


# Cosine Distance : 
from scipy.spatial.distance import cosine
p1=(1,0)
p2=(10,2)
x=cosine(p1,p2)
print(x)