import cv2
import numpy as np



video=cv2.VideoCapture("body.mp4")

body_cascade=cv2.CascadeClassifier("C:\\Users\\Burak\\Desktop\\OpenCv\\Udemy\\Haar_Cascade\\fullbody.xml")


while True:
    ret,frame=video.read()

    frame=cv2.resize(frame, (640,580))

    gray=cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    body=body_cascade.detectMultiScale(gray,1.1,4)

    for (x,y,w,h) in body:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,0,255),2)

    cv2.imshow("frame",frame)

    if cv2.waitKey(5) & 0xFF==ord("q"):
        break

video.release()
cv2.destroyAllWindows()