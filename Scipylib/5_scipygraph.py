# working with graphs: we have a module name sciy.sparse.csgraph
# adjacency Matrix:nxn matrix where n is the no of elements in graph.
# Connected Component :
import numpy as np
from scipy.sparse.csgraph import connected_components
from scipy.sparse import csr_matrix
x=np.array([[0,1,2],[1,0,0],[2,0,0]])
y=csr_matrix(x)
print(connected_components(y))

# Dijkstra method: for finding the shortest path in a graph from one element to another 
# it takes 3 arg: return_predecessors, indices, limit
# here we will find the shortest path from element 1 to 2:
import numpy as np
from scipy.sparse.csgraph import dijkstra
from scipy.sparse import csr_matrix
x=np.array([[0,1,2],[1,0,0],[2,0,0]])
y=csr_matrix(x)
print(dijkstra(y,return_predecessors=True, indices=0))

# Floyd Warshall() method : it is for finding the shortest path between all the pairs of elements.

import numpy as np
from scipy.sparse.csgraph import floyd_warshall
from scipy.sparse import csr_matrix
x=np.array([[0,1,2],[1,0,0],[2,0,0]])
y=csr_matrix(x)
print(floyd_warshall(y,return_predecessors=True))

# Bellman_ford() method:  it is for finding the shortest path between all the pairs of elements.but this method can handle negative wieght as well
import numpy as np
from scipy.sparse.csgraph import bellman_ford
from scipy.sparse import csr_matrix
x=np.array([[0,-1,2],[1,0,0],[2,0,0]])
y=csr_matrix(x)
print(bellman_ford(y,return_predecessors=True,indices=0))

# Depth first order:it return depth first traversal from a node: it has 2 arguments : the graph, starting element

import numpy as np
from scipy.sparse.csgraph import depth_first_order
from scipy.sparse import csr_matrix
x=np.array([[0,1,0,1],[1,1,1,1],[2,1,1,0],[0,1,0,1]])
y=csr_matrix(x)
print(depth_first_order(y,1))

# breadth_first_order() method : it returns the breadth from a node: it has 2 argu: the graph, starting elements
import numpy as np
from scipy.sparse.csgraph import breadth_first_order
from scipy.sparse import csr_matrix
x=np.array([[0,1,0,1],[1,1,1,1],[2,1,1,0],[0,1,0,1]])
y=csr_matrix(x)
print(breadth_first_order(y,1))