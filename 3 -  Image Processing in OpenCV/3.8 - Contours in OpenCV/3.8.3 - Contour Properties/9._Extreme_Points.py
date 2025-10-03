import cv2
import numpy as np

img = cv2.imread('lightning.png')
img_gray = cv2.imread('lightning.png', 0)
ret, thresh = cv2.threshold(img_gray, 127, 255, 0)
contours, hierarchy = cv2.findContours(thresh, 1, 2)
cnt = contours[0]

leftmost = tuple(int(v) for v in cnt[cnt[:, :, 0].argmin()][0])
rightmost = tuple(int(v) for v in cnt[cnt[:, :, 0].argmax()][0])
topmost = tuple(int(v) for v in cnt[cnt[:, :, 1].argmin()][0])
bottommost = tuple(int(v) for v in cnt[cnt[:, :, 1].argmax()][0])

print(f'Leftmost: {leftmost}')
print(f'Rightmost: {rightmost}')
print(f'Topmost: {topmost}')
print(f'Bottommost: {bottommost}')
