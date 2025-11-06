import cv2
import numpy as np

# Load images in grayscale
img = cv2.imread('star.png', 0)
img_A = cv2.imread('star.png', 0)
img_B = cv2.imread('image_B.png', 0)
img_C = cv2.imread('image_C.png', 0)

# Apply binary threshold
ret, thresh = cv2.threshold(img, 127, 255, 0)
ret_A, thresh_A = cv2.threshold(img_A, 127, 255, 0)
ret_B, thresh_B = cv2.threshold(img_B, 127, 255, 0)
ret_C, thresh_C = cv2.threshold(img_C, 127, 255, 0)

# Find contours in both images
contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
cnt = contours[0]

contours, hierarchy = cv2.findContours(thresh_A, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
cnt_A = contours[0]

contours, hierarchy = cv2.findContours(thresh_B, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
cnt_B = contours[0]

contours, hierarchy = cv2.findContours(thresh_C, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
cnt_C = contours[0]

# Compare shapes
mataching_A = cv2.matchShapes(cnt, cnt_A, cv2.CONTOURS_MATCH_I1, 0.0)
mataching_B = cv2.matchShapes(cnt, cnt_B, cv2.CONTOURS_MATCH_I1, 0.0)
mataching_C = cv2.matchShapes(cnt, cnt_C, cv2.CONTOURS_MATCH_I1, 0.0)

print("Matching Image A with itself:", mataching_A)
print("Matching Image A with Image B:", mataching_B)
print("Matching Image A with Image C:", mataching_C)