import cv2
import numpy as np

img = cv2.imread('messi5.jpg')

b,g,r = cv2.split(img)
img[:,:,2] = 0
img2 = cv2.merge((b,g,r))

cv2.namedWindow('image', cv2.WINDOW_NORMAL)
cv2.namedWindow('image2', cv2.WINDOW_NORMAL)
cv2.imshow('image', img)
cv2.imshow('image2', img2)
cv2.waitKey(0)
cv2.destroyAllWindows()
