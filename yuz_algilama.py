import cv2
import numpy as np

img=cv2.imread("face-1.png")

face_cascade=cv2.CascadeClassifier("C:\\Users\\Burak\\Desktop\\OpenCv\\Udemy\\Haar_Cascade\\frontalface.xml")

gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

faces=face_cascade.detectMultiScale(gray,1.3,7) #1.3 degerinde resmimizi küçültücez.Belli bir bölgede en az 4 pencerede yüz bulsun ki
#yüzün orada olduğundan emin olalım.


for (x,y,w,h) in faces:   #Dikdörtgenin sol üst kordinatları için x ve y ,yükseklik ve genişlik için de w ve h.

    cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),2)

cv2.imshow("image",img)

cv2.waitKey(0)
cv2.destroyAllWindows()



