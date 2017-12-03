import os

import cv2
import matplotlib.pyplot as plt


def showColor():
    img = cv2.imread(os.path.dirname(os.path.abspath(".")) + "\images" + "\lena.jpg", cv2.IMREAD_COLOR)
    ret, thresh = cv2.threshold(img, 127, 255, cv2.THRESH_TRUNC)
    plt.imshow(thresh, 'gray')
    plt.title("Color")
    plt.show()


def showBlack_White():
    img_gray = cv2.imread(os.path.dirname(os.path.abspath(".")) + "\images" + "\lena.jpg", cv2.IMREAD_GRAYSCALE)
    ret, thresh = cv2.threshold(img_gray, 127, 255, cv2.THRESH_TRUNC)
    plt.imshow(thresh, 'gray')
    plt.title('N;ack&White')
    plt.show()


showColor()
showBlack_White()
