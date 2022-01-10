import cv2
import numpy as np


img=cv2.imread("Strange Horizon.png")



#dimesion=img.shape #Resmin boyutların ve kanal verisini verir.

#print(dimesion)
#color=img[150,200]
#print(color)

#blue=img[150,200,0] # sonuncusu (0) indeks numarasi.
#print(blue)

blue1=img.item(150,200,0)
print("blue1:",blue1)

new_blue1=img.itemset((150,200,0), 172) #öncelikle kordinatları ve hangi renk değerini değiştirmek istediğimizi giriyoruz.

print("yeni blue1:",img[150,200,0])

cv2.imshow("img",img)


cv2.waitKey(0)
cv2.destroyAllWindows()
