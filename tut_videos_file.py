import cv2 as cv

vid_name = 'data/earth.mp4'
vid = cv.VideoCapture(vid_name)

# To get properties of your video you can use get method
f_width = vid.get(cv.CAP_PROP_FRAME_WIDTH)
f_height = vid.get(cv.CAP_PROP_FRAME_HEIGHT)
print("Frame width:",f_width)
print("Frame Height:",f_height)

while vid.isOpened():           # isOpened() method returns False if file name or device index entered is wrong or invalid.
    ret, frame = vid.read()
    cv.imshow(vid_name, frame)
    if cv.waitKey(1) == ord('q'):
        break

vid.release()
cv.destroyAllWindows()