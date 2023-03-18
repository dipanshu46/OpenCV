import numpy as np
import cv2

img = cv2.imread('data/leuvenA.jpg')
# img = np.zeros((512,512,3),np.uint8)

print(img.shape)        # returns a tuple of number of rows, columns and channels
print(img.size)         # returns Total number of pixels accessed
print(img.dtype)        # returns Image Datatype

# To get the bgr channel values differently use split
b,g,r = cv2.split(img)
# to merge three channel values together to form an imshow ready image use merge
img = cv2.merge((b,g,r))

cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()