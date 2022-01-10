import cv2
import numpy as np

def nothing():
    pass

#camera=cv2.VideoCapture("hsv.mp4")

camera=cv2.VideoCapture(0)

cv2.namedWindow("trackbar")

cv2.createTrackbar("LH","trackbar",0,180,nothing)
cv2.createTrackbar("LS","trackbar",0,255,nothing)
cv2.createTrackbar("LV","trackbar",0,255,nothing)

cv2.createTrackbar("UH","trackbar",0,180,nothing)
cv2.createTrackbar("US","trackbar",0,255,nothing)
cv2.createTrackbar("UV","trackbar",0,255,nothing)

while True:


    _,frame=camera.read()

    frame=cv2.flip(frame,1)

    if _ is False:
        continue

    frame=cv2.resize(frame,(640,480))

    hsv=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)

    lh = cv2.getTrackbarPos("LH", "trackbar")
    ls = cv2.getTrackbarPos("LS", "trackbar")
    lv = cv2.getTrackbarPos("LV", "trackbar")

    uh = cv2.getTrackbarPos("UH", "trackbar")
    us = cv2.getTrackbarPos("US", "trackbar")
    uv = cv2.getTrackbarPos("UV", "trackbar")

    lower_blue=np.array([lh,ls,lv])
    upper_blue = np.array([uh, us, uv])

    mask=cv2.inRange(hsv,lower_blue,upper_blue)

    bitwise=cv2.bitwise_and(frame,frame,mask=mask)



    cv2.imshow("frame",frame)
    cv2.imshow("mask",mask)
    cv2.imshow("bitwise",bitwise)

    if cv2.waitKey(30) % 0xFF==ord("q"):
        break

cv2.destroyAllWindows()