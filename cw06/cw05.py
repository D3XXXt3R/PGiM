import os

import cv2
from matplotlib import pyplot as plt

COLOR = ('b', 'g', 'r')

img = cv2.imread(os.path.dirname(os.path.abspath(".")) + "\images" + "\kobieta.jpg")
img_ycrcb = cv2.cvtColor(img, cv2.COLOR_BGR2YCR_CB)
y, cr, cb = cv2.split(img_ycrcb)
cv2.equalizeHist(y, y)
img_ycrcb = cv2.merge((y, cr, cb))
img_equalized = cv2.cvtColor(img_ycrcb, cv2.COLOR_YCR_CB2BGR)

cv2.imshow("Kobieta", img_equalized)


def showPlot(img):
    for i, col in enumerate(COLOR):
        hist = cv2.calcHist([img], [i], None, [256], [0, 256])
        plt.plot(hist, color=col)
        plt.xlim([0, 256])
    plt.show()

showPlot(img_equalized)
