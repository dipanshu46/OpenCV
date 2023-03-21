import cv2

img = cv2.imread('data/messi5.jpg', 1)
img2 = cv2.imread('data/opencv-logo.png', 1)

img2 = cv2.resize(img2, (img.shape[1], img.shape[0]))

# Add weighted method is used to specify the percentage intensity of both the images that are to be added.
# Intensity can vary between 0 to 1 for both.
# Syntax : addWeighted(img_src1, intensity_1, img_src2, intensity_2, scalar_value)
# scalar value is the value that changes the brightness of a pixels.
new = cv2.addWeighted(img, 1 , img2, .8, -20)
cv2.imshow('New Image', new)
cv2.waitKey(0)
cv2.destroyAllWindows()