import os

import cv2
import skimage


# def salt_pepper(im, ps=.1, pp=.1):
#     """ps probality white pixel, pp probability black pixel"""
#
#     im1 = im[:, :, 0].copy()
#     n, m = im1.shape
#     for i in range(n):
#         for j in range(m):
#             noise = np.random.uniform()  # uniform noise
#             if noise < ps:
#                 im1[i, j] = 0
#             elif noise > 1 - pp:
#                 im1[i, j] = 1
#     noisy_im = [[[im1[i, j]] * 3 for j in range(m)] for i in range(n)]
#     return noisy_im


img = cv2.imread(os.path.dirname(os.path.abspath(".")) + "\images" + "\lena.jpg", 0)
#pts = np.array(salt_pepper(img))
img = skimage.util.random_noise(img, mode='s&p', seed=None, clip=True)
cv2.namedWindow('image', cv2.WINDOW_NORMAL)
cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
