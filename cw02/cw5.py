import os

import cv2
import numpy as np
import matplotlib.pyplot as plt

def sepia(pixel):
    R = pixel[2] * 0.393 + pixel[1] * 0.769 + pixel[0] * 0.189
    G = pixel[2] * 0.349 + pixel[1] * 0.686 + pixel[0] * 0.168
    B = pixel[2] * 0.272 + pixel[1] * 0.534 + pixel[0] * 0.131
    R = R if R < 256 else 255
    G = G if G < 256 else 255
    B = B if B < 256 else 255
    result = np.array([R,G,B], dtype='uint8')
    return result


image = cv2.imread(os.path.dirname(os.path.abspath(".")) + "\images" + "\lena.jpg")
image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
sepiaImage = np.zeros((image.shape[0], image.shape[1], image.shape[2]), dtype=np.uint8)

for row in range(len(image)):
    for col in range(len(image[row])):
        sepiaImage[row][col] = np.apply_along_axis(sepia, 0, image[row][col])

plt.imshow(sepiaImage)
plt.show()

