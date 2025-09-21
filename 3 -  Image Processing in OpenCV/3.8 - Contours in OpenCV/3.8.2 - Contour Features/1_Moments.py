import cv2
import numpy as np

img = cv2.imread('star.jpg',0)
ret,thresh = cv2.threshold(img,127,255,0)
contours,hierarchy = cv2.findContours(thresh, 1, 2)
cnt = contours[0]

M = cv2.moments(cnt)
print(M)

# From this moments, you can extract useful data like area, centroid etc. 
# Centroid is given by the relations, Cx = M10/M00 and Cy = M01/M00. This can be done as follows:
cx = int(M['m10']/M['m00'])
cy = int(M['m01']/M['m00'])
print(f"\nThe centroid of the star is: cx={cx}, cy={cy}.")