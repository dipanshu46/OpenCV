import cv2
import numpy as np

img = cv2.imread('data/opencv-logo.png', 1)
img_copy = cv2.imread('data/opencv-logo.png', 1)
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# What are contours?
# Contours are the curves joining all the continuous points along the boundary which are having the same color or intensity

# Now we need to create a threshold image for finding the contours on the image. For doing so we need to convert the image using threshold binary or canny edge detection just to make the edges of similar color and intensity so that our findContours() method finds them easily.

# Method 1: Using Threshold Binary, we need to provide a gray image as seen earlier to apply thresholds to the image
ret, thresh1 = cv2.threshold(img_gray, 127, 255, 0)

# Method 2: Using Canny Edge detection, just pass the image with your threhold values and it will find the edges real quick.
thresh2 = cv2.Canny(img, 100, 200)

# To find the contours use cv2.findContours(img_source, mode, method, contours=None, hierarchy=None, offset=None) which will return contours, hierarchy as shown below
# NOTE:- Contours here will be a python list of all the contours in the image. Each contour is a numpy array of (x,y) coordinates of boundary points of the object.
# Heirarchy is the optional output vector which is containing the information about image topology.
contours, hierarchy = cv2.findContours(thresh1, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)

# print("Number of Contours :", len(contours))
# for i in range(len(contours)):
#     print(i,'th contour :', contours[i])

# To draw contours on the image use cv2.drawContours(img_source, contours, index, BGR_COLOR, thickness)
# index -1 will result in all the contours to be printed.
cv2.drawContours(img_copy, contours, -1, (0,255,0), 3)

cv2.imshow('Original Image', img)
cv2.imshow('Logo Gray', img_gray)
cv2.imshow('Thresh', thresh1)
cv2.imshow('Canny', thresh2)
cv2.imshow('Contours using Threshold', img_copy)
img_copy = img
contours, hierarchy = cv2.findContours(thresh2, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
cv2.drawContours(img_copy, contours, -1, (0,255,0), 3)
cv2.imshow('Contours using Canny', img_copy)
cv2.waitKey(0)
cv2.destroyAllWindows()