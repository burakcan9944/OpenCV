import cv2

cv2.namedWindow("image",cv2.WINDOW_NORMAL)
img=cv2.imread("kabus_orman.png")
image=cv2.resize(img,(640,480))


cv2.imshow("image",image)

cv2.waitKey(0)
cv2.destroyAllWindows()

