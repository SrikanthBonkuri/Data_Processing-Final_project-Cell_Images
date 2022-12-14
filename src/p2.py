# Greg Howard & Srikanth Bonkuri

import matplotlib.pyplot as plt
import numpy as np

# Read images from the data folder
img_bf = plt.imread('data/BioIVT Hepatocytes 7-24-19_bf_20190620213016.png')
img_green = plt.imread('data/BioIVT Hepatocytes 7-24-19_green_20190620213016.png')
img_red = plt.imread('data/BioIVT Hepatocytes 7-24-19_red_20190620213016.png')

# Produce a joint histogram of pixel intensity across the images
num_bins = 256
labels = ['Brightfield', 'Green', 'Red']
image_set = [img_bf, img_green, img_red]
hist_range = (0.0, np.max(image_set))
fig, ax = plt.subplots()
for img in image_set:
    plt.hist(img.ravel(), bins=num_bins, range=hist_range)

# Label and beautify
fig.subplots_adjust(top=0.9, left=0.15)
x_locations = [np.median(img_bf), np.median(img_green), np.median(img_red)]
ax.set_xticks(x_locations, labels)
ax.set_ylabel('Pixel Count')
ax.set_xlabel('Pixel Intensity (scaled 0 to 1)')
fig.suptitle('Pixel Intensity Histogram by Imaging Method')
fig.savefig('figs/Pixel_Intensity_Hist_by_Imaging_Method.png')
