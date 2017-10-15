from scipy import ndimage
import cv2
import matplotlib.pyplot as plt


img = cv2.imread('lena.jpg', 0)

rotated = ndimage.rotate(img, 30)
plt.imshow(rotated)
plt.show()

rotated2 = ndimage.rotate(img, 40)
plt.imshow(rotated2)
plt.show()

rotated3 = ndimage.rotate(img, 90)
plt.imshow(rotated3)
plt.show()
