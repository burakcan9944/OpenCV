import cv2
import numpy as np

img_1=cv2.imread("coins.jpg")
img_2=cv2.imread("balls.jpg")

gray1=cv2.cvtColor(img_1,cv2.COLOR_BGR2GRAY)
gray2=cv2.cvtColor(img_2,cv2.COLOR_BGR2GRAY)

img1_blur=cv2.medianBlur(gray1,5)
img2_blur=cv2.medianBlur(gray2,5)

circles=cv2.HoughCircles(img1_blur,cv2.HOUGH_GRADIENT,1,img_1.shape[0]/4,param1=200,param2=10,minRadius=15,maxRadius=80)#minDist az değer değer girersek çok
# fazla çember olucaktır ve hatada artıcaktır.paramlar metoda özel parametrelerdir.Doğrudan bu sayiları girmelisiniz
#param1= gradient değeri,param2=threshold değeridir.

if circles is not None:

    circles=np.uint16(np.around(circles)) #verileri tuttuğu aralığı 16 yaptık.circles içerisnde
    #tuttuğu değerleri yuvarlıyoruz.

    for i in circles[0,:]:
        cv2.circle(img_1, (i[0],i[1]),i[2],(0,255,0),2)


cv2.imshow("img1",img_1)

cv2.waitKey(0)
cv2.destroyAllWindows()


