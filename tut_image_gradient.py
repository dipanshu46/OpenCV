'''
Image Gradient - is directional change in the intensity or the color in an image.
It is used find the edges inside an image
'''

import cv2
import numpy as np
from matplotlib import pyplot as plt

# img = cv2.imread('data/messi5.jpg', 0)    # Switch to sudoku.png to know about sobelX and sobelY in a better way
img = cv2.imread('data/sudoku.png', 0)
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

# Laplacian Method
lap = cv2.Laplacian(img, cv2.CV_64F)
# Converting the laplacian image back into uint8
lap = np.uint8(np.absolute(lap))

# SobelX and SobelY method
sobelX = cv2.Sobel(img, cv2.CV_64F, 1, 0)
sobelX = np.uint8(np.absolute(sobelX))
sobelY = cv2.Sobel(img, cv2.CV_64F, 0, 1)
sobelY = np.uint8(np.absolute(sobelY))

sobelCombined = cv2.bitwise_or(sobelX, sobelY)

# Plotting Code
titles =  ['image', 'Laplacian', 'SobelX', 'SobelY', 'SobelCombined']
images = [img, lap, sobelX, sobelY, sobelCombined]
col = 2
row = 1 if len(titles)<col else len(titles)//col if len(titles)%col==0 else (len(titles)//col)+1

for i in range(len(titles)):
    plt.subplot(row, col, i+1)
    plt.imshow(images[i])
    plt.title(titles[i])
    plt.xticks([])
    plt.yticks([])

plt.show()