import os

import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread(os.path.dirname(os.path.abspath(".")) + "\images" + "\lena.jpg", cv2.IMREAD_UNCHANGED)
cv2.namedWindow('image', cv2.WINDOW_NORMAL)
cv2.imshow('image', img)

img2 = cv2.imread(os.path.dirname(os.path.abspath(".")) + "\images" + "\statek.jpg", cv2.IMREAD_UNCHANGED)
cv2.namedWindow('image2', cv2.WINDOW_NORMAL)
cv2.imshow('image2', img2)

cv2.waitKey(0)
cv2.destroyAllWindows()

# using matploit

# img3 = cv2.imread('lena.jpg',1)
# plt.imshow(cv2.cvtColor(img3, cv2.COLOR_BGR2RGB))
# plt.axis("off")
# plt.show()
