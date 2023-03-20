import cv2

img = cv2.imread('data/leuvenA.jpg', 1)

# To draw a simple line use cv2.line(img_source, start_point, end_point, colour(BGR format), thickness)
img = cv2.line(img, (0,0), (255,255), (0,255,0), 10)

# To draw an arrowed line use cv2.arrowedLine(img_source, start_point, end_point, color(BGR format), thickness)
img = cv2.arrowedLine(img, (0,255), (255,255), (255,0,0), 10)

# To draw a rectangle use cv2.rectangle(img_source, left_top_coordinates, right_bottom_coordinates, color(BGR Format), thickness)
img = cv2.rectangle(img, (384,200),(510,128), (0,0,255), 5)

# To draw a filled polygon just change the thickness to -1
img = cv2.rectangle(img, (384,200),(510,128), (0,255,5), -1)

# To draw a circle use cv2.circle(img, center_coordinate, radius, colour(BGR Format), thickness)
img = cv2.circle(img, (447,63), 63, (0,60,220), -1)

# To put text on an image use cv2.putText(img, text_string, start_coordinates, font_face, fontscale, colour(BGR Format), thickness, linetype)
font = cv2.FONT_HERSHEY_SIMPLEX
img = cv2.putText(img, 'OpenCV', (10,300), font, 6, (255,255,255), 10, cv2.LINE_AA)


cv2.imshow('image', img)

cv2.waitKey(0)
cv2.destroyAllWindows()