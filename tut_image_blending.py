import cv2
import numpy as np

apple = cv2.imread('data/apple.jpg', 1)
orange = cv2.imread('data/orange.jpg', 1)

print(apple.shape)
print(orange.shape)

# one way to merge these apple and orange images is to stack the half apple and half orange image side by side using the numpy.hstack() method.
apple_orange = np.hstack((apple[:, :256], orange[:, 256:]))
# but we can see a sharp line through the center of the image that marks that the two images are stacked side by side whereas we desire a blended image 

cv2.imshow('apple', apple)
cv2.imshow('orange', orange)
cv2.imshow('apple_orange', apple_orange)
cv2.waitKey(0)
cv2.destroyAllWindows()

# my way
apple = cv2.imread('data/apple.jpg', 0)
orange = cv2.imread('data/orange.jpg', 0)
gradient = cv2.imread('data/gradient.png', 0)
gradient = cv2.resize(gradient, (apple.shape[1],apple.shape[0]))

_, apple_half = cv2.threshold(gradient, 122, 255, cv2.THRESH_BINARY_INV)
_, orange_half = cv2.threshold(gradient, 122, 255, cv2.THRESH_BINARY)

apple_half = cv2.bitwise_and(apple,apple_half)
orange_half = cv2.bitwise_and(orange,orange_half)
merged = cv2.add(apple_half, orange_half)
merged_or = cv2.bitwise_or(apple_half, orange_half)

cv2.imshow('gradient', gradient)
cv2.imshow('Apple Half', apple_half)
cv2.imshow('Orange Half', orange_half)
cv2.imshow('Merged', merged)
cv2.imshow('Merged Or', merged_or)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Using Image pyramid technique. To use it we need to follow 5 steps.
# 1) Load the two images. 
apple = cv2.imread('data/apple.jpg', 1)
orange = cv2.imread('data/orange.jpg', 1)

# 2) Find the Gaussian Pyramids for apple and orange

# generating Gaussian Pyramid for apple
apple_copy = apple.copy()
gp_apple = [apple_copy]

for i in range(6):
    apple_copy = cv2.pyrDown(apple_copy)
    gp_apple.append(apple_copy)

# generating Gaussian Pyramid for orange
orange_copy = orange.copy()
gp_orange = [orange_copy]

for i in range(6):
    orange_copy = cv2.pyrDown(orange_copy)
    gp_orange.append(orange_copy)

# 3) From Gaussian Pyramids find their laplacian pyramids

# generating laplacian pyramid for apple
apple_copy = gp_apple[5]
lp_apple = [apple_copy]

for i in range(5,0,-1):
    gaussian_extended = cv2.pyrUp(gp_apple[i])
    laplacian = cv2.subtract(gp_apple[i-1], gaussian_extended)
    lp_apple.append(laplacian)

# generating laplacian pyramid for orange
orange_copy = gp_orange[5]
lp_orange = [orange_copy]

for i in range(5,0,-1):
    gaussian_extended = cv2.pyrUp(gp_orange[i])
    laplacian = cv2.subtract(gp_orange[i-1], gaussian_extended)
    lp_orange.append(laplacian)

# 4) Now join the left half of apple and right half of the orange in each levels of laplacian pyramid.
apple_orange_pyramid = []
n = 0

for apple_i, orange_i in zip(lp_apple, lp_orange):
    n += 1
    cols, rows, ch = apple_i.shape
    laplacian = np.hstack((apple_i[:,0:int(cols)//2], orange_i[:, int(cols)//2:]))
    apple_orange_pyramid.append(laplacian)

# 5) Finally from this joint image pyramids, reconstruct the original image
apple_orange_reconstruct = apple_orange_pyramid[0]
for i in range(1,6):
    apple_orange_reconstruct = cv2.pyrUp(apple_orange_reconstruct)
    apple_orange_reconstruct = cv2.add(apple_orange_pyramid[i], apple_orange_reconstruct)

cv2.imshow('apple', apple)
cv2.imshow('orange', orange)
cv2.imshow('apple_orange', apple_orange)
cv2.imshow('apple_orange_reconstruct', apple_orange_reconstruct)
cv2.waitKey(0)
cv2.destroyAllWindows()