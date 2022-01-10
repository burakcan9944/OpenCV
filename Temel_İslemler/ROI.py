import cv2
import numpy as np

img=cv2.imread("world.jpg")

#dimension=img.shape #resmin boyutlarını öğrendim.(y:1600,x: 2560, 3)
#print(dimension) #resmin boyutlarını öğrendim.


roi=img[150:450,800:1200] #resmin grönland'ı almaya çalıştık.(y,x)

cv2.imshow("img",img)
cv2.imshow("roi",roi)

cv2.waitKey(0)
cv2.destroyAllWindows()
