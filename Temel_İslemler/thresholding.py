import cv2
import numpy as np
from matplotlib import pyplot as plt

img=cv2.imread("Strange Horizon.png",0)

ret,th1=cv2.threshold(img,50,255,cv2.THRESH_BINARY)
th2=cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,11,2)
th3=cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,11,2)


#cv2.imshow("orj",img)
cv2.imshow("th1",th1)
cv2.imshow("th2",th2)
cv2.imshow("th3",th3)



cv2.waitKey(0)
cv2.destroyAllWindows()