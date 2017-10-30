import os

import cv2
import numpy as np
import matplotlib.pyplot as plt
from math import floor

image = cv2.imread(os.path.dirname(os.path.abspath(".")) + "\images" + "\wir.jpg", 0)


def lut_alg(image, B):
    LUT = []
    delta = (2 ** 8 / 2 ** B)
    for i in range(256):
        LUT.append(int(floor(max((i - (delta / 2) - 1 / delta), 0)) * delta + (delta / 2 - 1)))
    gray = np.zeros((image.shape[0], image.shape[1]), dtype=np.uint8)
    for row in range(len(image)):
        for col in range(len(image[row])):
            gray[row][col] = LUT[image[row][col]]
    return gray


outputImage = lut_alg(image, 6)

plt.imshow(outputImage)
plt.show()
