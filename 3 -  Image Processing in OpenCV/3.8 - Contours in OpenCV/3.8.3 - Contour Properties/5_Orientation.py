import cv2
import numpy as np

img = cv2.imread('lightning.png')
img_gray = cv2.imread('lightning.png', 0)
ret, thresh = cv2.threshold(img_gray, 127, 255, 0)
contours, hierarchy = cv2.findContours(thresh, 1, 2)
cnt = contours[0]

(x,y),(MA,ma),angle = cv2.fitEllipse(cnt)

print(angle)
