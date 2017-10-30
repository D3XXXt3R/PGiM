import os

import cv2

image1 = cv2.imread(os.path.dirname(os.path.abspath(".")) + "\images" + "\kopciuszek.png")
image2 = cv2.imread(os.path.dirname(os.path.abspath(".")) + "\images" + "\kopciuszek2.png")


res = image2 % image1
res = cv2.bitwise_not(res)

cv2.imshow("cv2.add img1 and img2", res)
cv2.waitKey(0)
cv2.destroyAllWindows()