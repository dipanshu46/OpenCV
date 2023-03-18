import numpy as np
import cv2

# Mouse events can be handled using cv2 library.

# List of available flags for mouse events :-

# ['EVENT_FLAG_ALTKEY', 'EVENT_FLAG_CTRLKEY', 'EVENT_FLAG_LBUTTON', 'EVENT_FLAG_MBUTTON', 'EVENT_FLAG_RBUTTON', 'EVENT_FLAG_SHIFTKEY', 'EVENT_LBUTTONDBLCLK', 'EVENT_LBUTTONDOWN', 'EVENT_LBUTTONUP', 'EVENT_MBUTTONDBLCLK', 'EVENT_MBUTTONDOWN', 'EVENT_MBUTTONUP', 'EVENT_MOUSEHWHEEL', 'EVENT_MOUSEMOVE', 'EVENT_MOUSEWHEEL', 'EVENT_RBUTTONDBLCLK', 'EVENT_RBUTTONDOWN', 'EVENT_RBUTTONUP']

# Flags can be searched using the below 2 lines of code after importing cv2.
# events = [i for i in dir(cv2) if 'EVENT' in i]
# print(events)

# update image function
def updateScreen(s,x,y,color):
    '''Function updates the screen'''
    global img
    font = cv2.FONT_HERSHEY_SIMPLEX
    img = cv2.putText(img, s, (x,y), font, 0.7, color, 2, cv2.LINE_AA)
    cv2.imshow('image', img)
    print()


# Creating event handler for our mouse.
def click_event(event, x,y, flags, param):
    '''Function to track events and perform an action based on the event'''
    global img
    if event == cv2.EVENT_LBUTTONDOWN:
        # Event tracker for left button click -> performs coordinates display action.
        print('X-axis:',x,' Y-axis:',y)
        strXY = str(x) + ', ' + str(y)
        updateScreen(strXY,x,y,(255,255,0))


    if event == cv2.EVENT_RBUTTONDOWN:
        # Event tracker for right button click -> performs BGR channel value display action.
        b = img[y,x,0]
        g = img[y,x,1]
        r = img[y,x,2]
        print('X-axis:',x,' Y-axis:',y)
        print('Red:',r,'Green:',g,'Blue:',b)
        text = str(r) + ', ' + str(g) + ', ' + str(b)
        updateScreen(text,x,y,(0,255,255))
        

# img = np.zeros((512,512,3), np.uint8)     # For black image
img = cv2.imread('data/leuvenA.jpg', 1)
cv2.imshow('image', img)

cv2.setMouseCallback('image', click_event)
cv2.waitKey(0)

cv2.destroyAllWindows() 