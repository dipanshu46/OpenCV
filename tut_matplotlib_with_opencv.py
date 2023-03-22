import cv2
from matplotlib import pyplot as plt

img = cv2.imread('data/leuvenA.jpg', -1)
cv2.imshow('image', img)
# converting image to RGB from BGR as matplotlib reads images in RGB mode
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
# Method to display images on pyplots 
# NOTE:- It does not directly displays on the screen. It is a function that displays image on the pyplot. To display the pyplot, use pyplot.show() method. Look below.
plt.imshow(img)
# xticks and yticks are the markings on the respective axis.
# to remove them give them an empty array
plt.xticks([]), plt.yticks([])
# To display the output on the screen
plt.show()

# diving deep into matplotlib
img = cv2.imread('data/gradient.png', 0)
_, th1 = cv2.threshold(img, 50, 255, cv2.THRESH_BINARY)
_, th2 = cv2.threshold(img, 200, 255, cv2.THRESH_BINARY_INV)
_, th3 = cv2.threshold(img, 120, 255, cv2.THRESH_TRUNC)
_, th4 = cv2.threshold(img, 120, 255, cv2.THRESH_TOZERO)
_, th5 = cv2.threshold(img, 120, 255, cv2.THRESH_TOZERO_INV)

# Creating lists for titles and images to iterate over and display in the pyplot using subplots.
titles = ['Og Image', 'BINARY', 'BINARY_INV', 'TRUNC', 'TOZERO', 'TOZERO_INV']
images = [img, th1, th2, th3, th4, th5]

for i in range(6):
    # subplot(rows, columns, current_pos)
    plt.subplot(2,3, i+1)
    plt.imshow(images[i], 'gray')
    # To set title to the plot
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])

# Displaying the plot
plt.show()
cv2.waitKey(0)
cv2.destroyAllWindows()