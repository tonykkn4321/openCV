import cv2
import numpy as np
from matplotlib import pyplot as plt

img=cv2.imread('Bilateral-Filtering-Image.jpg')

# OpenCV uses BGR format by default, while matplotlib.pyplot.imshow() expects RGB.
img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
blur = cv2.bilateralFilter(img,9,75,75)
blur_rgb = cv2.cvtColor(blur, cv2.COLOR_BGR2RGB)

plt.subplot(121),plt.imshow(img_rgb),plt.title('Original')
plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(blur_rgb),plt.title('Blurred')
plt.xticks([]), plt.yticks([])
plt.show()
