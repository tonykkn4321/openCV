import cv2
import numpy as np
from matplotlib import pyplot as plt

img=cv2.imread('opencv_logo.png')

# Specify the width and height of the kernel which should be positive and odd
#blur = cv2.GaussianBlur(img,(5,5),0)
blur = cv2.GaussianBlur(img,(15,15),0)

plt.subplot(121),plt.imshow(img),plt.title('Original')
plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(blur),plt.title('Blurred')
plt.xticks([]), plt.yticks([])
plt.show()
