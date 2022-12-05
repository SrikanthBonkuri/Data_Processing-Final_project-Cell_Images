# Greg Howard & Srikanth Bonkuri

import pandas as pd
from sklearn.decomposition import PCA
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import StandardScaler

df = pd.read_csv('data/example.csv')

# Conduct principal components analysis
X = df
standardized_X = StandardScaler().fit_transform(X)
pca = PCA(n_components=8)
pca.fit(standardized_X)

print('PCA Mean: ' + str(pca.mean_[1:9]) + '\n')
print('PCA Explained Variance Ratio: ' + str(pca.explained_variance_ratio_)  + '\n')
print('Cumulative Proportion of Variance: ' + str(np.cumsum(pca.explained_variance_ratio_))  + '\n')

# Make a scree plot to visualize the number of factors to retain
x_array=[1, 2, 3, 4, 5, 6, 7, 8]
var_explained = pd.DataFrame(pca.explained_variance_ratio_)
sns.barplot(data=var_explained, x=x_array, y=pca.explained_variance_ratio_)
plt.xlabel('Factor')
plt.ylabel('Explained Variance Ratio')
plt.title('Explained Variance Ratio of Each Factor')
plt.savefig('figs/Explained_Variance_Ratio_by_Factor.png')
plt.cla()
plt.clf()

# Credit to Renesh Bedre for the fantastic guide linked below that provided a map for this section
# https://www.reneshbedre.com/blog/principal-component-analysis.html
loadings = pca.components_
count_pc = pca.n_features_
pc_list = ['PC' + str(i) for i in x_array]
loadings_df = pd.DataFrame.from_dict(dict(zip(pc_list, loadings)))
loadings_df['variable'] = df.columns.values
loadings_df = loadings_df.set_index('variable')
ax = sns.heatmap(loadings_df, annot=True, cmap='Spectral')
fig = ax.get_figure()
fig.subplots_adjust(left=0.24)
plt.title('Correlation matrix plot for loadings')
plt.savefig('figs/Correlation_Matrix.png')

'''clf = PCA(4)
X_trans = clf.fit_transform(standardized_X)

pca2 = PCA(2)
X_trans2 = pca2.fit_transform(standardized_X)
print(standardized_X.shape)
print(X_trans2.shape)'''
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
