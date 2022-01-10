import cv2
import numpy as np


camera=cv2.VideoCapture("car.mp4")

subtractor= cv2.createBackgroundSubtractorMOG2(history=100,varThreshold=120,detectShadows=True) #bu fonksiyon diğer 1. de yaptığımız daha iyi halini yapar.
#history 100 almamın sebebi her bir frame değişen bazı koşullar olabilir.mesela güneşin hareketinde dolayı gölgeler değişebilir.


while True:


    _,frame=camera.read()

    frame=cv2.resize(frame,(640,480))

    mask=subtractor.apply(frame)


    cv2.imshow("frame",frame)
    cv2.imshow("mask",mask)






    if cv2.waitKey(20) % 0xFF==ord("q"):
        break

camera.release()
cv2.destroyAllWindows()