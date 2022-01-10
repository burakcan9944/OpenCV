import cv2
import numpy as np


img=cv2.imread("Strange Horizon.png")

img_RGB=cv2.cvtColor(img,cv2.COLOR_BGR2RGB) #BGR 'DEN RGB'YE dönüştü.

img_HSV=cv2.cvtColor(img,cv2.COLOR_BGR2HSV) #BGR 'DEN HSV'YE dönüştü.

img_gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY) #BGR 'DEN renksize dönüştü.

cv2.imshow("img_ORJ",img)
cv2.imshow("img_RGB",img_RGB)
cv2.imshow("img_HSV",img_HSV)
cv2.imshow("img_gray",img_gray)

cv2.waitKey(0)
cv2.destroyAllWindows()