'''
What is thresholding?

Thresholding is a very popular segmentation technique used for seperating an object from its background.
The process involves comparing each pixel of an image with a pre-defined threshold value. On this  comparison we create two groups of pixels, one that has pixels with value less than the threshold value and the second with the ones that have the value greater than the threshold value.
'''


import cv2 as cv

img = cv.imread('data/gradient.png', 0)

# To do thresholding we use the method cv.threshold(image_source, threshold, maxval, type_of_threshold). This method returns two values, first ret and second the thresholded output.

# Binary Threshold - pixel values above threshold are assigned max value and below threshold are assigned 0/minimum value
_, th1 = cv.threshold(img, 50, 255, cv.THRESH_BINARY)

# Binary Inverse Threshold - Inverse of Binary threshold, i.e. pixel values above threshold are assigned minimum value and below threshold are assigned maximum value
_, th2 = cv.threshold(img, 200, 255, cv.THRESH_BINARY_INV)

# Thresh Trunc - The values of pixel upto the threshold value will not change and values of pixel after the threshold will remain same as that of the threshold.
_, th3 = cv.threshold(img, 120, 255, cv.THRESH_TRUNC)

# Thresh ToZero - The values of pixel upto threshold will become 0 and after the threshold will remain same.
_, th4 = cv.threshold(img, 120, 255, cv.THRESH_TOZERO)

# Thresh ToZero Inverse - Inverse of ThreshTOZero, the values of pixel upto threshold will remain same and after the threshold will become 0
_, th5 = cv.threshold(img, 120, 255, cv.THRESH_TOZERO_INV)

cv.imshow('Image', img)
cv.imshow('Binary Threshold', th1)
cv.imshow('Binary Inverse Threshold', th2)
cv.imshow('Threshold Trunc', th3)
cv.imshow('Thresh ToZero', th4)
cv.imshow('Thresh ToZero Inverse', th5)

# res = cv.bitwise_and(img, th1)
# cv.imshow('result', res)
cv.waitKey(0)
cv.destroyAllWindows()