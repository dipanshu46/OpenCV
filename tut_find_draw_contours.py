import cv2
import numpy as np

img = cv2.imread('data/opencv-logo.png', 1)
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# What are contours?
# Contours are the curves joining all the continuous points along the boundary which are having the same color or intensity

# First get threshold or the cannyedge of the image
ret, thresh = cv2.threshold(img_gray, 127, 255, 0)
# To find the contours use cv2.findContours(img_source, mode, method, contours=None, hierarchy=None, offset=None) which will return contours, hierarchy as shown below
# NOTE:- Contours here will be a python list of all the contours in the image. Each contour is a numpy array of (x,y) coordinates of boundary points of the object.
# Heirarchy is the optional output vector which is containing the information about image topology.
contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)

# print("Number of Contours :", len(contours))
# for i in range(len(contours)):
#     print(i,'th contour :', contours[i])

# To draw contours on the image use cv2.drawContours(img_source, contours, index, BGR_COLOR, thickness)
# index -1 will result in all the contours to be printed.
cv2.drawContours(img, contours, -1, (0,255,0), 3)

cv2.imshow('Logo', img)
cv2.imshow('Logo Gray', img_gray)
cv2.waitKey(0)
cv2.destroyAllWindows()