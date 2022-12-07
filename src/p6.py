# Greg Howard & Srikanth Bonkuri

import pandas as pd
from sklearn.decomposition import PCA
import numpy as np
import matplotlib.pyplot as plt
import math

df = pd.read_csv('../data/example.csv')



df.drop(df.columns[[0]], axis=1, inplace=True)

X = df
print(X)

# Using the elbow method to find the optimal number of clusters
from sklearn.cluster import KMeans
wcss = []   # 
for i in range(1, 11):
    kmeans = KMeans(n_clusters = i, init = 'k-means++', random_state = 42)
    kmeans.fit(X)
    wcss.append(kmeans.inertia_)
plt.plot(range(1, 11), wcss)
plt.title('The Elbow Method')
plt.xlabel('Number of clusters')
plt.ylabel('WCSS')
plt.show()

plt.cla()   # Clear axis
plt.clf() 


kmeans = KMeans(n_clusters = 4, init = 'k-means++', random_state = 42)
y_kmeans = kmeans.fit_predict(X)

print(y_kmeans)



# Visualising the clusters

plt.scatter(X["Area"][y_kmeans == 0], X["White Pixel Count"][y_kmeans == 0], s = 20, c = 'red', label = 'Cluster 1')
plt.scatter(X["Area"][y_kmeans == 1], X["White Pixel Count"][y_kmeans == 1], s = 20, c = 'blue', label = 'Cluster 2')
plt.scatter(X["Area"][y_kmeans == 2], X["White Pixel Count"][y_kmeans == 2], s = 20, c = 'green', label = 'Cluster 3')
plt.scatter(X["Area"][y_kmeans == 3], X["White Pixel Count"][y_kmeans == 3], s = 20, c = 'cyan', label = 'Cluster 4')

plt.scatter(kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:, 1], s = 50, c = 'black', label = 'Centroids')

plt.title('Clusters of cells')
plt.xlabel('Area (sq.pixel)')
plt.ylabel('White Pixel Count (1-100)')
plt.legend()
plt.show()

plt.savefig('../figs/Cell_Cluster_Kmeans.png')

# Try this
'''
# Plot the data with K Means Labels
from sklearn.cluster import KMeans
kmeans = KMeans(4, random_state=0)
labels = kmeans.fit(X).predict(X)
plt.scatter(X[:, 0], X[:, 1], c=labels, s=40, cmap='viridis')
'''

# Optional as to whether we want to try to visualize the clusters with hyper-spheres
# May not work well if our clusters are elliptical, rather than circular
# GMM may be better: https://github.com/jakevdp/PythonDataScienceHandbook/blob/master/notebooks/05.12-Gaussian-Mixtures.ipynb
'''
from scipy.spatial.distance import cdist

def plot_kmeans(kmeans, X, n_clusters=4, rseed=0, ax=None):
    labels = kmeans.fit_predict(X)

    # plot the input data
    ax = ax or plt.gca()
    ax.axis('equal')
    ax.scatter(X[:, 0], X[:, 1], c=labels, s=40, cmap='viridis', zorder=2)

    # plot the representation of the KMeans model
    centers = kmeans.cluster_centers_
    radii = [cdist(X[labels == i], [center]).max()
             for i, center in enumerate(centers)]
    for c, r in zip(centers, radii):
        ax.add_patch(plt.Circle(c, r, fc='#CCCCCC', lw=3, alpha=0.5, zorder=1))
    
kmeans = KMeans(n_clusters=4, random_state=0)
plot_kmeans(kmeans, X)
'''