import os

import cv2
import matplotlib.pyplot as plt
import numpy as np


def otsu():
    img = cv2.imread(os.path.dirname(os.path.abspath(".")) + "\images" + "\sudoku.jpg", cv2.IMREAD_GRAYSCALE)
    blur = cv2.GaussianBlur(img, (5, 5), 0)
    hist = cv2.calcHist([blur], [0], None, [256], [0, 256])
    hist_norm = hist.ravel() / hist.max()
    Q = hist_norm.cumsum()
    bins = np.arange(256)
    fn_min = np.inf
    for i in range(1, 256):
        # probabilities
        p1, p2 = np.hsplit(hist_norm, [i])

        # sum of classes
        q1, q2 = Q[i], Q[255] - Q[i]

        # weights
        b1, b2 = np.hsplit(bins, [i])

        # means and variances
        m1, m2 = np.sum(p1 * b1) / q1, np.sum(p2 * b2) / q2
        v1, v2 = np.sum(((b1 - m1) ** 2) * p1) / q1, np.sum(((b2 - m2) ** 2) * p2) / q2

        # minimization function
        fn = v1 * q1 + v2 * q2
        if fn < fn_min:
            fn_min = fn

    # OTSU
    ret, otsu = cv2.threshold(blur, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    plt.imshow(otsu, 'gray')
    plt.title('Otsu')
    plt.show()

otsu()
