import cv2
import numpy as np

font=cv2.FONT_HERSHEY_SIMPLEX
font1=cv2.FONT_HERSHEY_COMPLEX#OPENCV FONTS

img=cv2.imread("polygons.png")

gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

ret,thres=cv2.threshold(gray,240,255,cv2.THRESH_BINARY)

contours,_=cv2.findContours(thres,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

for cnt in contours:

    epsilon=0.01 *cv2.arcLength(cnt,True) #şeklin kapalı olup olmadığına bakılır.
    approx=cv2.approxPolyDP(cnt,epsilon,True) #YAKLAŞMA DEMEK.contourlara daha yaklaşmak için.


    cv2.drawContours(img,[approx],0,(0),5)

    x=approx.ravel()[0]#bu fonk sutunkarı yani dik sıraları satıra döker ve bunu aprroxa uygulayacağız.
    y=approx.ravel()[1]#Sıraladıktan sonra 0 indis x,1 indis y yi temsil edecek.Çünkü şekillerin üst koordinatların
    #adlarını yazacağız.konturların başladığı noktalardın buralar.

    #print(approx)
    #print(len(approx))

    if len(approx) ==3: #approxun uzunluğu 3 tür
        cv2.putText(img,"Triangle",(x,y),font1,1,(0))

    elif len(approx) ==4: #approxun uzunluğu 3 tür
        cv2.putText(img,"Rectangle",(x,y),font1,1,(0))

    elif len(approx) ==5: #approxun uzunluğu 3 tür
        cv2.putText(img,"Pentagon",(x,y),font1,1,(0))

    elif len(approx) ==6: #approxun uzunluğu 3 tür
        cv2.putText(img,"Hexagon",(x,y),font1,1,(0))

    else:
        cv2.putText(img,"Ellipse",(x,y),font1,1,(0))


cv2.imshow("IMG",img)
cv2.waitKey(0)
cv2.destroyAllWindows()