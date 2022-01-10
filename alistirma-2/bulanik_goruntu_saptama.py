import cv2
import numpy as np

img=cv2.imread("starwars.jpg")

blur=cv2.medianBlur(img,9)

laplacian=cv2.Laplacian(blur,cv2.CV_64F).var() #blurlu olup olmadigi anlayacagiz.laplacian degeri belli bir threshold degerinin altindaysa blurlu diyebilizriz.

#print(laplacian) #blurlama arttiginda lablacian degeri duser.

if laplacian < 500:
    print("this image is blurry")

cv2.imshow("img",img)
cv2.imshow("blur",blur)

cv2.waitKey(0)
cv2.destroyAllWindows()
