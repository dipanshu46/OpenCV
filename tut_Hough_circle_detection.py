'''
Hough Circle Detection - 
    In mathematics, a circle is represented in the form of 
    (x-xc)**2 + (y-yc)**2 = r**2 where, 
    (xc,yc) are the center coordinates of the circle and r is the radius.
'''

import cv2
import numpy as np

img = cv2.imread('data/smarties.png', 1)
output = img.copy()
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
gray = cv2.medianBlur(gray, 5)

# hough circles can be made using cv2.HoughCircles(img, method, dp, minDist[, circles[, param1[, param2[, minRadius[, maxRadius]]]]]) where,
# image - 8-bit, single channel, greyscale input image.
# It outputs vector of found circles.
# method - Detection method, see HoughModes. Currently, the only implemented mehtod is HOUGH_GRADIENT.
# dp - Inverse ratio of the accumulator resoution to the image resolution.
# minDist - Minimum distance between the centers of the detected circles.
# param1 - First method-specific parameter. In case of HOUGH_GRADIENT, it is the higher threshold of the two passed to the Canny Edge detector (the lower one is twice smaller.)
# param2 - Second method-specific parameter. In case of HOUGH_GRADIENT, it is the accumulator threshold for the circle centers at the detection stage.
# minRadius - Minimum circle radius.
# maxRadius - Maximum circle radius. if <= 0 , uses the maximum image dimension. If < 0, returns centers without finding the radius.
circles = cv2.HoughCircles(gray, cv2.HOUGH_GRADIENT, 1, 20, param1=50, param2=30, minRadius=0, maxRadius=0)
detected_circles = np.uint16(np.around(circles))
for (x,y,r) in detected_circles[0, :]:
    cv2.circle(output, (x,y), r, (100,40,120), 2)
    cv2.circle(output, (x,y), 2, (0,255,255), -1)

cv2.imshow('Output', output)
cv2.waitKey(0)
cv2.destroyAllWindows()
