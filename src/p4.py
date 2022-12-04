# Greg Howard & Srikanth Bonkuri

import pandas as pd
from sklearn.decomposition import PCA
import numpy as np
import matplotlib.pyplot as plt
import math

df = pd.read_csv('data/example.csv')

print(df)

# Conduct principal components analysis
X = df
pca = PCA(n_components=8)
pca.fit(X)
print('PCA Mean: ' + str(pca.mean_[1:9]))
print('PCA Explained Variance Ratio: ' + str(pca.explained_variance_ratio_))
print() # New line

# Plot Data
fig, ax = plt.subplots(1, 2, figsize=(16, 6)) # Change code for figsize due to deprecation warning
fig.subplots_adjust(left=0.0625, right=0.95, wspace=0.1)

# Show that the brightness of a cell increases with the size
X['% White'] = round(X['White Pixel Count'] / X['Area'] * 100, 2)

ax[0].scatter(X['Area'], X['% White'], alpha=0.2)
ax[0].set_title('Cell Area by Percentage White')
ax[0].set_xlabel('Total Pixel Count')
ax[0].set_ylabel('Percentage of White Pixels')

# Calculate Log Data
def log_function(x):
    return math.log(x)

X['log_Area'] = X['Area'].transform(log_function)

# Show the logorithmic relationship
ax[1].scatter(X['log_Area'], X['% White'], alpha=0.2)
ax[1].set_title('log(Cell Area) by Percentage White')
ax[1].set_xlabel('log(Total Pixel Count)')
ax[1].set_ylabel('Percentage of White Pixels')

plt.savefig('figs/Cell_Area_by_Percentage_White.png')



# Plot principal components
'''
# Use the draw vector function for our plot
def draw_vector(v0, v1, ax=None):
    ax = ax or plt.gca()
    arrowprops=dict(arrowstyle='->',
                    linewidth=2,
                    shrinkA=0, shrinkB=0)
    ax.annotate('', v1, v0, arrowprops=arrowprops)

fig, ax = plt.subplots(1, 2, figsize=(16, 6)) # Change code for figsize due to deprecation warning
fig.subplots_adjust(left=0.0625, right=0.95, wspace=0.1)

ax[0].scatter(X['Area'], X['% White'], alpha=0.2)
for length in pca.explained_variance_:
    print(length)
for vector in pca.components_:
    print(vector)
print(zip(pca.explained_variance_, pca.components_))
for length, vector in zip(pca.explained_variance_, pca.components_):
    v = vector * 3 * np.sqrt(length)
    draw_vector(pca.mean_, pca.mean_ + v, ax=ax[0])
#ax[0].axis('equal')
ax[0].set(xlabel='Area', ylabel='Percent of White Pixels', title='input')

X_pca = pca.transform(X)
ax[1].scatter(X_pca[:, 0], X_pca[:, 1], alpha=0.2)
draw_vector([0, 0], [0, 3], ax=ax[1])
draw_vector([0, 0], [3, 0], ax=ax[1])
ax[1].axis('equal')
ax[1].set(xlabel='component 1', ylabel='component 2',
          title='principal components',
          xlim=(-5, 5), ylim=(-3, 3.1))'''

# Try this K based on what seems optimal from PCA
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