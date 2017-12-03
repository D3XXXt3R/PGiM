import os

import cv2
import matplotlib.pyplot as plt


def showBinary():
    img_gray = cv2.imread(os.path.dirname(os.path.abspath(".")) + "\images" + "\lena.jpg", cv2.IMREAD_GRAYSCALE)
    ret, thresh = cv2.threshold(img_gray, 127, 255, cv2.THRESH_TOZERO)
    plt.imshow(thresh, 'gray')
    plt.title("Binary with range")
    plt.show()

showBinary()
