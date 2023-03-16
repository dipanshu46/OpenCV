import cv2

vid = cv2.VideoCapture(0)     # Creating instance of default camera
f_width = vid.get(cv2.CAP_PROP_FRAME_WIDTH)      # accessing frame width of camera output
f_height = vid.get(cv2.CAP_PROP_FRAME_HEIGHT)    # accessing frame height of camera output
fourcc = cv2.VideoWriter_fourcc(*'mp4v')        # fourcc is four character code that specifies the data format. I am using mp4v for mp4 video codec.

# Create an instance of writing file using cv2.VideoWriter('filename', fourcc_code, FramesPerSecond, (frame_width, frame_height))
out = cv2.VideoWriter('data/my_cam.mp4', fourcc, 15, (640,480))   

while vid.isOpened():
    ret, frame = vid.read()

    # gray_frame = cv2.cvtcolor(frame, cv2.COLOR_BGR2GRAY)      # To change the color to grayscale

    if ret==True:
        out.write(frame)
        cv2.imshow('Live Feed', frame)

        if cv2.waitKey(1) == ord('q' or 'Q'):
            break

out.release()
vid.release()
cv2.destroyAllWindows()