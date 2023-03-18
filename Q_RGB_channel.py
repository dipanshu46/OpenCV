'''
Q. Display the RGB channel colours differently of an image.
'''

import numpy as np
import cv2

img = cv2.imread('data/leuvenA.jpg')

# To get the bgr channel values differently use split
b,g,r = cv2.split(img)
zero = np.zeros((img.shape[0],img.shape[1]),np.uint8)
r_img = cv2.merge((zero,zero,r))
g_img = cv2.merge((zero,g,zero))
b_img = cv2.merge((b,zero,zero))
cv2.imshow('R Channel', r_img)
cv2.imshow('G Channel', g_img)
cv2.imshow('B Channel', b_img)

cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()