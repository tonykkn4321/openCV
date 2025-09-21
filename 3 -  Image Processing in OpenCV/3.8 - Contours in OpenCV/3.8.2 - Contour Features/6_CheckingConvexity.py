import cv2
import numpy as np

# Load the image in color
color_img = cv2.imread('hand.jpg', cv2.IMREAD_COLOR)

# Convert to grayscale for processing
gray = cv2.cvtColor(color_img, cv2.COLOR_BGR2GRAY)

# Apply adaptive thresholding
thresh = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
                               cv2.THRESH_BINARY_INV, 11, 2)

# Morphological operations
kernel = np.ones((5, 5), np.uint8)
morph = cv2.morphologyEx(thresh, cv2.MORPH_CLOSE, kernel)
morph = cv2.morphologyEx(morph, cv2.MORPH_OPEN, kernel)

# Find contours
contours, _ = cv2.findContours(morph, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
contours = [c for c in contours if cv2.contourArea(c) > 5000]

if not contours:
    print("No valid contour found.")
    exit()

# Largest contour
cnt = max(contours, key=cv2.contourArea)

# Convex hull (for defects, returnPoints=False)
hull = cv2.convexHull(cnt, returnPoints=False)

# Find convexity defects
defects = cv2.convexityDefects(cnt, hull)

# Draw original contour in blue
cv2.drawContours(color_img, [cnt], -1, (255, 0, 0), 2)

# Draw convex hull in green
cv2.drawContours(color_img, [cv2.convexHull(cnt)], -1, (0, 255, 0), 2)

# Draw convexity defects in red
if defects is not None:
    for i in range(defects.shape[0]):
        s, e, f, d = defects[i, 0]
        start = tuple(cnt[s][0])
        end = tuple(cnt[e][0])
        far = tuple(cnt[f][0])
        cv2.circle(color_img, far, 5, (0, 0, 255), -1)  # Red dot at defect point

# Check if a curve is convex or not, cv2.isContourConvex(). It just return whether True or False.
k = cv2.isContourConvex(cnt)
print(k)
