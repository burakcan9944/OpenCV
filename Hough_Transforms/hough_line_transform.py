import cv2
import numpy as np


img=cv2.imread("h_line.png")

gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

edges=cv2.Canny(gray,75,150) #köşeler içindir.


#cv2.HoughLines() #çok fazla CPU kullnıyor
lines=cv2.HoughLinesP(edges,rho=1,theta=np.pi/180,threshold=50,maxLineGap=500) #daha çok bunu kullanıcağız.
for line in lines:

    x1,y1,x2,y2=line[0]

    cv2.line(img,(x1,y1),(x2,y2),(0,255,0),2) #tek tek bukduğumuz koordinatla yaptığımız çizimi buluyoruz.

cv2.imshow("img",img)
cv2.imshow("orj",gray)
cv2.imshow("edges",edges)

cv2.waitKey(0)
cv2.destroyAllWindows()