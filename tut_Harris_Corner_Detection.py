import numpy as np
import cv2

img = cv2.imread('data/chessboard.png',1)
# Not an important step doing just because my image file was very big
print(img.shape)
img = cv2.resize(img, (877,620))
cv2.imshow('ChessBoard', img)
# Converting the image to grayscale to get better results
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# Since our cv2.CornerHarris() method takes float 32 bit image source we need to make sure our image is of the same format. So using np.float32(gray)
gray = np.float32(gray)
# cv2.CornerHarris(image, blockSize, ksize, k) where, 
# image - Input image, it should be grayscale and float32 type.
# blockSize - It is the size of neighborhood considered for corner detection.
# ksize -  Aperture parameter of soble derivative used.
# k - Harris detector free parameter in the equation.
dst = cv2.cornerHarris(gray, 2, 3, 0.04)
dst = cv2.dilate(dst, None)
img[dst > 0.01 * dst.max()] = [0,0,255]
cv2.imshow('dst', img)

if cv2.waitKey(0)==ord('q'):
    cv2.destroyAllWindows()