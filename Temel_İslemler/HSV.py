import cv2
import numpy as np

camera=cv2.VideoCapture(0)

def nothing(x):
    pass

cv2.namedWindow("image")
cv2.resizeWindow("image",600,400)

cv2.createTrackbar("LowerH","image",0,180,nothing)
cv2.createTrackbar("LowerS","image",0,255,nothing)
cv2.createTrackbar("LowerV","image",0,255,nothing)

cv2.createTrackbar("UpperH","image",0,180,nothing)
cv2.createTrackbar("UpperS","image",0,255,nothing)
cv2.createTrackbar("UpperV","image",0,255,nothing)

cv2.setTrackbarPos("UpperH","image",180)# varsayılan olarak sıfırdan başlayacaktır ama sonu sıfırdan başlamasın istediğim içindir.
cv2.setTrackbarPos("UpperS","image",255)
cv2.setTrackbarPos("UpperV","image",255)


while True:

    ret,frame=camera.read()
    frame=cv2.flip(frame,1) #görüntüyü takla attıtıyoruz.Y eksenine göre yansımasını alıyoruz.

    frame_hsv=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)

    lowerh = cv2.getTrackbarPos("LowerH","image")
    lowers = cv2.getTrackbarPos("LowerS", "image")
    lowerv = cv2.getTrackbarPos("LowerV", "image")

    upperh = cv2.getTrackbarPos("UpperH", "image")
    uppers = cv2.getTrackbarPos("UpperS", "image")
    upperv = cv2.getTrackbarPos("UpperV", "image")

    lower_color=np.array([lowerh,lowers,lowerv])#değişkenleri tek bir yer topladık.
    upper_color = np.array([upperh, uppers, upperv])

    mask=cv2.inRange(frame_hsv,lower_color,upper_color) #bu foksiyonumuz ise girilen değerler arasındaki renkleri seçmeye yarar. Mesela mavi rengin taban ve tavan renklerini girersek fonksiyona, kolaylıkla mavi rengi görüntümüz arasından seçebiliriz.

    if ret==False:  #video bittikten sonra alınan hata("video bitti ben ne yapayım" diyor) götürmek içindir.
        break

    cv2.imshow("orj",frame)
    cv2.imshow("Mask",mask)

    if cv2.waitKey(5) & 0xFF==ord("q"):
        break




camera.release()
cv2.destroyAllWindows()