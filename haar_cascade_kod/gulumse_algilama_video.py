import cv2
import numpy as np

video=cv2.VideoCapture(0)

face_cascade=cv2.CascadeClassifier("C:\\Users\\Burak\\Desktop\\OpenCv\\Udemy\\Haar_Cascade\\frontalface.xml")
smile_cascade=cv2.CascadeClassifier("C:\\Users\\Burak\\Desktop\\OpenCv\\Udemy\\Haar_Cascade\\smile.xml")


while True:
    ret,frame=video.read()

    if ret==False:
        break

    frame=cv2.resize(frame,(480,360))

    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(gray,1.2,3)

    for (x,y,w,h) in faces:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)

        roi_gray = gray[y:y + h, x:x + w]
        roi_frame = frame[y:y + h, x:x + w]

        smile = smile_cascade.detectMultiScale(roi_gray)

        for (sx, sy, sw, sh) in smile:
            cv2.rectangle(roi_frame, (sx, sy), (sx + sw, sy + sh), (0, 0, 255), 2)

    cv2.imshow("frame",frame)

    if cv2.waitKey(5) & 0xFF ==ord("q"):
        break

video.release()
cv2.destroyAllWindows()



