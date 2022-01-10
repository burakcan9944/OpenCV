import cv2
import numpy
import matplotlib



img=cv2.imread("kabus_orman.png")

cv2.namedWindow("image",cv2.WINDOW_NORMAL)  #pencereyi büyütüp küçültebiliyoruz.

cv2.imshow("image",img)

cv2.imwrite("klon-1.jpg",img) #resmin başka bir şekilde kayderder.

cv2.waitKey(0)
cv2.destroyAllWindows()





