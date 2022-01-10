import cv2
import numpy as np

img=cv2.imread("smile.jpg")

face_cascade=cv2.CascadeClassifier("C:\\Users\\Burak\\Desktop\\OpenCv\\Udemy\\Haar_Cascade\\frontalface.xml")
smile_cascade=cv2.CascadeClassifier("C:\\Users\\Burak\\Desktop\\OpenCv\\Udemy\\Haar_Cascade\\smile.xml")

gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

faces=face_cascade.detectMultiScale(gray,1.3,5)

for (x,y,w,h) in faces:

    cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),3)


roi_img=img[y:y+h,x:x+w] #yüzünün old değişken
roi_gray= gray[y:y+h,x:x+w]

smile= smile_cascade.detectMultiScale(roi_gray)

for (sx,sy,sw,sh) in smile:
    cv2.rectangle(roi_img,(sx,sy),(sx+sw,sy+sh),(255,0,0),2)

cv2.imshow("image",img)
cv2.waitKey(0)
cv2.destroyAllWindows()



