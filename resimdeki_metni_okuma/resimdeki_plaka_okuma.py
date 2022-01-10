import cv2
import numpy as np
import pytesseract
import imutils


img=cv2.imread("licence_plate.jpg")

gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

filtered=cv2.bilateralFilter(gray,6,250,250)

edges=cv2.Canny(filtered,30,200)

contours=cv2.findContours(edges,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

cnts=imutils.grab_contours(contours) #uygun konturları yakala.

cnts=sorted(cnts,key=cv2.contourArea,reverse=True)[:10] #içine girdiğimiz değerleri sıralar
#key olarak yazdığımızda alana göre sıralama yapıyor.Reverse=True da girdiğimiz değerleri tersten sıralıyor.
#0 dan 10 a kadar olan değerler için yap.

screen= None  #kapalı bir şekil bulabildimmi yoksa bulamadımmı onun içindir bulduğumuzda None olamayacaktır.

for c in cnts:
    epsilon=0.018 * cv2.arcLength(c,True)

    approx=cv2.approxPolyDP(c,epsilon,True)

    if len(approx==4): #eğer 4 tane ise burda dikdörtgen var
        screen=approx
        break
mask=np.zeros(gray.shape,np.uint8) #gray.shape demek grayın içinde tuttuğu boyutlar kadar değer olucak.

new_img=cv2.drawContours(mask,[screen],0,(255,255,255),-1)

new_img=cv2.bitwise_and(img,img,mask=mask)

(x,y)=np.where(mask==255)#beyaz bölgeleri x,y de tut.

(topx,topy)=(np.min(x),np.min(y))

(bottomx,bottomy)=(np.max(x),np.max(y))

cropped= gray[topx:bottomx+1,topy:bottomy+1]#kırpılmış.1 fazlasına da alalım ki son değer de gelsin

cv2.imshow("new_img",cropped)

cv2.waitKey(0)
cv2.destroyAllWindows()