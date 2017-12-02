import os

import cv2
import numpy as np
from matplotlib import pyplot as plt

COLOR = ('b', 'g', 'r')

img = cv2.imread(os.path.dirname(os.path.abspath(".")) + "\images" + "\lena.jpg")
image_ycrcb = cv2.cvtColor(img, cv2.COLOR_BGR2YCR_CB)
cv2.imshow("Lena", img)

y, cr, cb = cv2.split(image_ycrcb)
cv2.equalizeHist(y, y);
image_ycrcb = cv2.merge((y, cr, cb))
image_equalized = cv2.cvtColor(image_ycrcb, cv2.COLOR_YCR_CB2BGR)

cv2.imshow("Lena Equalized", image_equalized)


def showPlot(img):
    for i, col in enumerate(COLOR):
        hist = cv2.calcHist([img], [i], None, [256], [0, 256])
        plt.plot(hist, color=col)
        plt.xlim([0, 256])
    plt.show()


showPlot(image_equalized)
