# Greg Howard & Srikanth Bonkuri

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Retrieve the data and prepare to work with the Cell instance column
df = pd.read_csv('data/example.csv')
df.rename(columns = {df.columns[0]:'Cell'}, inplace = True)

# Plot (beautifully) and save
scatter_plot_matrix = sns.pairplot(df, palette='deep', hue='Cell')
plt.savefig('figs/Feature_Scatterplot_Matrix.png')
