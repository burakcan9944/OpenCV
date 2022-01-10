import cv2
import numpy as np


img=cv2.imread("contour-2.png")

gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

ret,th1=cv2.threshold(gray,127,255,cv2.THRESH_BINARY)

contours,ret=cv2.findContours(th1,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

print(contours)

cnt=contours[0] 

area= cv2.contourArea(cnt)#alan buluyoruz.bu fonk da bulabiliyoruz moments["m00"]'da aynı alan çıkıyor.

print("alan:",area)

moments=cv2.moments(cnt)

print("alan:",moments["m00"])

perimeter=cv2.arcLength(cnt,True)
#çevreyi buluyoruz.True burda şekilin kapalı yada açık olduğuna bakar ve kapalıysa devam et.

print("cevre:",perimeter)

cv2.imshow("img",img)
cv2.imshow("gray",gray)
cv2.imshow("thres",th1)

cv2.waitKey(0)
cv2.destroyAllWindows()






