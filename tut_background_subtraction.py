import numpy as np
import cv2

# Method 1 - cv2.bgsegm.createBackgroundsubtractorMOG2()
cap = cv2.VideoCapture('data/vtest.avi')
fgbg = cv2.bgsegm.createBackgroundSubtractorMOG()

while cap.isOpened():
    ret, frame = cap.read()
    if frame is None:
        break
    
    # applying mask on frame
    fgmask = fgbg.apply(frame)
    cv2.imshow('Frame', frame)
    cv2.imshow('FG Mask Frame 1', fgmask)

    if cv2.waitKey(30)==ord('q'):
        break

cap.release()
cv2.destroyAllWindows()


# Method 2 - directly using createBackgroundsubtractorMOG2()
cap = cv2.VideoCapture('data/vtest.avi')
fgbg = cv2.createBackgroundSubtractorMOG2(detectShadows=False)

while True:
    ret, frame = cap.read()
    if frame is None:
        break
    
    # applying mask on frame
    fgmask = fgbg.apply(frame)
    cv2.imshow('Frame', frame)
    cv2.imshow('FG Mask Frame 2', fgmask)

    if cv2.waitKey(30)==ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

# Method 3 - using cv2.bgsegm.createBackgroundsubtractorGMG()
cap = cv2.VideoCapture('data/vtest.avi')
fgbg = cv2.bgsegm.createBackgroundSubtractorGMG()
kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (3,3))

while True:
    ret, frame = cap.read()
    if frame is None:
        break
    
    # applying mask on frame
    fgmask = fgbg.apply(frame)
    # we need to add a morphological operation on the mask to make it clearly visible
    fgmask = cv2.morphologyEx(fgmask, cv2.MORPH_OPEN, kernel)

    cv2.imshow('Frame', frame)
    cv2.imshow('FG Mask Frame 3', fgmask)

    if cv2.waitKey(30)==ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

# Method 4 - Background Subtractor knn method().
cap = cv2.VideoCapture('data/vtest.avi')
fgbg = cv2.createBackgroundSubtractorKNN(detectShadows=False)

while True:
    ret, frame = cap.read()
    if frame is None:
        break
    
    # applying mask on frame
    fgmask = fgbg.apply(frame)

    cv2.imshow('Frame', frame)
    cv2.imshow('FG Mask Frame 4', fgmask)

    if cv2.waitKey(30)==ord('q'):
        break

cap.release()
cv2.destroyAllWindows()