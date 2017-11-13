import os

import cv2
import skimage

img = cv2.imread(os.path.dirname(os.path.abspath(".")) + "\images" + "\lena.jpg", 0)
img = skimage.util.random_noise(img, mode='speckle', seed=None, clip=True)
cv2.namedWindow('image', cv2.WINDOW_NORMAL)
cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()