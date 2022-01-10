import cv2
import numpy as np

window="Live video"
cv2.namedWindow(window)


camera=cv2.VideoCapture(0)

print("Width: "+str(camera.get(3))) #camera.get(3) yazdigimizda bana cameradaki goruntunun 3 yazidigimda
#enini,4 yazdigimizda yuksekligini verir.stringe cevirip "Width" yanina eklesin diye.

print("Height: "+str(camera.get(4)))

camera.set(3,1280) #ilk başta içine degistirmek istedigimiz ekseni yazarız sonra yaninada cozunurluk girilir.
camera.set(4,720)

print("Width*: "+str(camera.get(3)))
print("Height*: "+str(camera.get(4)))

while True:
    ret,frame=camera.read()

    frame=cv2.flip(frame,1)

    cv2.imshow(window,frame)

    if ret is False:
        break

    if cv2.waitKey(1) & 0xFF==ord("q"):
        break




camera.release()
cv2.destroyAllWindows()