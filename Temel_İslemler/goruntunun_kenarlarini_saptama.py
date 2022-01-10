import cv2
import numpy as np


camera=cv2.VideoCapture(0)

while True:
    ret,frame=camera.read()

    frame=cv2.flip(frame,1)

    edges=cv2.Canny(frame,100,200)

    cv2.imshow("frame",frame)

    cv2.imshow("edges",edges)

    if cv2.waitKey(5) & 0xFF ==ord("q"):

        break





camera.release()
cv2.destroyAllWindows()