'Trackbar is a slider on window pane'

import numpy as np
import cv2 as cv

img = np.zeros((300,512,3), np.uint8)
cv.namedWindow('image')         # method used to create a named window.
switch = "0: OFF\n1: ON"

# Creating a call back function for Trackbar
def changeColour(x):
    '''Function to change the bgr value of the image'''
    print(x)
    

# createTrackbar() method is used to create a trackbar.
# Syntax : createTrackbar('trackbar_name','window_name', range_starting_point, range_end_point, call_back_function_name)
cv.createTrackbar('B', 'image', 0, 255, changeColour)
cv.createTrackbar('G', 'image', 0, 255, changeColour)
cv.createTrackbar('R', 'image', 0, 255, changeColour)
cv.createTrackbar(switch, 'image', 0, 1, changeColour)

while True:
    cv.imshow('image', img)
    
    # getTrackbarPos() is used to get the trackbar position or the value it is at right now.
    # Syntax : cv.getTrackbarPos('trackbar_name', 'window_name')
    b = cv.getTrackbarPos('B','image')
    g = cv.getTrackbarPos('G','image')
    r = cv.getTrackbarPos('R','image')
    s = cv.getTrackbarPos(switch, 'image')
    if s==0:
        img[:] = 0
    else:
        img[:] = [b,g,r]
    k = cv.waitKey(1)
    if k == ord('q'):
        break

cv.destroyAllWindows()