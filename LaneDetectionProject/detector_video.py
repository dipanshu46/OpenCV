import cv2 
import numpy as np

def region_of_interest(img, vertices):
    '''Function to mask the region of interest on the image using vertices'''
    mask = np.zeros_like(img)
    # channel_count = img.shape[2]
    # match_mask_color = (255,) * channel_count
    match_mask_color = (255)
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

def main(frame):
    '''Main Body'''
    img = frame
    
    # print(img.shape)
    height = img.shape[0]
    width = img.shape[1]

    # Creating a list of vertices for region of interest.
    roi_vertices = [
        (0,height),
        (0,height-70),
        (width/2, height/2 + 30),
        (width,height-80),
        (width,height)
    ]

    # image from which lane will be detected
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    edges = cv2.Canny(gray, 120, 130, apertureSize = 3)
    masked_image = region_of_interest(edges, np.array([roi_vertices], np.int32))
    lines = cv2.HoughLinesP(masked_image, 2, np.pi/180, 100, lines=np.array([]), minLineLength=40, maxLineGap=100)
    try:
        if lines.any()!=None:
            line_img = draw_lines(img, lines)
            return line_img
    except:
        return img

# Driver Code
vid = cv2.VideoCapture('road.mp4')
ret, frame = vid.read()
print(frame.shape)

while vid.isOpened():
    ret, frame = vid.read()
    if ret == False:
        break
    frame = main(frame)
    cv2.imshow('Lane Detection', frame)

    if cv2.waitKey(100)==ord('q'):
        break

vid.release()
cv2.destroyAllWindows()