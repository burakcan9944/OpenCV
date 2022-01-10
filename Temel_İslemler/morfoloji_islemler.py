import cv2
import numpy as np


img=cv2.imread("Strange Horizon.png",0)

kernel=np.ones((5,5),np.uint8)

eresion=cv2.erode(img,kernel,iterations=1)  #resmi erzyona uğratır.
dilation = cv2.dilate(img,kernel,iterations=1) #Beyazları kalınlaştırmadır.
opening=cv2.morphologyEx(img,cv2.MORPH_OPEN,kernel,iterations=1) #resmi dışındaki bozulmayı ve gurultuyu kaldırır.
closing=cv2.morphologyEx(img,cv2.MORPH_CLOSE,kernel,iterations=1) #resmideki bozulmayı ve gurultuyu kaldırır.
gradient=cv2.morphologyEx(img,cv2.MORPH_GRADIENT,kernel,iterations=1) #resmin dış kısmını çizmiştir.
tophat=cv2.morphologyEx(img,cv2.MORPH_TOPHAT,kernel,iterations=1)



cv2.imshow("eresion",eresion)
cv2.imshow("dilation",dilation)
cv2.imshow("opening",opening)
cv2.imshow("closing",closing)
cv2.imshow("gradient",gradient)
cv2.imshow("tophat",tophat)


cv2.waitKey(0)
cv2.destroyAllWindows()
