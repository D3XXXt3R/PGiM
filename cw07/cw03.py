import os

import cv2
import matplotlib.pyplot as plt


def otsu():
    img = cv2.imread(os.path.dirname(os.path.abspath(".")) + "\images" + "\sudoku.jpg", cv2.IMREAD_GRAYSCALE)
    blur = cv2.GaussianBlur(img, (5, 5), 0)
    ret, thresh = cv2.threshold(blur, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    plt.imshow(thresh, 'gray')
    plt.title('Otsu')
    plt.show()

otsu()
