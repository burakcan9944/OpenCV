import cv2
import numpy as np

video=cv2.VideoCapture("car.mp4")

face_cascade=cv2.CascadeClassifier("C:\\Users\\Burak\\Desktop\\OpenCv\\Udemy\\car_cascade\\carr_cascade.xml")

while True:
    ret,frame=video.read()

    frame=cv2.resize(frame,(640,480))

    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(gray,1.4,2)

    for (x,y,w,h) in faces:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)

    cv2.imshow("frame",frame)

    if cv2.waitKey(5) & 0xFF ==ord("q"):
        break

video.release()
cv2.destroyAllWindows()



