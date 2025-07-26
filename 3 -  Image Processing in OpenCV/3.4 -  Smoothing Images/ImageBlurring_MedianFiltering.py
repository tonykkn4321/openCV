import cv2
import numpy as np
from matplotlib import pyplot as plt

# Read the original image
img = cv2.imread('opencv_logo.png')

# Convert image to RGB for matplotlib display
img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

# Create noisy image by adding salt-and-pepper noise
def add_salt_pepper_noise(image, amount):
    noisy = image.copy()
    total_pixels = image.shape[0] * image.shape[1]
    num_noise = int(amount * total_pixels)

    for _ in range(num_noise):
        y = np.random.randint(0, image.shape[0])
        x = np.random.randint(0, image.shape[1])
        # Randomly assign either salt or pepper
        if np.random.rand() < 0.5:
            noisy[y, x] = [255, 255, 255]  # salt
        else:
            noisy[y, x] = [0, 0, 0]        # pepper
    return noisy

# Add 50% noise
noisy_img = add_salt_pepper_noise(img, 0.5)

# Apply median filter with kernel size 5, the kernel size must be a positive odd integer
#denoised_img = cv2.medianBlur(noisy_img, 5)
#denoised_img = cv2.medianBlur(noisy_img, 15)
denoised_img = cv2.medianBlur(noisy_img, 3)

# Convert to RGB for matplotlib
noisy_rgb = cv2.cvtColor(noisy_img, cv2.COLOR_BGR2RGB)
denoised_rgb = cv2.cvtColor(denoised_img, cv2.COLOR_BGR2RGB)

# Display images
plt.subplot(131), plt.imshow(img_rgb), plt.title('Original')
plt.xticks([]), plt.yticks([])
plt.subplot(132), plt.imshow(noisy_rgb), plt.title('Noisy (50%)')
plt.xticks([]), plt.yticks([])
plt.subplot(133), plt.imshow(denoised_rgb), plt.title('Median Filter')
plt.xticks([]), plt.yticks([])
plt.show()
