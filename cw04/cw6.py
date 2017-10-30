import os

import cv2

img = cv2.imread(os.path.dirname(os.path.abspath(".")) + "\images" + "\redeyes.jpg", 1)
img_hls = cv2.cvtColor(img, cv2.COLOR_BGR2HLS)

for index_i, i in enumerate(img):
    for index_j, j in enumerate(i):
        H = img_hls[index_i][index_j][0]
        L = img_hls[index_i][index_j][1]
        S = img_hls[index_i][index_j][2]
        if float(S) != 0 and float(L) != 0:
            LS_ratio = float(L) / float(S)
        else:
            LS_ratio = 0
        red_eye_pixel = (L >= 64) and (S >= 100) and (LS_ratio > 0.5) and (LS_ratio < 1.5) and ((H <= 7) or (H >= 162))
        if not red_eye_pixel:
            j[0] = 0.299 * j[0] + 0.587 * j[1] + 0.114 * j[2]
            j[1] = 0.299 * j[0] + 0.587 * j[1] + 0.114 * j[2]
            j[2] = 0.299 * j[0] + 0.587 * j[1] + 0.114 * j[2]

cv2.imshow("redeyes", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
