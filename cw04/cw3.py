import os

import cv2

img = cv2.imread(os.path.dirname(os.path.abspath(".")) + "\images" + "\lena.jpg", 1)
img = cv2.cvtColor(img, cv2.COLOR_RGB2HLS)
cv2.imshow("ycbr", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
