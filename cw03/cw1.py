import os

import cv2


def incr_pixel(val):
    img3 = cv2.imread(os.path.dirname(os.path.abspath(".")) + "\images" + "\lena.jpg", 1)
    for i in img3:
        for j in i:
            j += val
    return img3


cv2.namedWindow('image2', cv2.WINDOW_NORMAL)
cv2.imshow('image2', incr_pixel(50))
cv2.waitKey(0)
cv2.destroyAllWindows()
