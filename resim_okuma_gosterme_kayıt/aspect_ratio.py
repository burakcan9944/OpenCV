import cv2


def resizewithApectRation(img,width=None,height=None,inter=cv2.INTER_AREA):

    dimension=None
    (h,w)=img.shape[:2]

    if width is None and height is None:
        return img

    if width is None:
        r=height / float(h)
        dimension=(int(w*r),height)

    else:
        r=width / float(w)
        dimension=(width, int(h*r))

    return cv2.resize(img,dimension,interpolation=inter)

img =cv2.imread("kabus_orman.png")
img1=resizewithApectRation(img,width=None,height=600,inter=cv2.INTER_AREA)

cv2.imshow("original",img)
cv2.imshow("Rezided",img1)

cv2.waitKey()
cv2.destroyAllWindows()





