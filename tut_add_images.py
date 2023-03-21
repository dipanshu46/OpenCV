import numpy as np
import cv2

img = cv2.imread('data/messi5.jpg', 1)
img2 = cv2.imread('data/opencv-logo.png', 1)

cv2.imshow('Image 1', img)
cv2.imshow('Image 2', img2)

# resize(image_source, (width, height))
img2 = cv2.resize(img2, (img.shape[1], img.shape[0]))
# print(img2.shape)
# print(img.shape)


new = cv2.add(img, img2)
cv2.imshow('New Image', new)
cv2.waitKey(0)
cv2.destroyAllWindows()