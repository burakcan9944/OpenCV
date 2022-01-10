#f(x,y) = x*a + y*b + c


import cv2
import numpy as np


circle=np.zeros((512,512,3),np.uint8) +255

cv2.circle(circle,center=(206,206),radius=100,color=(0,0,255),thickness=-1)

rectangle=np.zeros((512,512,3),np.uint8)+255

cv2.rectangle(rectangle,(100,100),(300,300),color=(255,0,0),thickness=-1)

dst=cv2.addWeighted(circle,0.3,rectangle,0.7, 0)


cv2.imshow("circle",circle)
cv2.imshow("rectangle",rectangle)
cv2.imshow("dst",dst)

cv2.waitKey(0)
cv2.destroyAllWindows()