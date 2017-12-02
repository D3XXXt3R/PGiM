import os

import cv2
import matplotlib.pyplot as plt

img = cv2.imread(os.path.dirname(os.path.abspath(".")) + "\images" + "\lena.jpg",0)
cv2.namedWindow('image2', cv2.WINDOW_NORMAL)
cv2.imshow('image2', img)

cv2.waitKey(0)
cv2.destroyAllWindows()
plt.hist(img.ravel(), 256, [0, 256])
plt.title("Before Contrast")
plt.show()

# create a CLAHE object (Arguments are optional).
clahe = cv2.createCLAHE(clipLimit=10.0, tileGridSize=(8,8))
cl1 = clahe.apply(img)
cv2.namedWindow('image2', cv2.WINDOW_NORMAL)
cv2.imshow('image2', cl1)

cv2.waitKey(0)
cv2.destroyAllWindows()
plt.hist(cl1.ravel(), 256, [0, 256])
plt.title("After Contrast")
plt.show()