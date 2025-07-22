import cv2
import numpy as np

img = cv2.imread('messi5.jpg')
img_gray = cv2.imread('messi5.jpg',0)
rows,cols = img_gray.shape

M = cv2.getRotationMatrix2D((cols/2,rows/2),90,1)
dst = cv2.warpAffine(img,M,(cols,rows))

cv2.imshow('img',dst)
cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.imwrite('rotation.jpg',dst)