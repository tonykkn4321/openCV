import cv2
import timeit

print(cv2.useOptimized())
# result: True


# Load image
img = cv2.imread('messi5.jpg')

def blur():
    cv2.medianBlur(img, 49)

duration = timeit.timeit(blur, number=10)
print(f"Average time over 10 runs: {duration / 10:.6f} seconds per loop")


# Disable it
cv2.setUseOptimized(False)
print(cv2.useOptimized())

duration = timeit.timeit(blur, number=10)
print(f"Average time over 10 runs: {duration / 10:.6f} seconds per loop")