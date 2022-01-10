import cv2
import numpy as np

video=cv2.VideoCapture("traffic.avi")

backsub=cv2.createBackgroundSubtractorMOG2()
c=0 #her araç saydığımzda bir bri arttıracağız.

while True:
    ret,frame=video.read()

    if ret:
        fgmask = backsub.apply(frame)

        cv2.line(frame,(50,0),(50,300),(0,255,0),2) #videonun boyutuna bakarak o çizgileri çekiniz.
        cv2.line(frame, (70, 0), (70, 300), (0, 255, 0), 2)

        contours,hierarch=cv2.findContours(fgmask,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

        try: hierarch=hierarch[0]
        except:hierarch=[]

        for contour,hier in zip(contours,hierarch): #zip,tekrar tekrar buradan değeri çekeceğiz.
            (x,y,w,h)=cv2.boundingRect(contour)
            if w>40 and h>40: #bu değerlerden büyük ise dikdörtgen çizilecek.çünkü bu değerlerden büyük old orada araba olur.
                cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),3)
                if x>50 and x<70:#o kordinatlar benim çizgimin arasından geçiyor ise ben sayacı bir arttıracağım.

                    c +=1

        cv2.putText(frame,"car: " +str(c),(90,100),cv2.FONT_HERSHEY_SIMPLEX,2,(0,0,255),2,cv2.LINE_AA)

        cv2.imshow("video",frame)
        cv2.imshow("mask", fgmask)

        if cv2.waitKey(20) & 0xFF==ord("q"):
            break

video.release()
cv2.destroyAllWindows()