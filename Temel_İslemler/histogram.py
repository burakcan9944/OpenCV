import cv2
import numpy as np
from matplotlib import pyplot as plt


#img=np.zeros((500,500),np.uint8)
img=cv2.imread("Strange Horizon.png")

B,G,R=cv2.split(img)

#cv2.rectangle(img,(50,100),(150,200),color=(255,255,255),thickness=-1)
#cv2.rectangle(img,(400,400),(450,450),color=(255,255,255),thickness=-1)

cv2.imshow("img",img)

#plt.hist(img.ravel(),256,[0,256]) #histogramı çizicez.ravel tüm pikseli alıp tek bir satır haline döküyor.0-255 renk degerleridir.

plt.hist(B.ravel(),256,[0,256])
plt.hist(G.ravel(),256,[0,256])
plt.hist(R.ravel(),256,[0,256])

plt.show() #bunlada gostericez


cv2.waitKey(0)
cv2.destroyAllWindows()

