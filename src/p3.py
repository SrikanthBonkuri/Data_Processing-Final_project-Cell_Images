# Greg Howard & Srikanth Bonkuri

# Count the light objects in an image with a dark background

import cv2 as cv # Import the OpenCV library

# For now we are handling a hard coded local images.
# We may consider improving to have this deal with a series of images.
image = cv.imread("data/image_green.png")

r = len(image)
c = len(image[0])
print(r,"x",c)
print("Total Pixels:", r*c)

# For now we are handling all pixels in one of 3 categories.
# We may consider a more nuanced approach based on input from visual studies and cell biology experts.
d = 0
w = 0
g = 0

M = image
for i in range(r):
    for j in range(c):
        #Vec3b color = image.at<Vec3b>(i, j)
        z = image[i,j,0]   #blue
        y = image[i,j,1]   #green
        x = image[i,j,2]   #red
        if x < 51 and y < 51 and z < 51:
            d +=1 
            M[i,j,0] = 0
            M[i,j,1] = 0
            M[i,j,2] = 0
        elif x > 200 and y > 200 and z > 200:
            w +=1
            M[i,j,0] = 250
            M[i,j,1] = 250
            M[i,j,2] = 250
        else:
            g +=1
            M[i,j,0] = 150
            M[i,j,1] = 150
            M[i,j,2] = 150

    
print("Dark Pixels:", d)
print("Bright Pixels:", w)
print("Gray Pixels:", g)

# imshow function is native to C++, so we may find a Python alternative for displaying a greyscale reduction image
#imshow("abc", M);
#imwrite("abc.png", M);
#waitKey(0);

R = M
k = 0
t, m = 0, 0

# BFS approach to counting cells, because it's easier to visualize
# DFS approach is laid out here: https://www.geeksforgeeks.org/find-the-number-of-islands-using-dfs/
q = []  #Queue
cells = []
white = 0 # We need to figure out how to get actual count of white pixels per cell

for i in range(r):
    for j in range(c):
        if R[i,j,0] == 0 and R[i, j, 1] == 0 and R[i, j, 2] == 0:
            k = 0
            continue
        q.append([i,j])
        if R[i,j,0] == 250:
            white += 1
        R[i, j, 0] = 0
        R[i, j, 1] = 0
        R[i, j, 2] = 0
        while len(q)!=0:
            result = q[0]
            x = result[0]
            y = result[1]
            q.pop(0)
            #r[k][l]=0;
            k += 1
            for a in range(x-1, x+2):
                for b in range(y-1, y+2):
                    if a < 0 or a >= r or b < 0 or b >= c: continue
                    if R[a,b,0] == 0 and R[a,b,1] == 0 and R[a,b,2] == 0: continue
                    q.append([a,b])
                    if R[i,j,0] == 250:
                        white += 1
                    #r[a][b] = 0;
                    R[a,b,0] = 0
                    R[a,b,1] = 0
                    R[a,b,2] = 0
                
        if k>32:
            t +=1
            cells.append([k, white]) # Not working yet
            #white = 0
        if k > m: m = k
        #cout<<t<<"*";
        k = 0
        white = 0
    
print("Total Chunks:", t)
print("Largest Chunk:", m)
print(cells)
