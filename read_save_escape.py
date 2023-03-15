import cv2 as cv

img = cv.imread('Lena.png', 1)

print("Press Esc to exit\nPress s to save as\n")
cv.imshow('image',img)
k = cv.waitKey(0) & 0xFF        # to take the keyboard interrupt key into a variable k
# cv.destroyAllWindows()
# print(k)        # printing k value which is the ascii value of the key pressed

if k == 27:         # Ascii value for Esc
    cv.destroyAllWindows()
elif k==115:        # Ascii value for s
    name = input("Enter file name to save: ")
    if '.' in name:
        cv.imwrite(name, img)
    cv.imwrite(name+'.jpg', img)
    cv.destroyAllWindows()

cv.destroyAllWindows()