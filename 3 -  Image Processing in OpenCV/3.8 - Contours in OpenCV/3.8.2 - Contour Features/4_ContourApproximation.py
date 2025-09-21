import cv2
import numpy as np

# Read the image in grayscale
img = cv2.imread('square.jpg', 0)

# Apply thresholding to get a binary image
ret, thresh = cv2.threshold(img, 127, 255, 0)

# Find contours in the binary image
contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

# Get the largest contour (more robust than just contours[0])
cnt = max(contours, key=cv2.contourArea)

# Try different epsilon values to find a 4-point approximation
approx = None
for i in range(1, 50):  # Try epsilon from 1% to 50%
    epsilon = i * 0.01 * cv2.arcLength(cnt, True)
    temp_approx = cv2.approxPolyDP(cnt, epsilon, True)
    if len(temp_approx) == 4:
        approx = temp_approx
        print(f"Found square with epsilon = {epsilon}")
        break

# If no 4-point contour is found, fall back to original approximation
if approx is None:
    print("Could not find a 4-point approximation. Using default epsilon.")
    epsilon = 0.01 * cv2.arcLength(cnt, True)
    approx = cv2.approxPolyDP(cnt, epsilon, True)

# Create a color image to draw the contours on
color_img = cv2.cvtColor(img, cv2.COLOR_GRAY2BGR)

# Draw the approximate contour in green
cv2.drawContours(color_img, [approx], -1, (0, 255, 0), 2)

# Save the image with the drawn contour
cv2.imwrite('4_ContourApproximation.png', color_img)
