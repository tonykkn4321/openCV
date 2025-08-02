import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('j.png',0)
# OpenCV uses BGR format by default, while matplotlib.pyplot.imshow() expects RGB.
img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
kernel = np.ones((5,5),np.uint8)
dilation = cv2.dilate(img,kernel,iterations = 1)
dilation_rgb = cv2.cvtColor(dilation, cv2.COLOR_BGR2RGB)

plt.subplot(121),plt.imshow(img_rgb),plt.title('Original')
plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(dilation_rgb),plt.title('Dilated')
plt.xticks([]), plt.yticks([])
plt.show()