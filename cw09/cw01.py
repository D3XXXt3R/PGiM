import os

import cv2
import numpy as np

img = cv2.imread(os.path.dirname(os.path.abspath(".")) + "\images" + "\lena.jpg", 0)
border = 116
ret, img_bin = cv2.threshold(img, border, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
kernel_hit = np.array([[1, 1, 1],
                       [1, 0, 1],
                       [1, 1, 1]], dtype=np.uint8)
kernel_miss = np.array([[0, 0, 0],
                        [0, 0, 0],
                        [0, 0, 0]], dtype=np.uint8)
img_hit = cv2.erode(img_bin, kernel_hit, iterations=1)
img_miss = cv2.erode(cv2.bitwise_not(img_bin), kernel_miss, iterations=1)
img_hit_or_miss = cv2.bitwise_or(img_hit, img_miss)

cv2.imshow("Image", img)
cv2.imshow("Binary", img_bin)
cv2.imshow("Hit-or-Miss", img_hit_or_miss)
cv2.waitKey(0)
cv2.destroyAllWindows()
