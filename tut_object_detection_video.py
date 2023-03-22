'''Object Detection on video is similar to that of on an image'''

import numpy as np
import cv2

def nothing(x):
    '''Function to receieve the call back from trackbar and do nothing'''
    pass

cam = cv2.VideoCapture(0)

cv2.namedWindow('Tracking')
cv2.createTrackbar('LH', 'Tracking', 0, 255, nothing)
cv2.createTrackbar('UH', 'Tracking', 255, 255, nothing)
cv2.createTrackbar('LS', 'Tracking', 0, 255, nothing)
cv2.createTrackbar('US', 'Tracking', 255, 255, nothing)
cv2.createTrackbar('LV', 'Tracking', 0, 255, nothing)
cv2.createTrackbar('UV', 'Tracking', 255, 255, nothing)

while True:
    _, frame = cam.read()
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    # Lower HSV values
    l_h = cv2.getTrackbarPos('LH', 'Tracking')
    l_s = cv2.getTrackbarPos('LS', 'Tracking')
    l_v = cv2.getTrackbarPos('LV', 'Tracking')
    # Upper HSV values
    u_h = cv2.getTrackbarPos('UH', 'Tracking')
    u_s = cv2.getTrackbarPos('US', 'Tracking')
    u_v = cv2.getTrackbarPos('UV', 'Tracking')
    # Actual lower bound and upper bound values from trackbars above
    l_b = np.array([l_h, l_s, l_v])
    u_b = np.array([u_h, u_s, u_v])
    # Create a mask for the image, use cv2.inRange(source_hsv, lowerbound, upperbound)
    mask = cv2.inRange(hsv, l_b, u_b)
    # Masking the mask on the frame to get the result 
    res = cv2.bitwise_and(frame, frame, mask=mask)

    # cv2.imshow('image', frame)
    # cv2.imshow('mask', mask)
    cv2.imshow('res', res)
    key = cv2.waitKey(1)
    if key == ord('q'):
        break

cam.release()
cv2.destroyAllWindows()