import cv2
import numpy as np

img = cv2.imread('data/sudoku.png', 1)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
edges = cv2.Canny(gray, 50, 150, apertureSize = 3)
cv2.imshow('edges', edges)
# Using cv2.HoughLinesP(image, rho, theta, threshold [,lines[,minLineLength[, maxLineGap]]])
# where, 
# rho = Distance resolution of the accumulator in pixels
# theta = Angle resolution of the accumulator in radians
# threshold = Accumulator threshold Parameter. Only those lines are returned that get enough votes. (>threshold)
# minLineLength = Minimum length of line. Line segments shorter than this are rejected.
# maxLineGap = Maximum allowed gap between line segments to treat them as single line.
# It returns vector of lines. Each line is represented by x1, y1, x2, y2 coordinates
lines = cv2.HoughLinesP(edges, 1, np.pi/180, 100, minLineLength=100, maxLineGap=10)
for line in lines:
    x1, y1, x2, y2 = line[0]
    cv2.line(img, (x1,y1), (x2,y2), (0,255,0), 2)

cv2.imshow('Image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()