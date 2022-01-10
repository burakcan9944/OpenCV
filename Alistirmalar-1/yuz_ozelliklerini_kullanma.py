import cv2
import numpy as np
import math


def findMaxContour(contours): #max contours bulmak

    max_i=0
    max_area=0

    for i in range(len(contours)): #alanları tek tek birbirleriyle karşılaştırarak max olana ulaşmak

        area_face=cv2.contourArea(contours[i])

        if max_area<area_face: #burda max alanı bulana kadar döndürür.
            max_area=area_face
            max_i=i

            try:
                c=contours[max_i]
            except: #eger max alan bulamazsa bunun değeri sıfır olsun ki herhangi bir hata alamayalım
                contours=[0]
                c=contours[0]

            return c

camera=cv2.VideoCapture(0)


while True:
    ret,frame=camera.read()

    frame=cv2.flip(frame,1)

    roi=frame[100:300,200:350] #frame[y1:y2,x1:x2]

    cv2.rectangle(frame,(200,100),(350,300),(0,0,255),0) #(x1,y1),(x2,y2).kalınlık sıfır olsun ki o d amask işlemine dahil olmasın

    hsv=cv2.cvtColor(roi,cv2.COLOR_BGR2HSV)

    lower_color=np.array([0,45,79],dtype=np.uint8)
    upper_color=np.array([17,255,255],dtype=np.uint8)

    mask=cv2.inRange(hsv,lower_color,upper_color)

    kernel=np.ones((3,3),np.uint8)

    mask=cv2.dilate(mask,kernel,iterations=1)#temiz görüntü için
    mask=cv2.medianBlur(mask,15)

    contours,_=cv2.findContours(mask,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

    if len(contours) > 0: #contours dan herhangibir değer gelmediyse

        try: #arka plandaki beyaz karıncalanmalaı ilgilnemke istemiyorum sadece yüzümle ilgilenmek istiyorum
            c=findMaxContour(contours)

            extLeft= tuple(c[c[:,:,0].argmin()][0]) #uç sol nokta.Tüm konturler arasında en küçük x leri bulacak.
            extrRight = tuple(c[c[:, :, 0].argmax()][0])
            extrTop = tuple(c[c[:, :, 1].argmin()][0])# 1 diyoruz çünkü yukarı aşağı yöden bir hareket olduğu için ben y'leri aracağım
            extrBot = tuple(c[c[:, :, 1].argmax()][0])

            cv2.circle(roi,extLeft,5,(0,255,0),2)
            cv2.circle(roi, extrRight, 5, (0, 255, 0), 2)
            cv2.circle(roi, extrTop, 5, (0, 255, 0), 2)
            cv2.circle(roi, extrBot, 5, (0, 255, 0), 2)

            cv2.line(roi, extLeft, extrTop, (255, 0, 0), 2)
            cv2.line(roi, extrTop, extrRight, (255, 0, 0), 2)
            cv2.line(roi, extrRight, extrBot, (255, 0, 0), 2)
            cv2.line(roi, extrBot, extLeft, (255, 0, 0), 2)

            a=math.sqrt((extrRight[0]-extrTop[0])**2+(extrRight[1]-extrTop[1])**2) #kenarının uzunluğu
            b = math.sqrt((extrBot[0] - extrRight[0]) ** 2 + (extrBot[1] - extrRight[1]) ** 2)#buralarda iki nokta rasındaki uzaklık formülünü uyguluyoruz.
            c = math.sqrt((extrTop[0] - extrBot[0]) ** 2 + (extrTop[1] - extrBot[1]) ** 2)

            try:
                angle_ab= int(math.acos((a**2+b**2-c**2)/(2*b*c))*57)#açıları buluyoruz.sıfıra bölünme hatası yaşanılabilir.
                cv2.putText(roi,str(angle_ab),(extrRight[0]-50,extrRight[1]),cv2.FONT_HERSHEY_SIMPLEX,1
                            ,(0,0,255),2,cv2.LINE_AA)
            except:
                cv2.putText(roi,
                "?", (extrRight[0] - 50, extrRight[1]), cv2.FONT_HERSHEY_SIMPLEX, 1,
                            (0, 0, 255), 2, cv2.LINE_AA)

        except:
            pass

    else:
        pass

    cv2.imshow("frame",frame)
    cv2.imshow("roi", roi)
    cv2.imshow("mask", mask)

    if cv2.waitKey(20) & 0xFF==ord("q"):
        break


camera.release()
cv2.destroyAllWindows()