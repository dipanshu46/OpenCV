import numpy as np
import cv2

# Shi Tomasi is better than Harris Corner detector as we can also decide the number of corners we want which is required in some conditions

img = cv2.imread('data/pic1.png')
# Converting image to gray scale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# Since the paper published by Shi and Tomasi was Good Features To Track, therefore the name of the method is also the same.
# cv2.goodFeaturesToTrack(iamge, max_corners, qulatiy_level, minDist) 
corners = cv2.goodFeaturesToTrack(gray, 100, 0.01, 10)
# after finding all the corners we need to convert it into int 64. int0 is just an alias for int64.
corners = np.int0(corners)
# After completing the above step we iterate over the corners and get the value of x and y.
for i in corners:
    x, y = i.ravel()
    cv2.circle(img ,(x, y), 3, 255, -1)

cv2.imshow('dst', img)

cv2.waitKey(0)
cv2.destroyAllWindows()