import os

import cv2
import numpy as np

img = cv2.imread(os.path.dirname(os.path.abspath(".")) + "\imgs" + "\lfigury.png", 0)
border = 116
ret, img_bin = cv2.threshold(img, border, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
kernel = np.array([[0, 0, 1, 0, 0],
                   [0, 1, 1, 1, 0],
                   [1, 1, 1, 1, 1],
                   [0, 1, 1, 1, 0],
                   [0, 0, 1, 0, 0]], dtype=np.uint8)
img_dil = cv2.dilate(img_bin, kernel, iterations=1)
img_sub = cv2.subtract(img_dil, img)
cv2.imshow("img", img)
cv2.imshow("Binary", img_bin)
cv2.imshow("Dilate", img_dil)
cv2.imshow("Substract", img_sub)
cv2.waitKey(0)
cv2.destroyAllWindows()
