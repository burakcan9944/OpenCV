import cv2
import numpy as np


img=cv2.imread("starwars.jpg")
template=cv2.imread("starwars2.jpg",0)

gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

w,h=template.shape[::-1]

result=cv2.matchTemplate(gray,template,cv2.TM_CCOEFF_NORMED) #ilk başta eşleştirme yapacağım resim sonra şablonum(template)
location=np.where(result >= 0.7) #renk degeri giriyoruz.

for point in zip(*location[::-1]): # eger [::] yazarsak genislik ve yukselik degerleri oluyor.-1 eklediğimizde tersten oluyor.yukseklik ve genislik aliyor.
    cv2.rectangle(img,point,(point[0] + w,point[1] + h),(0,255,0),3)



cv2.imshow("image",img)

cv2.waitKey(0)
cv2.destroyAllWindows()