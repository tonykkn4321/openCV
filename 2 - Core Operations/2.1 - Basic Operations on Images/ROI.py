import cv2
import numpy as np

img = cv2.imread('messi5.jpg')

ball = img[150:180, 175:205]
img[136:163, 50:80] = ball

cv2.namedWindow('image', cv2.WINDOW_NORMAL)
cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
