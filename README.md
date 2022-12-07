# Cell Images
Greg Howard & Srikanth Bonkuri

#### Note: you will need to download OpenCV for Python to complete Part2
```pip install opencv```

### Reproducing the figures based on the dataset
First clone this repo.
```git clone https://github.com/ds5110/cell-images.git```
Then in the directory where you cloned this repo, run the files in <strong><code>src</code></strong>.
#### Part 1
```python3 src/p1.py```
#### Part 2
```python3 src/p2.py```
#### Part 3
```python3 src/p3.py```
#### Part 3.5 (optional: used to produce the dataframe example, already as a csv in /data)
```python3 src/p3_5.py```
#### Part 4
```python3 src/p4.py```
Review <strong><code>figs</code></strong> and the file will have been overwritten by your runs. Feel free to delete the pre-existing figures in advance to truly validate.

## Part 1: Elementary Image Analysis

Here we've proven we can read PNG files and show the count of pixels. All the PNGs we'll be working with have the following properties.
* pixel count: 3145728
* height: 1536
* width: 2048

## Part 2: Pixel Intensity Analysis

<img src="figs/pixel_intensity_hist_by_imaging_method.png" width="500">

There are three types of images that are captured by DeNovix's CellDrop automated cell counters, prior to their algorithm producing a 'result' image. These images are brightfield, which involves passing light through the sample, and two kinds of fluorescent imaging, red and green. In the flourescent images, only the cells which have absorbed dyes will light up and appear bright in the image. In the green images, live and intact cells that (i.e. those that have absorbed acridine orange) light up. And, in the red images, dead cells (i.e. those that have absorbed propidium iodide) light up.

In this histogram of 256 bins - because there are 2^6 options for level of intensity in RGB - it is easy to see that there are different intensity levels prevailing in each of the image types. Specifically, there are more pixels of higher intensity in the brightfield image. And between the Red and the Green image it seems the Green image has brighter bright spots.

Note: there is a bug that affects MacOS, which will throw an unecessary warning and is supposed to be corrected in the next major version. Until then, please do not mark off points if you experience this error as I have: https://github.com/matplotlib/matplotlib/issues/23921

## Part 3: Greyscale Image Reduction

<img src="data/image_green.png" width="500">
This is a sample image of hepatocytes that have absorbed acridine orange, glowing green in flourescent light.

<img src="data/image_grey.png" width="500">
Here we have our greyscale reduction of the image, which we produce for easier analysis.

## Part 4: Analysis of Flourescence

<img src="figs/Cell_Area_by_Percentage_White.png" width="500">

White pixels count is a measure of how much of a cell absorbed acridine orange dye. It is easy to see that there is a logarithmic relationship between the area of a cell and the percentage of it that is white. Notably, it's also easy to see that as a cell takes up more pixels, it is also more likely to have a larger proportion of white pixels. This is not surprising, nor is the bundle of scattered dots with 0% white and small total size, because the larger a cell, the more flourescent dye it will hold onto.

## Part 5: Principal Components Analysis

<img src="figs/Explained_Variance_Ratio_by_Factor.png", width="500">

We can see here that among the factors we have tracked 3 of them will explain 95.7% of the variance among the cells and 4 factors can cumulatively explain 98.3%. Once we consider 5 factors, we can explain more than 99% of the variance. Dimensionality reduction is pretty meaningful in the context of our project, considering we may one day want our code to run rapidly on cell counter devices. It is also worth noting that we have standardized the columns to scale them. Otherwise, 'Area' would dominate and explain over 95% of the variance.

In the future, we can produce a proper scree plot to demarcate the elbow beyond which additional factors become largely unimportant.

<img src="figs/Covariance_Matrix.png", width="500">

For additional information, here is the correlation matrix.

## Part 6: K-Means Clustering

<img src="figs/Elbow_Plot_Kmeans.png", width="500">

Calculating within cluster sum of squares (WCSS), one can figure out the most informative number of clusters. We have plotted the WCSS for 1 through 8 clusters in the elbow plot above and observed that WCSS is reducing substantially and increasingly until k=4 and not very significantly thereafter.

Therefore, we used k-means to identify 4 clusters on two of our most interesting engineered features: White Percent Area and Black Percent Circle. The former is a measure of object fluorescence and the latter is a measure of object sphericity. We have plotted these against Area and Circle Area respectively. The Area is the area of the entire object (i.e. count of contiguous grey and white pixels that make up a cell or clumped neighborhood of cells). The Circle Area is the area of a circle produced on the center of the object with a diameter that is the average of the object’s width and height.

<img src="figs/Cell_Cluster_Kmeans(White Percent x Area and Black Percent x Circle Area).png", width="500">

In both charts, it’s easy to see the relationship between clusters and the size of the object. Object size may be single most predictive feature for the variance across the population. It’s also interesting to note that cluster 3 (in moss green) holds only a single anomalous object, with a far larger pixel count than the rest. Perhaps this is multiple overlapping cells. And, it’s curious to see that there is a small cell with a very large percentage of black within its circle area. Likely, this is a slender oval, and perhaps it represents cellular material from a no longer intact cell. Prior to our final submission, we may seek to recreate images with the clusters identified visually for deeper analyses and more intutive analyses.
