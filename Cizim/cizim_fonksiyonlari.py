import cv2
import numpy as np

canvas=np.zeros((512,512,3),np.uint8) + 255

cv2.line(canvas,(50,50),(150,150),color=(255,255,0),thickness=3 )#pt1:başlangıc yeri line nin,pt2:line'in sonu,
cv2.line(canvas,(100,50),(200,250),color=(0,0,255),thickness=3 )

cv2.rectangle(canvas,(100,100),(300,300),(0,255,0),3)

cv2.circle(canvas,(400,400),100,(255,0,0),3)

p1=(100,200)
p2=(50,50)
p3=(300,300)

cv2.line(canvas,p1,p2,(0,0,0),4)#üçgen yapıyoruz
cv2.line(canvas,p2,p3,(0,0,0),4)
cv2.line(canvas,p1,p3,(0,0,0),4)

points=np.array([[[110,200],[330,200],[290,220],[100,100]]],np.int32)

cv2.ellipse(canvas,(100,400), (80,20),10,90,360,(0,0,0),-1)   #elips çizimi

cv2.polylines(canvas, [points],True, (255,0,0),3)   #yamuk oluşturmak,kapalı olması için "True" yazın.




cv2.putText(canvas,"Python",(350,100),fontFace=cv2.FONT_HERSHEY_COMPLEX,fontScale=1,color=(0,0,0),thickness=3)

cv2.imshow("canvas",canvas)
cv2.waitKey(0)
cv2.destroyAllWindows()