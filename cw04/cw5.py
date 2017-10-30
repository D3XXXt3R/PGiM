import os

import cv2
import sys

# Solution from:
# https://realpython.com/blog/python/face-recognition-with-python/

# # Create the haar cascade
# faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

# Read the image
# image = cv2.imread("skin.jpg")
# gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
#
# # Detect faces in the image
# faces = faceCascade.detectMultiScale(
#     gray,
#     scaleFactor=1.1,
#     minNeighbors=5,
#     minSize=(30, 30),
#     flags = cv2.CASCADE_SCALE_IMAGE
# )
#
# print("Found {0} faces!".format(len(faces)))
#
# # Draw a rectangle around the faces
# for (x, y, w, h) in faces:
#     cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 2)
#
# cv2.imshow("Faces found", image)
# cv2.waitKey(0)

image = cv2.imread(os.path.dirname(os.path.abspath(".")) + "\images" + "\skin.jpg")
hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HLS)
h, l, s = cv2.split(hsv)
for i in range(image.shape[0]):
    for j in range(image.shape[1]):
        ratio = l[i][j] / s[i][j]
        if not (s[i][j] >= 50 and ratio > 0.5 and ratio < 3.0 and (h[i][j] <= 14 or h[i][j] >= 165)):
            image[i][j] = 0

cv2.imshow("Water", image)
cv2.waitKey(0)
cv2.destroyAllWindows()