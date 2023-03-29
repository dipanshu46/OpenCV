import cv2

def detectFaces(img):
    '''Function to detect faces on a frame'''
    face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
    frame = img
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(gray, 1.1, 4)

    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x,y), (x+w, y+h), (255,0,0), 2)

    return frame

def main():
    '''Main body'''
    vid = cv2.VideoCapture(0)

    while vid.isOpened():
        ret, frame = vid.read()
        output = detectFaces(frame)
        cv2.imshow('Faces', output)
        if cv2.waitKey(50)==ord('q'):
            break
    
    vid.release()
    cv2.destroyAllWindows()


# Driver Code
main()