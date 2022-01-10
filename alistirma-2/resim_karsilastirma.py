import cv2
import numpy as np


img1=cv2.imread("aircraft.jpg")
img1=cv2.resize(img1,(640,550))

img2=cv2.imread("aircraft1.jpg")
img2=cv2.resize(img2,(640,550))

img3_blur=cv2.medianBlur(img1,7)

if img1.shape==img2.shape:
    print("same size")
else:
    print("not same")

diff= cv2.subtract(img1,img3_blur) #difference

b,g,r=cv2.split(diff)

if cv2.countNonZero(b) ==0 and cv2.countNonZero(g)==0 and cv2.countNonZero(r)==0:#diff'in içinde sıfır olmayan bir değer varsa ben bunu bulucam.

    print("completely equal")
else:
    print("NOT completely equal")

cv2.imshow("img1",img1)
#cv2.imshow("img2",img2)
cv2.imshow("img3_blur",img3_blur)
cv2.imshow("diff",diff)

cv2.waitKey(0)
cv2.destroyAllWindows()
