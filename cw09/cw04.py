import os

import cv2
import numpy as np

img = cv2.imread(os.path.dirname(os.path.abspath(".")) + "\images" + "\siatka2.png", 0)
border = 116
ret, img_bin = cv2.threshold(img, border, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
kernel_hit_1_1 = np.array([[0, 0, 0],
                           [0, 1, 0],
                           [0, 0, 0]], dtype=np.uint8)
kernel_miss_1_1 = np.array([[1, 0, 0],
                            [1, 0, 1],
                            [1, 1, 1]], dtype=np.uint8)
kernel_hit_1_2 = np.array([[0, 0, 0],
                           [0, 1, 0],
                           [0, 0, 0]], dtype=np.uint8)
kernel_miss_1_2 = np.array([[1, 1, 1],
                            [1, 0, 0],
                            [1, 1, 0]], dtype=np.uint8)
kernel_hit_1_3 = np.array([[0, 0, 0],
                           [0, 1, 0],
                           [0, 0, 0]], dtype=np.uint8)
kernel_miss_1_3 = np.array([[1, 1, 1],
                            [1, 0, 1],
                            [0, 0, 1]], dtype=np.uint8)
kernel_hit_1_4 = np.array([[0, 0, 0],
                           [0, 1, 0],
                           [0, 0, 0]], dtype=np.uint8)
kernel_miss_1_4 = np.array([[0, 1, 1],
                            [0, 0, 1],
                            [1, 1, 1]], dtype=np.uint8)
kernel_hit_2_1 = np.array([[0, 0, 0],
                           [0, 1, 0],
                           [0, 0, 0]], dtype=np.uint8)
kernel_miss_2_1 = np.array([[0, 0, 1],
                            [1, 0, 1],
                            [1, 1, 1]], dtype=np.uint8)
kernel_hit_2_2 = np.array([[0, 0, 0],
                           [0, 1, 0],
                           [0, 0, 0]], dtype=np.uint8)
kernel_miss_2_2 = np.array([[1, 1, 0],
                            [1, 0, 0],
                            [1, 1, 1]], dtype=np.uint8)
kernel_hit_2_3 = np.array([[0, 0, 0],
                           [0, 1, 0],
                           [0, 0, 0]], dtype=np.uint8)
kernel_miss_2_3 = np.array([[1, 1, 1],
                            [1, 0, 1],
                            [1, 0, 0]], dtype=np.uint8)
kernel_hit_2_4 = np.array([[0, 0, 0],
                           [0, 1, 0],
                           [0, 0, 0]], dtype=np.uint8)
kernel_miss_2_4 = np.array([[1, 1, 1],
                            [0, 0, 1],
                            [0, 1, 1]], dtype=np.uint8)
for i in range(10):
    img_hit = cv2.erode(img_bin, kernel_hit_1_1, iterations=1)
    img_miss = cv2.erode(cv2.bitwise_not(img_bin), kernel_miss_1_1, iterations=1)
    img_tmp = cv2.bitwise_and(img_hit, img_miss)
    img_bin = cv2.absdiff(img_bin, img_tmp)
    img_hit = cv2.erode(img_bin, kernel_hit_2_1, iterations=1)
    img_miss = cv2.erode(cv2.bitwise_not(img_bin), kernel_miss_2_1, iterations=1)
    img_tmp = cv2.bitwise_and(img_hit, img_miss)
    img_bin = cv2.absdiff(img_bin, img_tmp)
    img_hit = cv2.erode(img_bin, kernel_hit_1_2, iterations=1)
    img_miss = cv2.erode(cv2.bitwise_not(img_bin), kernel_miss_1_2, iterations=1)
    img_tmp = cv2.bitwise_and(img_hit, img_miss)
    img_bin = cv2.absdiff(img_bin, img_tmp)
    img_hit = cv2.erode(img_bin, kernel_hit_2_2, iterations=1)
    img_miss = cv2.erode(cv2.bitwise_not(img_bin), kernel_miss_2_2, iterations=1)
    img_tmp = cv2.bitwise_and(img_hit, img_miss)
    img_bin = cv2.absdiff(img_bin, img_tmp)
    img_hit = cv2.erode(img_bin, kernel_hit_1_3, iterations=1)
    img_miss = cv2.erode(cv2.bitwise_not(img_bin), kernel_miss_1_3, iterations=1)
    img_tmp = cv2.bitwise_and(img_hit, img_miss)
    img_bin = cv2.absdiff(img_bin, img_tmp)
    img_hit = cv2.erode(img_bin, kernel_hit_2_3, iterations=1)
    img_miss = cv2.erode(cv2.bitwise_not(img_bin), kernel_miss_2_3, iterations=1)
    img_tmp = cv2.bitwise_and(img_hit, img_miss)
    img_bin = cv2.absdiff(img_bin, img_tmp)
    img_hit = cv2.erode(img_bin, kernel_hit_1_4, iterations=1)
    img_miss = cv2.erode(cv2.bitwise_not(img_bin), kernel_miss_1_4, iterations=1)
    img_tmp = cv2.bitwise_and(img_hit, img_miss)
    img_bin = cv2.absdiff(img_bin, img_tmp)
    img_hit = cv2.erode(img_bin, kernel_hit_2_4, iterations=1)
    img_miss = cv2.erode(cv2.bitwise_not(img_bin), kernel_miss_2_4, iterations=1)
    img_tmp = cv2.bitwise_and(img_hit, img_miss)
    img_bin = cv2.absdiff(img_bin, img_tmp)
    cv2.imshow("Hit-or-Miss " + str(i), img_bin)

cv2.imshow("Img", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
