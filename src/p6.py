# Greg Howard & Srikanth Bonkuri

import pandas as pd
from sklearn.decomposition import PCA
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import StandardScaler
from bioinfokit.visuz import cluster

df = pd.read_csv('data/example.csv')
df.drop(df.columns[[0]], axis=1, inplace=True)

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

# Capture the loadings and plot the correlation matrix for these
loadings = pca.components_
for loading in loadings:
    for load in loading:
        load = round(load, 2)
count_pc = pca.n_features_
pc_list = ['PC' + str(i) for i in x_array]
loadings_df = pd.DataFrame.from_dict(dict(zip(pc_list, loadings)))
loadings_df['variable'] = df.columns.values
loadings_df = loadings_df.set_index('variable')
ax = sns.heatmap(loadings_df, annot=True, cmap=sns.diverging_palette(5, 250, n=200))
fig = ax.get_figure()
fig.subplots_adjust(left=0.24)
fig.subplots_adjust(right=1)
plt.title('Correlation matrix plot for loadings')
plt.savefig('figs/Correlation_Matrix.png')
'''
Possible add on if time allows for troubleshooting:
plt.cla()
plt.clf()

# Get the pc scores for 4 components and plot these in a 2D biplot
pca4 = PCA(4).fit(standardized_X)
print(type(pca4))
cluster.biplot(cscore=pca4, loadings=loadings, labels=df.columns.values, var1=round(var_explained[0][0]*100, 2), var2=round(var_explained[0][1]*100, 2))
plt.title('2D PCA Biplot')
plt.savefig('figs/2D_PCA_Biplot.png')
'''