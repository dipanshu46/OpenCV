import numpy as np
import cv2
from matplotlib import pyplot as plt

# Using black images with custom rectangles
img = np.zeros((200,200), np.uint8)
cv2.rectangle(img, (0,100), (200,200), (255), -1)
cv2.rectangle(img, (0,50), (100,100), (127), -1)

cv2.imshow('img', img)

# To plot a histogram we use the matplotlib.pyplot library from which we use pyplot.hist(img, total x values , range of x)
plt.hist(img.ravel(), 256, [0,256])
plt.xlabel('Pixel Value')
plt.ylabel('No. of Pixels')
plt.title('Pixel Intesity')
plt.show()

cv2.waitKey(0)
cv2.destroyAllWindows()

# Now using actual images
img = cv2.imread('data/leuvenA.jpg', 0)
cv2.imshow('img', img)

plt.hist(img.ravel(), 256, [0,256])
plt.xlabel('Pixel Value')
plt.ylabel('No. of Pixels')
plt.title('Pixel Intensity')
plt.show()

cv2.waitKey(0)
cv2.destroyAllWindows()

# Histograms for rgb colors
img = cv2.imread('data/leuvenA.jpg', 1)
b,g,r = cv2.split(img)
cv2.imshow('image',img)
cv2.imshow('b',b)
cv2.imshow('g',g)
cv2.imshow('r',r)

plt.hist(b.ravel(), 256, [0,256])
plt.hist(g.ravel(), 256, [0,256])
plt.hist(r.ravel(), 256, [0,256])
plt.xlabel('Pixel Value')
plt.ylabel('No. of Pixels')
plt.title('Pixel Intensity')
plt.show()

cv2.waitKey(0)
cv2.destroyAllWindows()

# Using OpenCV method for plotting histogram
img = cv2.imread('data/leuvenA.jpg', 1)

# cv2.calcHist([img], channels, mask, histSize, ranges, hist=None, accumulate=None)
histb = cv2.calcHist([img], [0], None, [256], [0,256])
histg = cv2.calcHist([img], [1], None, [256], [0,256])
histr = cv2.calcHist([img], [2], None, [256], [0,256])
plt.plot(histb)
plt.plot(histg)
plt.plot(histr)
plt.xlabel('Pixel Value')
plt.ylabel('No. of Pixels')
plt.title('Pixel Intesity')
plt.show()