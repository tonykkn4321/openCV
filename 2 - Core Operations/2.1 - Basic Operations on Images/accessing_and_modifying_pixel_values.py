import cv2
import numpy as np

img = cv2.imread('messi5.jpg')
px = img[100,100]
print(px)

# accessing only blue pixel
blue = img[100,100,0]
print(blue)

# modify the pixel values
img[100,100] = [255,255,255]
print(img[100,100]) 

# accessing RED value
print(img.item(10,10,2))

# modifying RED value
img[10, 10, 2] = 100
print(img.item(10,10,2))