import os

import cv2
import numpy as np

image1 = cv2.imread(os.path.dirname(os.path.abspath(".")) + "\images" + "\kopciuszek.png")
image2 = cv2.imread(os.path.dirname(os.path.abspath(".")) + "\images" + "\kopciuszek2.png")

difference = cv2.subtract(image1, image2)

result = not np.any(difference)
# lack of difference return False

if result is True:
    print("The same images")
else:
    cv2.imshow("cv2.add img1 and img2", difference)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
