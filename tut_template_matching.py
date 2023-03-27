import cv2
import numpy as np

img = cv2.imread('data/messi5.jpg', 1)
grey_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
template = cv2.imread('data/messi_face.jpg',0)
w, h = template.shape[::-1]

# To check for templates to match in your image use cv2.matchTemplate(image, template, method, result=None, mask=None)
res = cv2.matchTemplate(grey_img, template, cv2.TM_CCOEFF_NORMED)
# It returns of a list of comparison of each possibility with the template.
# print(res)
# Different methods are available and might give better result than the other, so do try other template matching methods.

# To get the maximum number of similar pixels from a numpy array use np.where(condition)
threshold = 0.9
loc = np.where(res >= threshold)
print(loc)    # using where we got the coordinate the only two points where the templates are matching the maximum. 
# So now we we'll draw a rectangle starting from the coordinate of the already known height and width
for pt in zip(*loc[::-1]):
    cv2.rectangle(img, pt, (pt[0]+w, pt[1]+h), (0,255,0), 2)


cv2.imshow('image', img)
cv2.imshow('res', res)
cv2.waitKey(0)
cv2.destroyAllWindows()