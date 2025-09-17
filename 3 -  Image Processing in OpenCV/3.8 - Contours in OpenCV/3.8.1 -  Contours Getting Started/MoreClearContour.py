import numpy as np
import cv2

im = cv2.imread('hand.jpg')
imgray = cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)

# Apply Gaussian Blur. This reduces noise and smooths the image:
imgray = cv2.GaussianBlur(imgray, (5, 5), 0)
ret,thresh = cv2.threshold(imgray,127,255,0)

# A version of cv2.findContours() that applies to OpenCV 3.x, where it returns three values: image, contours, and hierarchy. 
# However, in OpenCV 4.x and later, the function returns only two values: contours and hierarchy.


# Use Adaptive Thresholding or Canny Edge Detection.
edges = cv2.Canny(imgray, 100, 200)
contours, hierarchy = cv2.findContours(edges, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

# To draw all the contours in an image:
MoreClearContour = cv2.drawContours(im, contours,-1, (0,255,0), 3)
cv2.imwrite('MoreClearContour.jpg', MoreClearContour)
