import cv2


camera = cv2.VideoCapture("video-2.mp4")
#camera=cv2.VideoCapture(0)

while True:
    ret, frame = camera.read()  # ret kameranın calısıp calısmadıgını kontrol edeicek.
    if ret== 0:
        break

    frame=cv2.flip(frame,1)  #aldığınız her görütüyü istediğimiz eksenlere yansıtır.1=y eksenine göre yansıtılarak görünür.(-1 orjine göre)

    cv2.imshow("camera", frame)

    if cv2.waitKey(30) & 0xFF == ord("q"): # 30 m/S bir goruntu cek ve cikisda sunduk.
        break


camera.release()  # okutmuyorum.

cv2.destroyAllWindows()















