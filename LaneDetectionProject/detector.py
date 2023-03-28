'''
Lane Detector for images
Author : Dipanshu Singh
Date : March 28, 2023

NOTE: to give your image for test
'''

import sys
import cv2
import matplotlib.pylab as plt
import numpy as np

# Function to mask only the required area under observation and to discard noises.
def region_of_interest(img, vertices):
    '''Function to mask the region of interest on the image using vertices'''
    # np.zeros_like(img) method creates a numpy array similar to the array provided (here image array).
    mask = np.zeros_like(img)
    # channel_count = img.shape[2]
    # match_mask_color = (255,) * channel_count
    match_mask_color = (255)
    # use cv2.fillPoly(img_source, vertices, match_mask_color)
    cv2.fillPoly(mask, vertices, match_mask_color)
    masked_image = cv2.bitwise_and(img, mask)
    return masked_image

def draw_lines(img, lines):
    '''Function to draw the detected lines on the original image'''
    img = np.copy(img)
    blank_image = np.zeros((img.shape[0], img.shape[1], 3), dtype=np.uint8)
    for line in lines:
        x1, y1, x2, y2 = line[0]
        cv2.line(blank_image, (x1,y1), (x2,y2), (0,255,0), 2)

    img = cv2.add(img,blank_image)
    return img

def input_image():
    '''Function to take input from the user while running the code, if not passing self image.'''
    try:
        img = cv2.imread(sys.argv[1])
    except:
        img = cv2.imread('road.jpeg') 
    
    return img

def main():
    '''Main Body'''
    img = input_image()
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    # print(img.shape)
    height = img.shape[0]
    width = img.shape[1]

    # Creating a list of vertices for region of interest.
    roi_vertices = [
        (0,height),
        (0,613),
        (width/2, 400),
        (width,614),
        (width,height)
    ]

    # image from which lane will be detected
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    edges = cv2.Canny(gray, 100, 200, apertureSize = 3)
    masked_image = region_of_interest(edges, np.array([roi_vertices], np.int32))
    lines = cv2.HoughLinesP(masked_image, 2, np.pi/180, 200, lines=np.array([]), minLineLength=40, maxLineGap=25)
    line_img = draw_lines(img, lines)
    plt.imshow(line_img)
    plt.show()

# Driver Code
main()