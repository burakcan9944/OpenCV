import cv2
import numpy as np


img=cv2.imread("Strange Horizon.png",0)

row,col=img.shape

matrix=np.float32([[1,0,50],[0,1,100]]) #ilk koseli parantex x'dir,digeride y'dir.girdiğimiz değerler resmin siyah kısım ile olan mesafesidir.
print(matrix)

dst = cv2.warpAffine(img,matrix,(row,col)) #resmi istediğimiz kadar kaydırabiliyoruz.

cv2.imshow("dst",dst)


cv2.waitKey(0)
cv2.destroyAllWindows()