# Greg Howard & Srikanth Bonkuri

import cv2

# Read image from the data folder
img = cv2.imread('data/BioIVT Hepatocytes 7-24-19_bf_20190620213016.png')

# Access the pixel count in each dimension and print
b_height, b_width, channels = img.shape
size = b_height * b_width
print('Brightfield image pixel count: ' + str(size) + ' (height: ' + str(b_height) + ' width: ' + str(b_width) + ')')
