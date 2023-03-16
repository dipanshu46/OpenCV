import cv2

cam_feed = cv2.VideoCapture(0)

while True:
    ret, frame = cam_feed.read()

    # converting color frame to grayscale
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    cv2.imshow('Live Cam', gray_frame)

    if cv2.waitKey(1) == ord('q' or 'Q'):
        break

cam_feed.release()
cv2.destroyAllWindows()