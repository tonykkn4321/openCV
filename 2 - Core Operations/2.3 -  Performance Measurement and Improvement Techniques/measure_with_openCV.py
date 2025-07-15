'''
e1 = cv2.getTickCount()
# your code execution
e2 = cv2.getTickCount()
time = (e2- e1)/ cv2.getTickFrequency()

'''

import cv2
import time

img1 = cv2.imread('messi5.jpg')

# Use cv2.getTickCount
e1 = cv2.getTickCount()
for i in range(5,49,2):
    img1 = cv2.medianBlur(img1,i)
e2 = cv2.getTickCount()
t = (e2- e1)/cv2.getTickFrequency()
print(t)

# Use time.time() function
e1 = time.time()
for i in range(5,49,2):
    img1 = cv2.medianBlur(img1,i)
e2 = time.time()
t = (e2- e1)
print(t)

