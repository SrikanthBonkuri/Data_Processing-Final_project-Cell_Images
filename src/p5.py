# Greg Howard & Srikanth Bonkuri

import pandas as pd
from sklearn.decomposition import PCA
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import StandardScaler

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

# Credit to Renesh Bedre for the fantastic guide linked below that provided a map for this section
# https://www.reneshbedre.com/blog/principal-component-analysis.html
loadings = pca.components_
for loading in loadings:
    for load in loading:
        load = round(load, 2)
count_pc = pca.n_features_
pc_list = ['PC' + str(i) for i in x_array]
loadings_df = pd.DataFrame.from_dict(dict(zip(pc_list, loadings)))
loadings_df['variable'] = df.columns.values
loadings_df = loadings_df.set_index('variable')
ax = sns.heatmap(loadings_df, annot=True, cmap='Spectral')
fig = ax.get_figure()
fig.subplots_adjust(left=0.24)
fig.subplots_adjust(right=1)
plt.title('Correlation matrix plot for loadings')
plt.savefig('figs/Correlation_Matrix.png')