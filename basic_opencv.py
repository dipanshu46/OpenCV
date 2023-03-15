import cv2 as cv
# print(cv.__version__)       # to check the version of opencv

# to read an image
img = cv.imread('leuvenA.jpg', 1)
print(img)          # it will print the matrix of pixels read by opencv

# to display an image
cv.imshow('image', img)         

# cv.waitKey(5000)                # wait for 5 sec
cv.waitKey(0)                   # wait forever

# destroys all windows created by opencv
cv.destroyAllWindows()

# to write to a file using opencv
cv.imwrite('my_image.jpg', img)