import cv2
import numpy as np


camera=cv2.VideoCapture("car.mp4")

_,first_frame=camera.read()

first_frame=cv2.resize(first_frame,(640,480))

first_gray=cv2.cvtColor(first_frame,cv2.COLOR_BGR2GRAY)

first_gray=cv2.GaussianBlur(first_gray,(5,5),0)


while True:

    _, frame = camera.read()

    frame=cv2.resize(frame,(640,480))

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    gray = cv2.GaussianBlur(gray, (5, 5), 0)

    diff=cv2.absdiff(first_gray,gray)#ilk frame ile diğer tüm framleri karşılaştırcağız.

    _,diff=cv2.threshold(diff,25,255,cv2.THRESH_BINARY)

    cv2.imshow("frame",frame)
    cv2.imshow("first_frame", first_frame)
    cv2.imshow("diff", diff)

    if cv2.waitKey(20) & 0xFF==ord("q"):
        break

camera.release()
cv2.destroyAllWindows()
