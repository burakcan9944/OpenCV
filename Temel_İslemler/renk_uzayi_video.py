import cv2
import numpy as np


camera=cv2.VideoCapture("yuruyus.mp4")

while True:
    ret,frame=camera.read() #ret True ve False değerini döndürür.

    frame=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

    if ret==False:  #video bittikten sonra alınan hata("video bitti ben ne yapayım" diyor) götürmek içindir.
        break

    cv2.imshow("video",frame)

    if cv2.waitKey(30) & 0xFF == ord("q"):

        break


cv2.destroyAllWindows()