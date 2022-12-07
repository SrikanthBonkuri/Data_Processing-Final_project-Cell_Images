# Greg Howard & Srikanth Bonkuri

import pandas as pd
import matplotlib.pyplot as plt
import math

df = pd.read_csv('data/example.csv')
X = df
print(X)

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
