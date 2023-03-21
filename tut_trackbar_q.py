'''
Q. Create a trackbar for current position of the trackbar and display it on the image. Also create a trackbar to switch between grayscale and color image.
'''

import numpy as np
import cv2


cv2.namedWindow('image')
switch = 'color/gray'

def nothing(x):
    print(x)

cv2.createTrackbar('CP','image',10,400, nothing)
cv2.createTrackbar(switch,'image',0,1, nothing)

while True:
    img = cv2.imread('data/leuvenA.jpg',1)
    pos = cv2.getTrackbarPos('CP','image')
    font = cv2.FONT_HERSHEY_SIMPLEX
    img = cv2.putText(img, str(pos), (10,50), font, 4, (255,255,255), 4, cv2.LINE_AA)
    
    s = cv2.getTrackbarPos(switch, 'image')

    if s==0:
        pass
    else:
        img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    cv2.imshow('image',img)
    k = cv2.waitKey(1)
    if k == ord('q'):
        break

cv2.destroyAllWindows()