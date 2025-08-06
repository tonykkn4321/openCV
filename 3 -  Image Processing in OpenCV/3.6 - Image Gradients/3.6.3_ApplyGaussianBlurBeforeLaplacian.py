import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('dave.jpg', 0)
if img is None:
    raise ValueError("Image not found. Check the path.")

# Apply edge detection
laplacian = cv2.Laplacian(img, cv2.CV_64F)
sobelx = cv2.Sobel(img, cv2.CV_64F, 1, 0, ksize=5)
sobely = cv2.Sobel(img, cv2.CV_64F, 0, 1, ksize=5)

# Laplacian is a second derivative operator, so it amplifies noise. Pre-blurring the image helps suppress that.
blurred = cv2.GaussianBlur(img, (3, 3), 0)
laplacian = cv2.Laplacian(blurred, cv2.CV_64F)
laplacian = cv2.convertScaleAbs(laplacian)
# cv2.GaussianBlur(img, (3, 3), 0) applies a 3×3 Gaussian kernel.
# You can try (5, 5) for stronger smoothing if needed.

# Convert to 8-bit for visualization
laplacian = cv2.convertScaleAbs(laplacian)
sobelx = cv2.convertScaleAbs(sobelx)
sobely = cv2.convertScaleAbs(sobely)

# Display results
plt.subplot(2,2,1), plt.imshow(img, cmap='gray')
plt.title('Original'), plt.xticks([]), plt.yticks([])
plt.subplot(2,2,2), plt.imshow(laplacian, cmap='gray')
plt.title('Laplacian'), plt.xticks([]), plt.yticks([])
plt.subplot(2,2,3), plt.imshow(sobelx, cmap='gray')
plt.title('Sobel X'), plt.xticks([]), plt.yticks([])
plt.subplot(2,2,4), plt.imshow(sobely, cmap='gray')
plt.title('Sobel Y'), plt.xticks([]), plt.yticks([])
plt.tight_layout()
plt.show()
