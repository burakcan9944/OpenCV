import cv2
import numpy as np

img=cv2.imread("contour-2.png")

gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

ret,th1=cv2.threshold(gray,127,255,cv2.THRESH_BINARY)

moments=cv2.moments(th1) #thresholdu momenta attık ki bizim için değerleri çeksin.
                         #o degerle için de print(moments) yaparak bakabilirsin.

x=int(moments["m10"]/moments["m00"]) #geometri merkezlerini bulmak içindir.Bu hep böyledir.

y=int(moments["m01"]/moments["m00"])

cv2.circle(img,center=(x,y),radius=5,color=(0,255,0),thickness=-1)

cv2.imshow("img",img)

cv2.waitKey(0)
cv2.destroyAllWindows()