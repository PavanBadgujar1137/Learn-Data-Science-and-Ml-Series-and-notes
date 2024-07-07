# Creating a simple K-means Clustering model Using Python
import matplotlib.pyplot as plt
import numpy as np
from sklearn.datasets import make_blobs
from sklearn.cluster import KMeans

# step 2 : use make_blobs to generate data
X, y = make_blobs(n_samples=300, centers=4, random_state=42)

# step 3 : now we create KMeans instance with 4 clusters using KMeans
Kmeans = KMeans(n_clusters=4)

# step 4 : fitting 
Kmeans.fit(X)

# step 5 :
cluster_center= Kmeans.cluster_centers_
labels = Kmeans.labels_

plt.scatter(X[:,0], X[:,1], c=labels,  cmap='viridis')
plt.scatter(cluster_center[:,0],cluster_center[:,1], marker='x', s=300, c='red')
plt.xlabel('Feature 1')
plt.ylabel('Feature 2')
plt.title('K-Means Clustering')
plt.show()
