import numpy as np
import cv2

im_1 = cv2.imread('hand.jpg')
im_2 = cv2.imread('hand.jpg')
imgray = cv2.cvtColor(im_1,cv2.COLOR_BGR2GRAY)
ret,thresh = cv2.threshold(imgray,127,255,0)

# A version of cv2.findContours() that applies to OpenCV 3.x, where it returns three values: image, contours, and hierarchy. 
# However, in OpenCV 4.x and later, the function returns only two values: contours and hierarchy.
contours, hierarchy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

# To draw all the contours in an image:
all_contours = cv2.drawContours(im_1, contours,-1, (0,255,0), 3)
cv2.imwrite('all_contours.jpg',all_contours)

# To draw an individual contour, say 4th contour:
cnt = contours[4]
contour_4 = cv2.drawContours(im_2, [cnt], 0, (0,255,0), 3)
cv2.imwrite('contour_4.jpg',contour_4)