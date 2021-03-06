import os

import cv2

img1 = cv2.imread(os.path.dirname(os.path.abspath(".")) + "\images" + "\eagle.jpg")
img2 = cv2.imread(os.path.dirname(os.path.abspath(".")) + "\images" + "\image.jpg")
result = cv2.addWeighted(img1, 0.5, img2, 0.5, 0)
cv2.imshow('dst', result)
cv2.waitKey(0)
cv2.destroyAllWindows()
