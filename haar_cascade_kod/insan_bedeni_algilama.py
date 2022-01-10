import cv2
import numpy as np



img=cv2.imread("body.jpg")

body_cascade=cv2.CascadeClassifier("C:\\Users\\Burak\\Desktop\\OpenCv\\Udemy\\Haar_Cascade\\fullbody.xml")

gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

body=body_cascade.detectMultiScale(gray,1.2,1)

for (x,y,w,h) in body:
    cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),2)

cv2.imshow("image",img)

cv2.waitKey(0)
cv2.destroyAllWindows()





