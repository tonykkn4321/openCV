import cv2
import numpy as np

img = cv2.imread('lightning.png')
img_gray = cv2.imread('lightning.png', 0)
ret, thresh = cv2.threshold(img_gray, 127, 255, 0)
contours, hierarchy = cv2.findContours(thresh, 1, 2)
cnt = contours[0]

rect = cv2.minAreaRect(cnt)
box = cv2.boxPoints(rect)
box = np.intp(box)  # np.int0 has been deprecated. Use np.int or np.int32 instead of np.int0
img = cv2.drawContours(img, [box], 0, (0, 0, 255), 2)  

cv2.imwrite('7b_Rotated_Rectangle.png', img)
