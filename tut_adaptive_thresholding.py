'''
Adaptive Thresholding - It is the method where the threshold is calculated for smaller region. and therefore there will be different thresholding for different regions.

Why is it needed?
Simple thresholding might not be a good idea in conditions where the image has different lighting conditions at different points. So instead of simple thresholding we'll be using adaptive thresholding so as to perform thresholding on different regions with different threshold requirements on the same image.
So Adaptive Thresholding gives us better result with varying illumination.
'''

import cv2 as cv
import numpy as np

img = cv.imread('data/sudoku.png', 0)
# this type of simple/global threshold method results in not so accurate or undesired incomplete result ,so we use Adaptive Thresholding.
_, th1 = cv.threshold(img, 127,255, cv.THRESH_BINARY)

# ADAPTIVE THRESHOLDING are of two types:-
# 1) Adaptive Thresh Mean C - in this type the threshold value is a mean of the blockSize x blockSize neighborhood of (x,y) minus C
th2 = cv.adaptiveThreshold(img, 255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY, 11, 2)

# 2) Adaptive Thresh Gaussian C - in this type the threshold value is a weighted sum of the blockSize x blockSize neighborhood of (x,y) minus C. The default sigma (standard deviation) is used for the specified blockSize.
th3 = cv.adaptiveThreshold(img, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY, 11, 2) 

cv.imshow('Image', img)
cv.imshow('th1', th1)
cv.imshow('Adaptive Thresholding Mean', th2)
cv.imshow('Adaptive Thresholding Gaussian', th3)

cv.waitKey(0)
cv.destroyAllWindows()