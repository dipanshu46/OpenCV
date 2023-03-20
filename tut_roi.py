'''
ROI :- Region of interest

The area in the image that we want to work on is known as the region of interest.
'''

import numpy as np
import cv2

img = cv2.imread('data/messi5.jpg',1)

# to select a region, give coordinates like image_object[y1:y2 , x1:x2] where points 1 and 2 are diagonally opposite points of a rectangle area.
ball = img[290:340, 335:390]
img[73:123, 200:255] = ball

cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()