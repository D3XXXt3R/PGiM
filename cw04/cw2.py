import os

import cv2
import numpy as np
import cw04.cw1


def ycbcr2rgb(im):
    xform = np.array([[1, 0, 1.402], [1, -0.34414, -.71414], [1, 1.772, 0]])
    rgb = im.astype(np.float)
    rgb[:, :, [1, 2]] -= 128
    return np.uint8(rgb.dot(xform.T))


image1 = cv2.imread(os.path.dirname(os.path.abspath(".")) + "\images" + "\lena.jpg")
cv2.imshow("rgb", ycbcr2rgb(cw04.cw1.rgb2ycbcr(image1)))
cv2.waitKey(0)
cv2.destroyAllWindows()
