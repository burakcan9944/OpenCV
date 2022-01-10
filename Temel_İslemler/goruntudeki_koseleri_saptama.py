import cv2
import numpy as np


img_text=cv2.imread("text.png")
img_contour=cv2.imread("contour.png")

gray=cv2.cvtColor(img_contour,cv2.COLOR_BGR2GRAY)
fray=np.float32(gray)

corners=cv2.goodFeaturesToTrack(gray,maxCorners=50,qualityLevel=0.01,minDistance=10)#koseleri bu fonk ile bulacağız.


corners=np.int0(corners)  #çemberler çizerken float sayılar kullanılamayacağından int çeviriyoruz.

for corner in corners:
    x,y=corner.ravel()  #değerleri tek bir satır yapar.
    cv2.circle(img_contour,(x,y),3,(0,0,255),-1) #kose noktalarını oluşturduk.


cv2.imshow("corner",img_contour)

cv2.waitKey(0)
cv2.destroyAllWindows()