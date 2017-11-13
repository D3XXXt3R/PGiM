import os

import numpy as np
import cv2
import skimage
from skimage.filters.rank import median


def display_image(img):
    cv2.namedWindow('image', cv2.WINDOW_NORMAL)
    cv2.imshow('image', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


img = cv2.imread(os.path.dirname(os.path.abspath(".")) + "\images" + "\lena.jpg", 0)
display_image(img)

imgs = skimage.util.random_noise(img, mode='speckle', seed=None, clip=True)
display_image(imgs)

imgg = skimage.util.random_noise(img, mode='gaussian', seed=None, clip=True)
display_image(imgg)

imgsp = skimage.util.random_noise(img, mode='s&p', seed=None, clip=True)
display_image(imgsp)

imgs_med = median(imgs)
display_image(imgs_med)

imgg_med = median(imgg)
display_image(imgg_med)

imgsp_med = median(imgsp)
display_image(imgsp_med)

print("Speckle")
print(skimage.measure.compare_psnr(img, imgs_med))
print("Gauss")
print(skimage.measure.compare_psnr(img, imgg_med))
print("S&P")
print(skimage.measure.compare_psnr(img, imgsp_med))
print("----------------------------")

img = cv2.imread(os.path.dirname(os.path.abspath(".")) + "\images" + "\lena.jpg", 1)
display_image(img)

imgs = skimage.util.random_noise(img, mode='speckle', seed=None, clip=True)
imgs = np.uint8(imgs * 255)
display_image(imgs)

imgg = skimage.util.random_noise(img, mode='gaussian', seed=None, clip=True)
imgg = np.uint8(imgg * 255)
display_image(imgg)

imgsp = skimage.util.random_noise(img, mode='s&p', seed=None, clip=True)
imgsp = np.uint8(imgsp * 255)
display_image(imgsp)

imgs_b, imgs_g, imgs_r = cv2.split(imgs)
imgs_med_b = median(imgs_b)
imgs_med_g = median(imgs_g)
imgs_med_r = median(imgs_r)
imgs_med = cv2.merge((imgs_med_b, imgs_med_g, imgs_med_r))
display_image(imgs_med)

imgs_ycc = cv2.cvtColor(imgs, cv2.COLOR_BGR2YCR_CB)
imgs_y, imgs_cr, imgs_cb = cv2.split(imgs_ycc)
imgsy_med = cv2.cvtColor(cv2.merge((median(imgs_y), imgs_cr, imgs_cb)), cv2.COLOR_YCR_CB2BGR)
display_image(imgsy_med)

imgg_b, imgg_g, imgg_r = cv2.split(imgg)
imgg_med_b = median(imgs_b)
imgg_med_g = median(imgs_g)
imgg_med_r = median(imgs_r)
imgg_med = cv2.merge((imgg_med_b, imgg_med_g, imgg_med_r))
display_image(imgg_med)

imgg_ycc = cv2.cvtColor(imgg, cv2.COLOR_BGR2YCR_CB)
imgg_y, imgg_cr, imgg_cb = cv2.split(imgg_ycc)
imggy_med = cv2.cvtColor(cv2.merge((median(imgg_y), imgg_cr, imgg_cb)), cv2.COLOR_YCR_CB2BGR)
display_image(imggy_med)

imgsp_b, imgsp_g, imgsp_r = cv2.split(imgsp)
imgsp_med_b = median(imgsp_b)
imgsp_med_g = median(imgsp_g)
imgsp_med_r = median(imgsp_r)
imgsp_med = cv2.merge((imgsp_med_b, imgsp_med_g, imgsp_med_r))
display_image(imgsp_med)

imgsp_ycc = cv2.cvtColor(imgsp, cv2.COLOR_BGR2YCR_CB)
imgsp_y, imgsp_cr, imgsp_cb = cv2.split(imgsp_ycc)
imgspy_med = cv2.cvtColor(cv2.merge((median(imgsp_y), imgsp_cr, imgsp_cb)), cv2.COLOR_YCR_CB2BGR)
display_image(imgspy_med)

print("Speckle")
print(skimage.measure.compare_psnr(img, imgs_med))
print("Gauss")
print(skimage.measure.compare_psnr(img, imgg_med))
print("S&P")
print(skimage.measure.compare_psnr(img, imgsp_med))
print("----------------------------")
print("Speckle")
print(skimage.measure.compare_psnr(img, imgsy_med))
print("Gauss")
print(skimage.measure.compare_psnr(img, imggy_med))
print("S&P")
print(skimage.measure.compare_psnr(img, imgspy_med))
