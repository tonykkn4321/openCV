import cv2
import numpy as np

img = cv2.imread('lightning.png')
img_gray = cv2.imread('lightning.png', 0)
ret, thresh = cv2.threshold(img_gray, 127, 255, 0)
contours, hierarchy = cv2.findContours(thresh, 1, 2)
cnt = contours[0]

mask = np.zeros(img_gray.shape,np.uint8)
cv2.drawContours(mask,[cnt],0,255,-1)
pixelpoints = np.transpose(np.nonzero(mask))
#pixelpoints = cv2.findNonZero(mask)

print(pixelpoints)

'''
Here, two methods, one using Numpy functions, next one using OpenCV function (last commented line) are given to
do the same. Results are also same, but with a slight difference. Numpy gives coordinates in (row, column) format,
while OpenCV gives coordinates in (x,y) format. So basically the answers will be interchanged. Note that, row = x
and column = y.
'''