
import numpy as np
import cv2

img=cv2.imread("Strange Horizon.png",0)

row,col=img.shape

matrix=cv2.getRotationMatrix2D((col/2,row/2),90,1) #2 boyutta bir yön değitirme rotasyonu uyguluyoruz.90 derece dödürür.

dst=cv2.warpAffine(img,matrix,(col,row))

cv2.imshow("dst",dst)


cv2.waitKey(0)
cv2.destroyAllWindows()








