import cv2
import numpy as np


img=cv2.imread("contour1.png")

gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY) #siyah-beyaz yaptık

ret,th1=cv2.threshold(gray,127,255,cv2.THRESH_BINARY) #threshold yaptık

counters,ret=cv2.findContours(th1,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE) #CHAIN_APPROX_SIMPLE ve RETR_TREE argümanlar hata almamak için hep yazılır.

draw=cv2.drawContours(img,counters,contourIdx=-1,color=(255,0,0),thickness=3)

cv2.imshow("draw",draw)


cv2.waitKey(0)
cv2.destroyAllWindows()
