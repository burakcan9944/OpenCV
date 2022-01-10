import cv2
import numpy as np

img=cv2.imread("map.jpg")

gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

blur=cv2.blur(gray,(3,3))

ret,thres=cv2.threshold(blur,40,255,cv2.THRESH_BINARY)

contours,hierarchy=cv2.findContours(thres,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

hull = [] #Noktaları buldukça bunun içerisine atacağız.

for i in range(len(contours)): #sıfırdan countoursun uzunluğuna kadar dödürecek.
    hull.append(cv2.convexHull(contours[i],False)) #false contours'un indisini döndürecek.

background=np.zeros((thres.shape[0],thres.shape[1],3),np.uint8)

for i in range(len(contours)):
    cv2.drawContours(background,contours,i,(255,0,0),thickness=3,lineType=8) #burada çizim yapıyoruz

    cv2.drawContours(background, hull, i, (0, 255, 0), thickness=1, lineType=8)#burası direk iç bükeyleri alamdan çizgiler

cv2.imshow("img",background)

cv2.waitKey(0)
cv2.destroyAllWindows()
