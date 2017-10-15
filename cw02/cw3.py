import numpy as np
from matplotlib import pyplot as plt
from scipy import misc

image = misc.imread('lena.jpg')
grey = np.zeros((image.shape[0], image.shape[1]))  # init 2D numpy array

for rownum in range(len(image)):
    for colnum in range(len(image[rownum])):
        grey[rownum][colnum] = np.average(image[rownum][colnum])

plt.imshow(grey, cmap='gray')
plt.show()
