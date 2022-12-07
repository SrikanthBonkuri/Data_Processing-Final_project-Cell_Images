# Greg Howard & Srikanth Bonkuri

import pandas as pd
from sklearn.decomposition import PCA
import numpy as np
import matplotlib.pyplot as plt
import math

df = pd.read_csv('data/example.csv')



df.drop(df.columns[[0]], axis=1, inplace=True)

X = df
print(X)

# Using the elbow method to find the optimal number of clusters
from sklearn.cluster import KMeans
wcss = []   # 
for i in range(1, 9):
    kmeans = KMeans(n_clusters = i, init = 'k-means++', random_state = 42)
    kmeans.fit(X)
    wcss.append(kmeans.inertia_)
plt.plot(range(1, 9), wcss)
plt.title('Elbow Plot on number of clusters')
plt.xlabel('Number of clusters')
plt.ylabel('WCSS')

plt.savefig('figs/Elbow_Plot_Kmeans.png')

plt.cla()   # Clear axis
plt.clf() 


kmeans = KMeans(n_clusters = 4, init = 'k-means++', random_state = 42)
y_kmeans = kmeans.fit_predict(X)



# Visualising the clusters

# Plot Data
fig, ax = plt.subplots(1, 2, figsize=(20, 9)) # Change code for figsize due to deprecation warning
fig.subplots_adjust(left=0.0625, right=0.9, wspace=0.1)

ax[0].scatter(X["Area"][y_kmeans == 0], X["White Percent Area"][y_kmeans == 0], s = 20, c = 'red', label = 'Cluster 1')
ax[0].scatter(X["Area"][y_kmeans == 1], X["White Percent Area"][y_kmeans == 1], s = 20, c = 'blue', label = 'Cluster 2')
ax[0].scatter(X["Area"][y_kmeans == 2], X["White Percent Area"][y_kmeans == 2], s = 20, c = 'green', label = 'Cluster 3')
ax[0].scatter(X["Area"][y_kmeans == 3], X["White Percent Area"][y_kmeans == 3], s = 20, c = 'cyan', label = 'Cluster 4')

ax[0].scatter(kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:, 1], s = 80, c = 'black', label = 'Centroid', alpha = 0.2)

ax[0].set_title('2D Plot of Clusters on Area by Percentage White')
ax[0].set_xlabel('Area')
ax[0].set_ylabel('White Percentage of Area')


ax[1].scatter(X["Circle Area"][y_kmeans == 0], X["Black Percent Circle"][y_kmeans == 0], s = 20, c = 'red', label = 'Cluster 1')
ax[1].scatter(X["Circle Area"][y_kmeans == 1], X["Black Percent Circle"][y_kmeans == 1], s = 20, c = 'blue', label = 'Cluster 2')
ax[1].scatter(X["Circle Area"][y_kmeans == 2], X["Black Percent Circle"][y_kmeans == 2], s = 20, c = 'green', label = 'Cluster 3')
ax[1].scatter(X["Circle Area"][y_kmeans == 3], X["Black Percent Circle"][y_kmeans == 3], s = 20, c = 'cyan', label = 'Cluster 4')

ax[1].scatter(kmeans.cluster_centers_[:, 6], kmeans.cluster_centers_[:, 7], s = 80, c = 'black', label = 'Centroid', alpha = 0.2)

ax[1].set_title('2D Plot of Clusters on Circle Area by Percentage Black')
ax[1].set_xlabel('Circle Area')
ax[1].set_ylabel('Black Percentage of Circle')
plt.legend(bbox_to_anchor=(1.18, 1))

plt.savefig('figs/Cell_Cluster_Kmeans(Circle Area vs Black Percent).png')
