import os

import cv2
import numpy as np

img = cv2.imread(os.path.dirname(os.path.abspath(".")) + "\images" + "\siatka1.png", 0)
border = 116
ret, img_bin = cv2.threshold(img, border, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
kernel_1_1 = np.array([[1, 1, 0],
                       [1, -1, 0],
                       [1, 0, -1]], dtype=np.uint8)
kernel_1_2 = np.array([[1, 1, 1],
                       [0, -1, 1],
                       [-1, 0, 0]], dtype=np.uint8)
kernel_1_3 = np.array([[-1, 0, 1],
                       [0, -1, 1],
                       [0, 1, 1]], dtype=np.uint8)
kernel_1_4 = np.array([[0, 0, -1],
                       [1, -1, 0],
                       [1, 1, 1]], dtype=np.uint8)
kernel_2_1 = np.array([[0, 1, 1],
                       [0, -1, 1],
                       [-1, 0, 1]], dtype=np.uint8)
kernel_2_2 = np.array([[-1, 0, 0],
                       [0, -1, 1],
                       [1, 1, 1]], dtype=np.uint8)
kernel_2_3 = np.array([[1, 0, -1],
                       [1, -1, 0],
                       [1, 1, 0]], dtype=np.uint8)
kernel_2_4 = np.array([[1, 1, 1],
                       [1, -1, 0],
                       [0, 0, -1]], dtype=np.uint8)
for i in range(30):
    img_tmp = cv2.morphologyEx(img_bin, cv2.MORPH_HITMISS, kernel_1_1)
    img_bin = cv2.add(img_bin, img_tmp)
    img_tmp = cv2.morphologyEx(img_bin, cv2.MORPH_HITMISS, kernel_2_1)
    img_bin = cv2.add(img_bin, img_tmp)
    img_tmp = cv2.morphologyEx(img_bin, cv2.MORPH_HITMISS, kernel_1_2)
    img_bin = cv2.add(img_bin, img_tmp)
    img_tmp = cv2.morphologyEx(img_bin, cv2.MORPH_HITMISS, kernel_2_2)
    img_bin = cv2.add(img_bin, img_tmp)
    img_tmp = cv2.morphologyEx(img_bin, cv2.MORPH_HITMISS, kernel_1_3)
    img_bin = cv2.add(img_bin, img_tmp)
    img_tmp = cv2.morphologyEx(img_bin, cv2.MORPH_HITMISS, kernel_2_3)
    img_bin = cv2.add(img_bin, img_tmp)
    img_tmp = cv2.morphologyEx(img_bin, cv2.MORPH_HITMISS, kernel_1_4)
    img_bin = cv2.add(img_bin, img_tmp)
    img_tmp = cv2.morphologyEx(img_bin, cv2.MORPH_HITMISS, kernel_2_4)
    img_bin = cv2.add(img_bin, img_tmp)
    img_bin[0][0] = 0
    img_bin[0][1] = 0
    img_bin[0][254] = 0
    img_bin[0][255] = 0
    img_bin[255][0] = 0
    img_bin[255][1] = 0
    img_bin[254][255] = 0
    img_bin[255][255] = 0
for i in range(30, 40):
    img_tmp = cv2.morphologyEx(img_bin, cv2.MORPH_HITMISS, kernel_1_1)
    img_bin = cv2.add(img_bin, img_tmp)
    img_tmp = cv2.morphologyEx(img_bin, cv2.MORPH_HITMISS, kernel_2_1)
    img_bin = cv2.add(img_bin, img_tmp)
    img_tmp = cv2.morphologyEx(img_bin, cv2.MORPH_HITMISS, kernel_1_2)
    img_bin = cv2.add(img_bin, img_tmp)
    img_tmp = cv2.morphologyEx(img_bin, cv2.MORPH_HITMISS, kernel_2_2)
    img_bin = cv2.add(img_bin, img_tmp)
    img_tmp = cv2.morphologyEx(img_bin, cv2.MORPH_HITMISS, kernel_1_3)
    img_bin = cv2.add(img_bin, img_tmp)
    img_tmp = cv2.morphologyEx(img_bin, cv2.MORPH_HITMISS, kernel_2_3)
    img_bin = cv2.add(img_bin, img_tmp)
    img_tmp = cv2.morphologyEx(img_bin, cv2.MORPH_HITMISS, kernel_1_4)
    img_bin = cv2.add(img_bin, img_tmp)
    img_tmp = cv2.morphologyEx(img_bin, cv2.MORPH_HITMISS, kernel_2_4)
    img_bin = cv2.add(img_bin, img_tmp)
    img_bin[0][0] = 0
    img_bin[0][1] = 0
    img_bin[0][254] = 0
    img_bin[0][255] = 0
    img_bin[255][0] = 0
    img_bin[255][1] = 0
    img_bin[254][255] = 0
    img_bin[255][255] = 0
    cv2.imshow("Hit-or-Miss " + str(i), img_bin)
cv2.imshow("Img", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
