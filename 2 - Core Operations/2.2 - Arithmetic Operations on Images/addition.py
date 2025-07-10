import cv2
import numpy as np 
 
x = np.uint8([250])
y = np.uint8([10])

print(x)                # [250]
print(y)                # [10]

print(cv2.add(x,y)
'''
[[260.]
 [  0.]
 [  0.]
 [  0.]]
'''

print(x+y)              # [4] because 250+10 = 260 % 256 = 4

'''
Note: Thereis adifference between OpenCVaddition and Numpyaddition. 
OpenCVaddition is a saturated operation
while Numpy addition is a modulo operation.
'''