import os

import cv2
import matplotlib.pyplot as plt


def bernsen():
    img = cv2.imread(os.path.dirname(os.path.abspath(".")) + "\images" + "\sudoku.jpg", cv2.IMREAD_GRAYSCALE)
    ret, th = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    plt.imshow(th, 'gray')
    plt.title('Otsu + Bernsen')
    plt.show()


bernsen()
