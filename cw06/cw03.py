import os

import cv2
from matplotlib import pyplot as plt

COLOR = ('b', 'g', 'r')

img = cv2.imread(os.path.dirname(os.path.abspath(".")) + "\images" + "\lena.jpg")
cv2.imshow("Lena", img)

img_ycrcb = cv2.cvtColor(img, cv2.COLOR_BGR2YCR_CB)
y, cr, cb = cv2.split(img_ycrcb)
cv2.normalize(y, y, 0, 255, cv2.NORM_MINMAX)
img_ycrcb = cv2.merge((y, cr, cb))
img_norm = cv2.cvtColor(img_ycrcb, cv2.COLOR_YCR_CB2BGR)
cv2.imshow("Lena Normalized", img_norm)


def showPlot(img):
    for i, col in enumerate(COLOR):
        hist = cv2.calcHist([img_norm], [i], None, [256], [0, 256])
        plt.plot(hist, color=col)
        plt.xlim([0, 256])
    plt.show()

showPlot(img_norm)
