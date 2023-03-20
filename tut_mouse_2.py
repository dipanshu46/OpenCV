'''
Program to display the colour of the point at which the mouse was clicked on a new window.
'''

import numpy as np
import cv2

# Creating a function to display the rgb color
def displayColor(x,y):
    '''Function to display the rgb color on a new window'''
    global img
    # reading colors of the point
    b = img[y,x,0]
    g = img[y,x,1]
    r = img[y,x,2]
    new_window = np.zeros((300,300,3), np.uint8)
    # Accessing each pixel and assigning bgr value to each pixel.
    new_window[:] = [b,g,r]
    cv2.imshow('color',new_window)

# Creating our mouse event handler
def clickEvent(event, x,y, flags, param):
    '''Function to perform actions according to the event'''
    
    if event == cv2.EVENT_LBUTTONDOWN:
        # Event tracker for left button down -> performs rgb channel on new window display action 
        displayColor(x,y)

# Opening image
img = cv2.imread('data/leuvenA.jpg', 1)
cv2.imshow('image', img)

# Connecting mouse event catcher with our mouse event handler
cv2.setMouseCallback('image', clickEvent)

cv2.waitKey(0)
cv2.destroyAllWindows()