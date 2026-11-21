import cv2
from PIL import Image

image_path = '314f024dc6.jpg'
doom_face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
image = cv2.imread(image_path)
cat_face = doom_face_cascade.detectMultiScale(image)
cat = Image.open(image_path)
glasses = Image.open('breutt8ycg2f1.png')
cat = cat.convert("RGBA")
glasses = glasses.convert("RGBA")

for (x,y,w,h) in cat_face:
    glasses = glasses.resize((w, int(h/3)))
    cat.paste(glasses, (x, int(y+h/4)),glasses)
    cat.save("cat_with_glasses.png")
    cat_with_glasses = cv2.imread("cat_with_glasses.png")
    cv2.imshow("Cat_with_glasses", cat_with_glasses)
    cv2.waitKey()