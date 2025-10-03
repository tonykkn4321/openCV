import cv2
import numpy as np

img = cv2.imread('lightning.png')
img_gray = cv2.imread('lightning.png', 0)
ret, thresh = cv2.threshold(img_gray, 127, 255, 0)
contours, hierarchy = cv2.findContours(thresh, 1, 2)
cnt = contours[0]

# Create a mask of zeros (same size as grayscale image)
mask = np.zeros(img_gray.shape, dtype=np.uint8)

# Draw the contour on the mask
cv2.drawContours(mask, [cnt], -1, 255, -1)  # Fill the contour area with white

# Now use the mask with minMaxLoc
min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(img_gray, mask=mask)

print(f'Minimum value: {min_val} & its location is at {min_loc}.')
print(f'Maximum value: {max_val} & its location is at {max_loc}.')
