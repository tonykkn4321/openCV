import cv2
import numpy as np 

img1 = cv2.imread('ml.png')
img2 = cv2.imread('opencv_logo.jpg')

'''
print(img1.shape)
print(img2.shape)
(250, 202, 3)
(249, 202, 3)

'''

img1 = img1[:249,:]

dst = cv2.add(img1,img2)

cv2.imshow('dst',dst)
cv2.waitKey(0)
cv2.destroyAllWindows()
