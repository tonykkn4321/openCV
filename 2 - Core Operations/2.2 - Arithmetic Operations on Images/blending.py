import cv2
import numpy as np 

img1 = cv2.imread('ml.png')
img2 = cv2.imread('opencv_logo.jpg')

'''
print(img1.shape)
print(img2.shape)
(250, 202, 3)
(258, 195, 3)

'''

img1 = img1[:,:195]
img2 = img2[:250,:]

dst = cv2.addWeighted(img1,0.7,img2,0.3,0)

cv2.imshow('dst',dst)
cv2.waitKey(0)
cv2.destroyAllWindows()

