import numpy as np
import cv2

im = cv2.imread('hand.jpg')
imgray = cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)
ret,thresh = cv2.threshold(imgray,127,255,0)

# A version of cv2.findContours() that applies to OpenCV 3.x, where it returns three values: image, contours, and hierarchy. 
# However, in OpenCV 4.x and later, the function returns only two values: contours and hierarchy.
contours, hierarchy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)  # Approximation method changed from SIMPLE to NONE

# To draw all the contours in an image:
none_method = cv2.drawContours(im, contours,-1, (0,255,0), 3)
cv2.imwrite('none_method.jpg',none_method)
