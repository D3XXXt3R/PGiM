import os

import cv2
import numpy as np

img = cv2.imread(os.path.dirname(os.path.abspath(".")) + "\imgs" + "\lena.jpg")
kernel = np.array([[0, 1, 0],
                   [1, 1, 1],
                   [0, 1, 0]], dtype = np.uint8)
img_er = cv2.erode(img, kernel, iterations = 1)
img_dil = cv2.dilate(img, kernel, iterations = 1)
cv2.imshow("Img", img)
cv2.imshow("Erode", img_er)
cv2.imshow("Dilate", img_dil)
cv2.waitKey(0)
cv2.destroyAllWindows()
