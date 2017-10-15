import cv2

img = cv2.imread('lena.jpg')
img = cv2.bitwise_not(img)
cv2.namedWindow('image', cv2.WINDOW_NORMAL)
cv2.imshow('image', img)


img2 = cv2.imread('statek.jpg')
img2 = cv2.bitwise_not(img2)
cv2.namedWindow('image2', cv2.WINDOW_NORMAL)
cv2.imshow('image2', img2)

cv2.waitKey(0)
cv2.destroyAllWindows()
