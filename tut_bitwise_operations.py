import numpy as np
import cv2

# Creating Image 1 with a white square at top center.
img1 = np.zeros((250,500,3), np.uint8)
img1 = cv2.rectangle(img1, (200,0), (300,100), (255,255,255), -1)
# Creating Image2 which is left half black and right half white
img2 = np.zeros((250,500,3), np.uint8)
img2 = cv2.rectangle(img2, (250,0), (500,250), (255,255,255), -1)

# bitwise operations
bit_and = cv2.bitwise_and(img1, img2)
bit_or = cv2.bitwise_or(img1, img2)
bit_xor = cv2.bitwise_xor(img1, img2)
bit_not_1 = cv2.bitwise_not(img1)
bit_not_2 = cv2.bitwise_not(img2)

cv2.imshow('Image 1', img1)
cv2.imshow('Image 2', img2)
cv2.imshow('Bitwise And', bit_and)
cv2.imshow('Bitwise Or', bit_or)
cv2.imshow('Bitwise Xor', bit_xor)
cv2.imshow('Bitwise Not 1', bit_not_1)
cv2.imshow('Bitwise Not 2', bit_not_2)

cv2.waitKey(0)
cv2.destroyAllWindows()