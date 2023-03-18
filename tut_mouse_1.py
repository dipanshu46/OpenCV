'''
Program to create lines using mouse on an image (here a blank black image)
First create a circle at the first mouse click, then at the second mouse click join the points.
'''

import numpy as np
import cv2

# Creating a function to draw a circle
def drawCircle(x,y):
    '''Function to draw a circle at the given screen point'''
    global img
    img = cv2.circle(img,(x,y), 4, (0,0,255), -1)
    cv2.imshow('image', img)

# Creating a function to draw a line
def drawLine():
    '''Function to draw line connecting the last two points on the screen'''
    global img
    global points
    start = points[-2]
    end = points[-1]
    img = cv2.line(img, start, end, (0,255,0), 2)
    cv2.imshow('image', img)

# Creating a function to clear the screen
def clearScreen():
    '''Function to clear screen'''
    global img
    global points
    img = np.zeros((512,512,3), np.uint8)
    cv2.imshow('image', img)
    points = []

# Creating mouse event handler
def clickEvent(event, x,y, flags, param):
    '''Function to perform an action according to the event'''
    global points
    if event == cv2.EVENT_LBUTTONDOWN:
        # Event tracker for Leftbuttondown -> performs marking operations
        drawCircle(x,y)
        points.append((x,y))
        if len(points)>=2:
            drawLine()

    if event == cv2.EVENT_RBUTTONDOWN:
        # Event tracker for Rightbuttondown -> performs initialization i.e. clears screen
        clearScreen()
    
        

# Black image
img = np.zeros((512,512,3), np.uint8)

# Opening color image
# img = cv2.imread('data/leuvenA.jpg',1)

cv2.imshow('image', img)
points = []

# connecting mouse event call back with our mouse event handler
cv2.setMouseCallback('image', clickEvent)

cv2.waitKey(0)
cv2.destroyAllWindows()