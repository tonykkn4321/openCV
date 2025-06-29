import cv2
import numpy as np

# Create a black image
img = np.zeros((512,512,3), np.uint8)

# Create a white image
#img = np.ones((512,512,3), np.uint8)*255

# Draw a diagonalblue line with thickness of 5 px
img = cv2.line(img,(0,0),(511,511),(255,0,0),5)

# To draw a rectangle, you need top-left corner and bottom-right corner of rectangle. 
# This time we will draw a green  rectangle at the top-right corner of image.
img = cv2.rectangle(img,(384,0),(510,128),(0,255,0),3)

# To draw a circle, you need its center coordinates and radius.
# We will draw a circle inside the rectangle drawn above.
img = cv2.circle(img,(447,63), 63, (0,0,255),-1)

# Draw a half ellipse at the center of the image
img = cv2.ellipse(img,(256,256),(100,50),0,0,180,255,-1)

# Draw a small polygon of with four vertices in yellow color
pts = np.array([[10,5],[20,30],[70,20],[50,10]], np.int32)
pts = pts.reshape((-1,1,2))
img = cv2.polylines(img,[pts],True,(0,255,255))

cv2.imshow("image", img)
cv2.waitKey(0)
cv2.destroyAllWindows()