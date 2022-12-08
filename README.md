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
#### Part 3.5 (optional: used to produce the data that is already as a csv in /data/example.csv)
```python3 src/p3_5.py```
#### Part 4
```python3 src/p4.py```
Review <strong><code>figs</code></strong> and the file will have been overwritten by your runs. Feel free to delete the pre-existing figures in advance to truly validate.
#### Part 5
```python3 src/p5.py```
#### Part 6
```python3 src/p6.py```

## Part 1: Elementary Image File Analysis

Here we've proven we can read PNG files and show the count of pixels. All the PNGs we'll be working with have the following properties.
* pixel count: 3145728
* height: 1536
* width: 2048

## Part 2: Pixel Intensity Analysis

<img src="figs/pixel_intensity_hist_by_imaging_method.png" width="500">

There are three types of images that are captured by DeNovix's CellDrop automated cell counters, prior to their algorithm producing a 'result' image. These images are brightfield, which involves passing light through the sample, and two kinds of fluorescent imaging, red and green. In the flourescent images, only the cells which have absorbed dyes will light up and appear bright in the image. In the green images, live and intact cells that (i.e. those that have absorbed acridine orange) light up. And, in the red images, dead cells (i.e. those that have absorbed propidium iodide) light up.

In this histogram of 256 bins - because there are 2^6 options for level of intensity in RGB - it is easy to see that there are different intensity levels prevailing in each of the image types. Specifically, there are more pixels of higher intensity in the brightfield image. And between the Red and the Green image it seems the Green image has brighter bright spots.

## Part 3: Image Gradient Reduction

<img src="data/image_green.png" width="500">
This is a sample image of tumorspheres that have absorbed acridine orange captured in green flourescent light.
<br /><br /><br />

<img src="data/image_grey.png" width="500">
Here we have our gradient reduction of the image pixel intensities into buckets of white, black, and grey. This allows for easier analysis of cells bodies (and organelles), membranes (and plasma), and background, which enables easier analysis.
<br /><br />

## Part 4: Cell Size by Fluorescence Analysis

<img src="figs/Cell_Area_by_Percentage_White.png" width="900">

White pixels count is a measure of how much of a cell absorbed acridine orange dye. It is easy to see that there is a logarithmic relationship between the area of a cell and the percentage of it that is white. Notably, it's also easy to see that as a cell takes up more pixels, it is also more likely to have a larger proportion of white pixels. This is not surprising, nor is the bundle of scattered dots with 0% white and small total size, because the larger a cell, the more flourescent dye it will hold onto.

## Part 5: K-Means Clustering

<img src="figs/Elbow_Plot_Kmeans.png" width="500">

Calculating within cluster sum of squares (WCSS), one can figure out the most informative number of clusters. We have plotted the WCSS for 1 through 8 clusters in the elbow plot above and observed that WCSS is reducing substantially and increasingly until k=4 and not very significantly thereafter.

Therefore, we used k-means to identify 4 clusters on two of our most interesting engineered features: White Percent Area and Black Percent Circle. The former is a measure of object fluorescence and the latter is a measure of object sphericity. We have plotted these against Area and Circle Area respectively. The Area is the area of the entire object (i.e. count of contiguous grey and white pixels that make up a cell or a clumped and touching neighborhood of cells). The Circle Area is the area of a circle produced on the center of the object with a diameter that is the average of the object’s width and height.

<img src="figs/Cell_Cluster_Kmeans(White Percent x Area and Black Percent x Circle Area).png" width="900">

In both charts, it’s easy to see the relationship between clusters and the size of the object. Object size may be single most predictive feature for the variance across the population. It’s also interesting to note that cluster 3 (in moss green) holds only a single anomalous object, with a far larger pixel count than the rest. Perhaps this object is a clump of multiple overlapping cells. And, it’s curious to see that there is a small cell with a very large percentage of black within its circle area. Likely, this is a slender oval, and perhaps it represents cellular material from a no longer intact cell. Prior to our final submission, we may seek to recreate images with the clusters identified visually for more intutive analyses and review with a cell biologist.

## Part 6: Principal Components Analysis

<img src="figs/Explained_Variance_Ratio_by_Factor.png" width="500">

We can see here that among the principal components we have computed 3 of them will explain 95.7% of the variance among the cells and 4 components can cumulatively explain 98.3%. Once we consider 5 components or more, we can explain more than 99% of the variance.

<img src="figs/Covariance_Matrix.png" width="500">

For additional information on the relationsips between features we tracked and engineered in our dataframe and the principal components, here is the covariance matrix.

Dimensionality reduction is pretty meaningful in the context of our project, considering we may one day want our code to run rapidly on cell counter devices. In the more immediate future, we may also want have subject matter experts tag cells for us in a way that we can use to train a deep learning model to count even non-spherical cells correctly. While this original test and train data may not be too large, future data sets from scientists we share this application with may be much larger. Therefore, we will continue to simultaneously engineer the most meaningful features we can and reduce the data frame size as much as possible.

## Acknowledgements

This work would not have been possible without the data and guidance provided by DeNovix, Inc. In particular we'd like to thank Aroshan Jayasinghe, Product Development Specialist, Vinsky Muthia, Application Scientist, and their entire product development team.

We'd also like to thank Professor Phil Bogden for teaching us the methods applied in this project and for providing the impetus to make this happen.

Lastly, we are grateful to the creators and contributors of Python, Pandas, Scikit-Learn, Matplotlib, Numpy, and OpenCV. To paraphrase Isaac Newton: if we have seen cells with greater insight, it is only by leveraging the work of giants.

## Note on deprecation warning

Note: there is a bug that affects MacOS, which will throw an unecessary warning and is supposed to be corrected in the next major version. Until then, please do not mark off points if you experience this error as we have. Source for details of the error: https://github.com/matplotlib/matplotlib/issues/23921
