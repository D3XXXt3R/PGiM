import os

import cv2
import numpy as np

p = cv2.imread(os.path.dirname(os.path.abspath(".")) + "\images" + "\peppers.png", cv2.IMREAD_COLOR)

h, w, bpp = np.shape(p)

for py in range(0, h):
    for px in range(0, w):
        green = max(p[px][py][0], p[px][py][1])
        green = max(green, p[px][py][2])
        if p[px][py][1] != green:
            p[px][py][0] = 0
            p[px][py][1] = 0
            p[px][py][2] = 0

cv2.imshow('matrix', p)
cv2.waitKey(0)
