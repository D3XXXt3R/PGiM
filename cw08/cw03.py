import os

import cv2

img = cv2.imread(os.path.dirname(os.path.abspath(".")) + "\imgs" + "\lfigury.png", 0)
border = 116
ret, img_bin = cv2.threshold(img, border, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
cv2.imshow("Img", img)
cv2.imshow("Binary", img_bin)
for i in range(2, 8):
    kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (2 * i + 1, 2 * i + 1))
    img_erode = cv2.erode(img_bin, kernel, iterations=1)
    cv2.imshow("img Erode r = " + str(i), img_erode)
cv2.waitKey(0)
cv2.destroyAllWindows()
