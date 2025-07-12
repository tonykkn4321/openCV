import cv2
import numpy as np 

# Load two images
img1 = cv2.imread('messi5.jpg')
img2 = cv2.imread('opencv_logo_white.jpg')

# I want to put logo on top-left corner, So I create a ROI 
rows,cols,channels = img2.shape
roi = img1[0:rows, 0:cols ]

# Convert logo to grayscale
img2gray = cv2.cvtColor(img2,cv2.COLOR_BGR2GRAY)
# Threshold to extract the non-white part of the image (i.e., the logo)
# Pixels below 250 are considered part of the logo; white (255) becomes black (0)
ret, mask = cv2.threshold(img2gray, 250, 255, cv2.THRESH_BINARY_INV)
# Create inverse mask for background removal
mask_inv = cv2.bitwise_not(mask)

# Now black-out the area of logo in ROI
img1_bg = cv2.bitwise_and(roi,roi,mask = mask_inv)

# Take only region of logo from logo image.
img2_fg = cv2.bitwise_and(img2,img2,mask = mask)

# Put logo in ROI and modify the main image
dst = cv2.add(img1_bg,img2_fg)
img1[0:rows, 0:cols ] = dst
cv2.imshow('res',img1)
cv2.waitKey(0)
cv2.destroyAllWindows()

