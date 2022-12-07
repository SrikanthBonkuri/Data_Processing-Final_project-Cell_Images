# Greg Howard & Srikanth Bonkuri

# Count the light objects in an image with a dark background

import cv2 as cv # Import the OpenCV library
import math

# For now we are handling a hard coded local images.
# We may consider improving to have this deal with a series of images.
image = cv.imread("data/image_green.png")

r = len(image)
c = len(image[0])
print(r,"x",c)
print("Total Pixels:", r*c)
assert(image.size == r*c*len(image[0][0]))

# For now we are handling all pixels in one of 3 categories.
# We may consider a more nuanced approach based on input from visual studies and cell biology experts.
d = 0
w = 0
g = 0

M = image
for i in range(r):
    for j in range(c):
        z = image[i, j, 0]   #blue
        y = image[i, j, 1]   #green
        x = image[i, j, 2]   #red
        if x < 51 and y < 51 and z < 51:
            d += 1 
            M[i, j, 0] = 0
            M[i, j, 1] = 0
            M[i, j, 2] = 0
        elif x > 200 and y > 200 and z > 200:
            w += 1
            M[i, j, 0] = 250
            M[i, j, 1] = 250
            M[i, j, 2] = 250
        else:
            g += 1
            M[i, j, 0] = 150
            M[i, j, 1] = 150
            M[i, j, 2] = 150

    
print("Black Pixels:", d)
print("White Pixels:", w)
print("Gray Pixels:", g)

# Produce a greyscale reduction image
# We may consider improving this to allow for naming multiple images differently
'''cv.imshow("image_grey", M)
cv.waitKey(0)'''
cv.imwrite("data/image_grey.png", M)


R = M.copy() # Make a copy so we can still reference the original
k = 0 # This is the count of pixels in an object
t, m = 0, 0 # Total objects and largest object

# BFS approach to counting cells, because it's easier to visualize
# DFS approach is laid out here: https://www.geeksforgeeks.org/find-the-number-of-islands-using-dfs/
q = []  #Queue
cells = []
white = 0 # A measure of flourescence (i.e how much dye the cell has absorbed)
black = 0 # A measure of distortedness (i.e. how non-spherical the cell is)

# Loop through all pixels by row and column
for i in range(r):
    for j in range(c):
        # When encountering a black pixel, reset the pixel count and continue looping
        if R[i,j,0] == 0 and R[i, j, 1] == 0 and R[i, j, 2] == 0:
            continue
        # If encountering a grey or white pixel, add to queue
        q.append([i, j])
        x1, x2 = i, i
        y1, y2 = j, j
        # Tally if white
        if R[i, j, 0] == 250 and R[i, j, 1] == 250 and R[i, j, 2] == 250:
            white += 1
        # Set the pixel black
        R[i, j, 0] = 0
        R[i, j, 1] = 0
        R[i, j, 2] = 0
        # Process the queue until empty
        while len(q) != 0:
            result = q[0]
            x = result[0]
            y = result[1]
            q.pop(0)
            k += 1 # Add to the object's pixel count after popping from the queue
            if x<x1: x1 = x # Find the leftmost pixel
            if x>x2: x2 = x # Find the rightmost pixel
            if y<y1: y1 = y # Find the lowest pixel
            if y>y2: y2 = y # Find the highest pixel
            for a in range(x-1, x+2):
                for b in range(y-1, y+2):
                    if a < 0 or a >= r or b < 0 or b >= c: continue # Deal with out of bounds cases
                    if R[a,b,0] == 0 and R[a,b,1] == 0 or R[a,b,2] == 0: continue # Deal with black pixels
                    q.append([a, b]) # Add to queue the location of any grey or white pixel
                    if R[a, b, 2] == 250: # Count if white
                        white += 1
                    # Set the pixel black
                    R[a, b, 0] = 0
                    R[a, b, 1] = 0
                    R[a, b, 2] = 0
        # Count if greater than 2^7 and add to our cells array
        if k > 128:
            # Get the variables
            cx = (x1 + x2) // 2
            cy = (y1 + y2) // 2
            height = y2 - y1
            width = x2 - x1
            hh = height // 2
            hw = width // 2
            radius = ( hh + hw ) // 2 # This lets us approximate a circle with the same center
            circle_area = int(math.pi * radius**2)
            # Check the count of black pixels within the radius
            for m in range(height):
                for n in range(width):
                    # Calculate distance from the center
                    if m < hh:
                        py = int(hh - m)
                    else:
                        py = int(m - hh)
                    if n < hw:
                        px = int(hw - n)
                    else:
                        px = int(n - hw)
                    d = math.sqrt(px**2 + py**2) # Thanks Pythagoras
                    # When distance is less than radius, calculate image x and y, then check if black
                    if d <= radius:
                        if m < hh and n < hw:
                            if M[cx - px, cy - py, 0] == 0:
                                black += 1
                        elif m < hh and n > hw:
                            if M[cx + px, cy - py, 0] == 0:
                                black += 1
                        elif m > hh and n < hw:
                            if M[cx - px, cy + py, 0] == 0:
                                black += 1
                        else:
                            if M[cx + px, cy + py, 0] == 0:
                                black += 1
            t += 1
            cells.append([k, round((white/k)*100, 2), height, width, cx, cy, circle_area, round((black/circle_area)*100, 2)])
            M[cx, cy, 0] = 0
            M[cx, cy, 1] = 0
            M[cx, cy, 2] = 255
            for a in range(cx-1, cx+2):
                for b in range(cy-1, cy+2):
                    if a < 0 or a >= r or b < 0 or b >= c: continue
                    if M[a,b,0] == 0 and M[a,b,1] == 0 or M[a,b,2] == 0: continue
                    M[a, b, 0] = 0
                    M[a, b, 1] = 0
                    M[a, b, 2] = 255
        if k > m: m = k
        # Reset counts of k, white pixels, and inner black pixels
        k = 0
        white = 0
        black = 0

    
'''cv.imshow("image_center", M)
cv.waitKey(0)
cv.imwrite("data/image_center.png", M)'''
print("Total objects:", t)
print("Largest object:", m)
print(cells)
