import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('j.png',0)

# OpenCV uses BGR format by default, while matplotlib.pyplot.imshow() expects RGB.
img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
#kernel = np.ones((9,9),np.uint8)
# Small holes might persist if your kernel is too small. Try using a larger kernel, like 9×9 or even 11×11
kernel = np.ones((11,11),np.uint8)
tophat = cv2.morphologyEx(img, cv2.MORPH_TOPHAT, kernel)
tophat_rgb = cv2.cvtColor(tophat, cv2.COLOR_BGR2RGB)

plt.subplot(121),plt.imshow(img_rgb),plt.title('Original')
plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(tophat_rgb),plt.title('Top Hat')
plt.xticks([]), plt.yticks([])
plt.show()