'''
Q. To display current date and time on live video.
'''

import time
import cv2

# Accessing camera resources
cam = cv2.VideoCapture(0)

# Printing Frame Width and Height
print('Frame Width:',cam.get(3))
print('Frame Height:',cam.get(4))

# Main Display loop
while cam.isOpened():
    ret, frame = cam.read()

    # Adding date and time text to frame (black background with white text)
    font = cv2.FONT_HERSHEY_COMPLEX_SMALL
    frame = cv2.rectangle(frame, (0,685), (610,720), (0,0,0), -1)
    frame = cv2.putText(frame, time.ctime(), (0,715), font, 2, (255,255,255), 2, cv2.LINE_AA)

    # Displaying output
    cv2.imshow('Live Feed', frame)

    # Exit if q is pressed
    if cv2.waitKey(1)==ord('q'):
        break

# Releasing resources and finishing up
cam.release()
cv2.destroyAllWindows()