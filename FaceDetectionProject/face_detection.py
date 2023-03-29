'''
Face Detection using Haar Cascade classifiers -
    is an effective object detection method proposed by Paul Viola and Micheal Jones in their paper. It is a machine learning bases approach where a cascade function is trained for a lot of positive and negative images. 
    First, a classifier (namely a cascade boosted classifiers working with Haar like features) is trained with a few hundred sample views of a particular object (i.e., a face or a car), called positive examples, that are scaled to the same size (say, 20x20), and negative examples - arbitrary images of the same size.

    Procedural Syntax:-
    objects = cv2.CascadeClassifier.detectMutliScale(image, scaleFactor, minNeighbors) where, 
    image        - Matrix of the type CV_8U containing an image where objects are detected.
    objects      - Vector of rectangles where each rectangle contains the detected object, the rectangles may be partially outside the original image.
    scaleFactor  - Parameters specifying how much the image size is reduced at each image scale.
    minNeighbors - Parameters specifying how many neighbors each candidate rectangle should have to retain it. 
'''

import cv2

# method to take cascades cv2.CascadeClassifier()
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
img = cv2.imread('faces.jpeg', 1)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Now to get faces from an image can be taken using the cascade ouput. 
# Syntax face_cascade.detectMultiScale(image, scaleFactor=None, minNeighbors=None, flags=None, minSize=None)
faces = face_cascade.detectMultiScale(gray, 1.1, 4)

for (x, y, w, h) in faces:
    cv2.rectangle(img, (x,y), (x+w, y+h), (255,0,0), 2)

cv2.imshow('Image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()