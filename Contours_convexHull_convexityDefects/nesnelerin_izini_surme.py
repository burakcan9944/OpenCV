import cv2
import numpy as np


camera=cv2.VideoCapture("dog.mp4")

while True:

    ret,frame=camera.read()

    hsv =cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)

    sensitivity=15

    lower_white=np.array([0,0,255-sensitivity]) #lower ve upperda kopeğin olduğu beyaz rengi bulmaya
    # çalışıyoruz.arrayin içinde yaptığımız işlemler beyaz rengin kodlarıdır.
    # Bunları googledan aratarak bulmalısın.Mesala kırmızı için "hsv code for red"

    upper_white=np.array([255,sensitivity,255])

    mask=cv2.inRange(hsv,lower_white,upper_white)

    res=cv2.bitwise_and(frame,frame,mask=mask) #maskın doğru uygulanabilmesi için bu fonk yazılır.
    #iki adet frame yazmamızın nedeni iki kere döngü oluyor.



    if ret==False:
        break


    cv2.imshow("frame",frame)
    cv2.imshow("mask", mask)
    cv2.imshow("result", res)


    if cv2.waitKey(30) % 0xFF==ord("q"):
        break





cv2.destroyAllWindows()