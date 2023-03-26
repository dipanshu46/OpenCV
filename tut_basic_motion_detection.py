import cv2
import numpy as np

vid = cv2.VideoCapture('data/vtest.avi')

# Reading two frames from the video for comparison
ret, frame1 = vid.read()
ret, frame2 = vid.read()

while vid.isOpened():

    # finding difference between two frames.
    diff =  cv2.absdiff(frame1, frame2)
    # cv2.imshow('Difference', diff)

    # finding the edges of the objects found moving( edges of pixels that were changed in the two frames)
    edge = cv2.Canny(diff, 100,200)

    # Processing the edges to get a clear edge around the moving object by first, adding Gaussian Blur, second, thresholding, third, dilating the edges.
    edge = cv2.GaussianBlur(edge, (5,5), 0)
    _, edge = cv2.threshold(edge, 20, 255, cv2.THRESH_BINARY)
    edge = cv2.dilate(edge, None, iterations=2)
    # cv2.imshow('Edge', edge)

    # Finding the contours on the objects detected moving
    contours, _ = cv2.findContours(edge, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    # For drawing rectangles around the moving objects and for reducing noise such as moving ropes and other smaller movements.
    for contour in contours:
        
        # to get the coordinates of the contours use cv2.boundingRect(contour)  
        (x, y, w, h) = cv2.boundingRect(contour)

        # removing smaller contours as of ropes, so that only persons would be marked.
        if cv2.contourArea(contour) < 800:
            continue

        # Drawing Rectangle around the detected obect
        cv2.rectangle(frame1, (x,y), (x+w, y+h), (0,255,0), 2)

    # Drawing contours on the frames. (We don't want to draw these contours on the final frames so commenting it out)
    # cv2.drawContours(frame1, contours, -1, (0,255,0), 2)

    # Displaying the contours added on the original frames.
    cv2.imshow('Video', frame1)

    # Preparing next frames for the same operations as above
    frame1 = frame2
    ret, frame2 = vid.read()

    if cv2.waitKey(40) == ord('q') or ret == False:
        break

vid.release()
cv2.destroyAllWindows()