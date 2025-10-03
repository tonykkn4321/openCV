import cv2
import numpy as np

img = cv2.imread('lightning.png')
img_gray = cv2.imread('lightning.png', 0)
ret, thresh = cv2.threshold(img_gray, 127, 255, 0)
contours, hierarchy = cv2.findContours(thresh, 1, 2)
cnt = contours[0]

rows, cols = img.shape[:2]
vx, vy, x, y = [v.item() for v in cv2.fitLine(cnt, cv2.DIST_L2, 0, 0.01, 0.01)]
lefty = int((-x * vy / vx) + y)
righty = int(((cols - x) * vy / vx) + y)
img = cv2.line(img, (cols - 1, righty), (0, lefty), (0, 255, 0), 2)

cv2.imwrite('10._Fitting_a_Line.png', img)


'''
v2.fitLine returns NumPy arrays, and you're trying to use them directly in arithmetic operations,
and cast them to int without extracting scalar values.

This behavior is deprecated in NumPy 1.25 and will raise an error in future versions.

'''