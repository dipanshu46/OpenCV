'''
Hough Transform basics - 
    The hough transform is a popular technique to detect any shape, if you can represent that shape in a mathematical form. It can detect the shape even if it is broken or distorted a little bit.

    - A line in the image space can be expressed with two variables. For example

    i) In the cartesian coordinate system. yi = mxi + c
    ii) In the Polar coordinate system xcoso + ysino = r

We'll use the polar coordinate system as the cartesian coordinate system cannot represent vertical lines.

Hough Transform Algorithm - 
    1) Edge Detection using canny edge detector
    2) Mapping of edge points to the Hough space and storage in an accumulator.
    3) Interpretation of accumulator to yield lines of infinite length. The interpretation is done by thresholding and possibly other constraints.
    4) Conversion of infinite lines to finite lines.

OpenCV implements two kind of Hough Line Transforms - 
    1) The Standard Hough Transform (HoughLines method)
    2) The Probabilistic Hough Transform (HoughLinesP Method)
'''

import cv2
import numpy as np

img = cv2.imread('data/sudoku.png')
# Converting the image to grey to find edges easily
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# Finding edges using Canny Edge Detection
edges = cv2.Canny(gray, 50, 150, apertureSize=3)
cv2.imshow('Edges', edges)
# Finding lines using HoughLines method
# Syntax: cv2.HoughLines(image, rho, theta, threshold)
# where, 
# image = source image
# rho = Distance resolution of the accumulator in pixels.
# theta = Angle resolution of the accumulator in radians.
# threshold = Accumulator threshold Parameter. Only those lines are returned that get enough votes. (>threshold)
# It returns vector of lines. Each line is represented by a 2 or 3 element vector (p,theta) or (p,theta, votes). p is the distance from the coordinate origin (0,0) (top-left corner of the image). theta is the line rotation angle in radians. votes is the value of accumulator.

lines = cv2.HoughLines(edges, 1, np.pi/180, 200)
# print(lines)

for line in lines:
    rho, theta = line[0]
    # Converting the polar points to cartesian lines.
    a = np.cos(theta)
    b = np.sin(theta)
    x0 = a*rho
    y0 = b*rho
    # x1 stores the rounded off value of (r*cos(theta) - 1000*sin(theta))
    x1 = int(x0 + 1000 * (-b))
    # y1 stores the rounded off value of (r*sin(theta) + 1000*cos(theta))
    y1 = int(y0 + 1000 * (a))
    # x2 stores the rounded off value of (r*cos(theta) + 1000*sin(theta))
    x2 = int(x0 - 1000 * (-b))
    # y2 stores the rounded off value of (r*sin(theta) - 1000*cos(theta))
    y2 = int(y0 - 1000 * (a))
    img = cv2.line(img, (x1,y1), (x2,y2), (0,0,255), 2)

cv2.imshow('Image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()

# we can see that in this method with just 2 parameters also the result takes a lot of computations and it is not even correct or undesired. This problem will be solved in the next method.