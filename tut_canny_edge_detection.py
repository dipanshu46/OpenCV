import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('data/messi5.jpg', 0)
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

'''
Canny edge detector method is an edge detection operator that uses a multi stage algorithm to detect a wide range of edges in images. It was developed by John F. Canny in 1986.

The Canny edge detection is composed 5 steps:
    1) Noise Reduction
    2) Gradient Calculation
    3) Non-maximum suppression
    4) Double Threshold
    5) Edge Tracking by Hysteresis
'''

# Canny edge method can be used using cv2.Canny(img_source, threshold1, threshold2, edges=None, apertureSize=None, L2gradient=None), it returns the edges frame.
edges = cv2.Canny(img, 100,200)

# Plotting Code
titles =  ['image', 'canny']
images = [img, edges]
col = 2
row = 1 if len(titles)<col else len(titles)//col if len(titles)%col==0 else (len(titles)//col)+1
    
for i in range(len(titles)):
    plt.subplot(row, col, i+1)
    plt.imshow(images[i])
    plt.title(titles[i])
    plt.xticks([])
    plt.yticks([])

plt.show()