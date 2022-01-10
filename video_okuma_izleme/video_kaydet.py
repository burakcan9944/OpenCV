import cv2

camera=cv2.VideoCapture(0,cv2.CAP_DSHOW)#hata olamamk için cap_dshow yapıldı.

filename= "C:\Amazon Games\camera.avi" #videoyu buraya kayıt edemiyorum çünkü \u gelir ise python onu komt olarak algılıyor.ondan dolayı amazona adres verildi

codec=cv2.VideoWriter_fourcc('W','M','V','2')#Bu 4 değerede fourcc sitesinden bakabilirsin(farklı olanalrı da var)

frameRate=30

resolution=(640,480)#çözünürlük degeri.



videoFileOutput=cv2.VideoWriter(filename,codec,frameRate,resolution)#codec=ses ve görünütden oluşur videolar.kod çözücüler bu ses algoritmalarını tanırlar.

while True:
    ret,frame=camera.read()

    frame=cv2.flip(frame,1)

    videoFileOutput.write(frame)

    cv2.imshow("camera",frame)

    if cv2.waitKey(30) % 0xFF==ord("q"):
        break

videoFileOutput.release()
camera.release()
cv2.destroyAllWindows()











