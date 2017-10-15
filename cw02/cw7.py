import cv2
import numpy as np

img = cv2.imread('lena.jpg', 1)
img2 = img[0:512, 0:300]
img3 = img[0:512, 301:512]
cv2.namedWindow('image', cv2.WINDOW_NORMAL)
vis = np.concatenate((img3, img2), axis=1)
cv2.imshow('image', vis)

cv2.waitKey(0)
cv2.destroyAllWindows()