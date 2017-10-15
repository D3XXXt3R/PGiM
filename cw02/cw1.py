import cv2

img3 = cv2.imread('lena.jpg',1)
counter = 0
for i in img3:
    for j in i:
        j += 100
        counter += 1
        if counter == 100:
            break

cv2.namedWindow('image2', cv2.WINDOW_NORMAL)
cv2.imshow('image2', img3)
cv2.waitKey(0)
cv2.destroyAllWindows()
