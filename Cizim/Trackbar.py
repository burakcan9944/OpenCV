import cv2
import numpy as np

def nothing(x):
    pass

canvas=np.zeros((512,512,3),np.uint8) +255

cv2.namedWindow("image") #tragbar arayüzünü bu rengini değiştireceğimiz pencereye yerleştirmek için.

cv2.createTrackbar("R","image",0,255,nothing) #taskbar adı,yerleşeceği pencerenin adı,başlangıç ve bitiş değerleri
cv2.createTrackbar("G","image",0,255,nothing)
cv2.createTrackbar("B","image",0,255,nothing)

switch="0:OFF,1:ON"
cv2.createTrackbar(switch,"image",0,1,nothing) #açma kapama


while True: #devamlı renklerin yenilenmesini istemekdeğiz.

    cv2.imshow("image",canvas)


    if cv2.waitKey(1) & 0xFF ==ord("q"):
        break

    r = cv2.getTrackbarPos("R", "image") #kızakların konumlarını alıp bir değişkende saklamalıyız.
    g = cv2.getTrackbarPos("G", "image")
    b = cv2.getTrackbarPos("B", "image")
    s = cv2.getTrackbarPos(switch,"image")

    if s==0:
        canvas[:]=[0,0,0] #bütün pikselleri siyah yapar çünkü kapalı

    elif s==1:
        canvas[:]=[b,g,r] #bütün piksel deperlerinin rengini değiştirilebilir olur.


cv2.destroyAllWindows()