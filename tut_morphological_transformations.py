'''
Morphological transformations - 
        are some simple operations based on the images shape. They are normally performed on binary images.

To perform morphological operations we need two things, 
first the image, 
second is called a structuring element or kernel which decides the nature of operations.
A kernel tells you how to change the value of any given pixel by combining it with different amounts of the neighboring pixels.

There are different types of morphological transformations.
'''

import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('data/smarties.png', 0)
_, mask = cv2.threshold(img,220, 255, cv2.THRESH_BINARY_INV)

# 1) Dilation - kernel is directly applied on the image.
# Create a kernel for dilation which is generally a square that will applied on the images
kernel = np.ones((5,5), np.uint8)
# for dilation we will create a new source of image dilation
# to use dilation we use dilate(image_source, kernel, iterations=1) method. iterations is a keyworded argument.
dilation = cv2.dilate(mask, kernel, iterations=2)

# 2) Erosion - our kernel moves over the whole picture and the pixel value is set 1 only if all the pixels under the kernel are 1.
erosion = cv2.erode(mask, kernel, iterations=1)

# 3) Opening - this morphological operation is a combination of the main two morphological operations i.e. Dilation and Erosion. First it performs Erosion followed by a Dilation.
opening = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)

# 4) Closing - this morphological operation is also a combination of the main two morphological operations i.e. Dilation and Erosion. First it performs Dilation followed by an Erosion.
closing = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)

# 5) Morphological Gradient - is the difference between dilation and erosion of an image
mg = cv2.morphologyEx(mask, cv2.MORPH_GRAPDIENT, kernel)

# 6) Tophat - it is difference between the image and the opening of the image.
th = cv2.morphologyEx(mask, cv2.MORPH_TOPHAT, kernel)

# There are few other morphological transformations that are left for you to explore.

titles = ['image', 'mask', 'dilation', 'ersoion','opening', 'gradient', 'tophat']
images = [img, mask, dilation, erosion, opening, mg, th]

for i in range(8):
    plt.subplot(2,4,i+1)
    plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])

plt.show()