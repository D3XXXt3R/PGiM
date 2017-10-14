import cv2

img = cv2.imread('lena.jpg', cv2.IMREAD_UNCHANGED)
cv2.namedWindow('image', cv2.WINDOW_NORMAL)
cv2.imshow('image', img)

img2 = cv2.imread('statek.jpg', cv2.IMREAD_UNCHANGED)
cv2.namedWindow('image2', cv2.WINDOW_NORMAL)
cv2.imshow('image2', img2)

cv2.waitKey(0)
cv2.destroyAllWindows()
