import cv2
import numpy as np

img = cv2.imread('star.png')
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
ret, thresh = cv2.threshold(img_gray, 127, 255, 0)
contours, hierarchy = cv2.findContours(thresh, 2, 1)
cnt = contours[0]

# This function finds the shortest distance between a point in the image and a contour. 
dist = cv2.pointPolygonTest(cnt,(50,50),True)
print(dist)
