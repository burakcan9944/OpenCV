
from PIL import Image
import pytesseract

img = Image.open("C:\\Users\\Burak\\Desktop\\OpenCv\\Udemy\\resimdeki_metni_okuma\\text.png")

text= pytesseract.image_to_string(img,lang="eng")#resimde okuduğum karakterleri saklaycak

print(text)





