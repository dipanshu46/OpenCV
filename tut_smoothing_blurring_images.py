import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('data/opencv-logo.png',1)
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

# smoothing operation means removing noise from the image. When smoothing images we can diverse linear filters as they are easy to achieve and fast. Various linear filters provided by opencv are Homogenous filters, Gaussian filter, Median filter, Bilateral filter etc.

# 1) Homogenous Filter - It is the most simple filter, each output pixel is the mean of it kernel neighbours. Kernel = (1/(k_width*k_height))*(k by k matrix containing 1)
kernel = np.ones((5,5), np.float32)/25
# filter2D is the method for homogenous filter
# Syntax: cv2.filter2D(img, -1, kernel)
dst = cv2.filter2D(img, -1, kernel)

# NOTE As in 1 Dimensional signals, images can also be filtered with various low-pass filters (LPF), high-pass filters (HPF) etc. 
# LPF helps in removing noises, blurring the images.
# HPF filters help in finding edges in the images.
# Syntax: cv2.blur(img_source, (kernel_x, kernel_y))
blur = cv2.blur(img, (5,5))

# 2) Gaussian Filter - is nothing but using different weighted kernel, in both x and y direction. It has heavier weights on the centre and lighter weights on the corners.
# Syntax: cv2.GaussianBlur(img_source, (kernel_x, kernel_y), sigmaX)
g_blur = cv2.GaussianBlur(img, (5,5), 0)

# 3) Median filter - is something that replaces each pixels value with the median of its neighboring pixels. This method is great when dealing with "Salt and Pepper noise".
# Syntax: cv2.medianBlur(img_source, kernel_shape)
median = cv2.medianBlur(img, 5)

# 4) Bilateral Filter - sometimes we need to preserve the edges of the image as in other techniques when the filters were applied they also dissolved the edges while blurring the image. Bilateral filter is highly effective in noise removal while keeping the edges the sharp.
# Syntax: cv2.bilateralFilter(img_source, diameter, sigmaColor,  sigmaSpace)
bilateralFilter = cv2.bilateralFilter(img, 9, 75, 75)  

titles = ['image','2D Convolution','Blur', 'Gausian Blur', 'Median Blur', 'Bilateral Filter']
images = [img, dst, blur, g_blur, median, bilateralFilter]
col = 3
row = 1 if len(titles)<col  else (len(titles)//col) if len(titles)%col==0 else (len(titles)//col)+1

for i in range(len(titles)):
    plt.subplot(row,col,(i+1))
    plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.xticks([])
    plt.yticks([])

plt.show()