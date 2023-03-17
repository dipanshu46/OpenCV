import cv2

my_cam = cv2.VideoCapture(0)

# Each property has an integer representation which can be used insted of the full name of the property
# cv2.CAP_PROP_FRAME_WIDTH attribute is mapped with 3
# cv2.CAP_PROP_FRAME_WIDTH attribute is mapped with 4
print(my_cam.get(cv2.CAP_PROP_FRAME_WIDTH))
print(my_cam.get(cv2.CAP_PROP_FRAME_HEIGHT))

# Set method is used to set properties.
my_cam.set(cv2.CAP_PROP_FRAME_WIDTH, 700)
my_cam.set(cv2.CAP_PROP_FRAME_HEIGHT, 700) 

print(my_cam.get(cv2.CAP_PROP_FRAME_WIDTH))
print(my_cam.get(cv2.CAP_PROP_FRAME_HEIGHT))

while my_cam.isOpened():
    ret, frame = my_cam.read()
    cv2.imshow('Live Feed', frame)

    if cv2.waitKey(1)==ord('q'):
        break

my_cam.release()
cv2.destroyAllWindows()