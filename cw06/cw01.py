import os

import cv2
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np

img = cv2.imread(os.path.dirname(os.path.abspath(".")) + "\images" + "\lena.jpg", 0)
plt.hist(img.ravel(), 256, [0, 256])
plt.title("Grey")
plt.show()

img = cv2.imread(os.path.dirname(os.path.abspath(".")) + "\images" + "\lena.jpg", 1)
plt.hist(img.ravel(), 256, [0, 256])
plt.title("RGB")
plt.show()
