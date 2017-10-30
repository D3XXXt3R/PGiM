import os

import cv2
import numpy as np


def rgb2ycbcr(im):
    xform = np.array([[.299, .587, .114], [-.1687, -.3313, .5], [.5, -.4187, -.0813]])
    ycbcr = im.dot(xform.T)
    ycbcr[:, :, [1, 2]] += 128
    return np.uint8(ycbcr)


image1 = cv2.imread(os.path.dirname(os.path.abspath(".")) + "\images" + "\lena.jpg")
cv2.imshow("ycbr", rgb2ycbcr(image1))
cv2.waitKey(0)
cv2.destroyAllWindows()
