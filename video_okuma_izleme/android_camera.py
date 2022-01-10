import cv2
import time
import requests
import numpy as np

url="http://192.168.0.27:8080//shot.jpg" #cameradan her bir shot alıyoruz
while True:
    img_resp=requests.get(url)
    img_arr=np.array(bytearray(img_resp.content), dtype=np.uint8)  #aldığımız görüntüyü byt'a çevirdik
    img=cv2.imdecode(img_arr, cv2.IMREAD_COLOR)  #hafızadan çektiği görüntüyü görütülebilir hale getirecektir.ımread_colola renkli görüntü alır.
    img=cv2.resize(img,(640,480))

    cv2.imshow("Android camera",img)

    if cv2.waitKey(1)==27:
        break



cv2.destroyAllWindows()