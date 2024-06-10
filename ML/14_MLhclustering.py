# Hierarchical Clustering: It is an Unsupersvised learning method for clusteringdata points. the algorithm builds clusters by measuring the disimilarities between data.
# example of the same:
# three lines to make our compiler able to draw .
'''import numpy as np
import matplotlib.pyplot as plt

x = [4,5,10,4,3,11,14,6,10,12]
y = [21,19,24,17,16,25,24,22,21,21]
plt.scatter(x,y)
plt.show

# now we wil compute the ward linkage method using euclidean distance and visualize it using the dendogram.
import numpy as np
import matplotlib.pyplot as plt
from scipy.cluster.hierarchy import dendrogram,linkage

x = [4,5,10,4,3,11,14,6,10,12]
y = [21,19,24,17,16,25,24,22,21,21]
data=list(zip(x,y))
linkage_data=linkage(data, method='ward', metric='euclidean')
dendrogram(linkage_data)
plt.show()'''

# Yes , we can do the same thing the python scikit-learn, and visualize on a 2-D plot.
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import AgglomerativeClustering

# Data points
x = [4, 5, 10, 4, 3, 11, 14, 6, 10, 12]
y = [21, 19, 24, 17, 16, 25, 24, 22, 21, 21]
data = list(zip(x, y)) # Turn the data into set of points

# Hierarchical clustering
hierarchical_clustering = AgglomerativeClustering(n_clusters=2, metric='euclidean', linkage='ward')
labels = hierarchical_clustering.fit_predict(data) # This fit_predict method can be called on the data to compute the cluster using to define

# Plot the clusters
plt.scatter(x, y, c=labels, cmap='viridis')
plt.title('Hierarchical Clustering')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.colorbar(label='Cluster Label')
plt.show()


