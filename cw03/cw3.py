import os

import cv2

img1 = cv2.imread(os.path.dirname(os.path.abspath(".")) + "\images" + "\eagle.jpg")
img2 = cv2.imread(os.path.dirname(os.path.abspath(".")) + "\images" + "\image.jpg")

result = cv2.add(img1, img2)

cv2.imshow("img1", img1)
cv2.imshow("img2", img2)
cv2.imshow("cv2.add img1 and img2", result)
cv2.waitKey(0)
cv2.destroyAllWindows()
