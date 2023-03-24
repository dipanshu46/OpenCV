'''
Image Pyramids - 
    Sometimes we need to work with images of different resolution. So we use pyramids.
    Pyramid representation, is a type of signal representation in which a signal or an image is subjected to repeat smoothing and subsampling.

There are two types of pyramids available in opencv:
    1) Gaussian pyramid - repeated filtering and subsampling of image. Func available are pyrdown and pyrup
    2) Laplacian pyramid

'''

import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('data/leuvenA.jpg')
# Using Gaussian Pyramid methods pyrdown and pyrup.
lr1 = cv2.pyrDown(img)
lr2 = cv2.pyrDown(lr1)
hr2 = cv2.pyrUp(lr2)

cv2.imshow('Original image', img)
cv2.imshow('pyrDown 1 image', lr1)
cv2.imshow('pyrDown 2 image', lr2)
cv2.imshow('pyrUp 1 image', hr2)
cv2.waitKey(0)
cv2.destroyAllWindows()

# To write the code for the same in a better way
layer = img.copy()
gp  = [layer]

for i in range(6):
    layer = cv2.pyrDown(layer)
    gp.append(layer)
    cv2.imshow(str(i), layer)

cv2.imshow('Original image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Laplacian Pyramid
# A level of Laplacia pyramid is formed by the difference between that level in the Gaussian pyramid and the expanded version of its upper level in Gaussian Pyramid.

layer = gp[-1]
cv2.imshow('Upper level Gaussian Pyramid', layer)
lp = [layer]

for i in range(5,0,-1):
    gaussian_extended = cv2.pyrUp(gp[i])
    laplacian = cv2.subtract(gp[i-1], gaussian_extended)
    cv2.imshow(str(i), laplacian)

cv2.imshow('Original Image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()