#! python3
# -*- coding:utf-8 -*-
#this sample code from
#https://www.tech-tech.xyz/haar-cascade.html

import cv2
import sys

fpath = "/home/puppy/pic/"
cascadepath = "/usr/local/lib/python3.5/dist-packages/cv2/data/"
targetf = "opencv_cascadetest/owarai_wagyu.jpeg"

if len(sys.argv) > 1 and sys.argv[1] is not None:
    targetf = sys.argv[1]

img = cv2.imread(fpath + targetf)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#カスケードファイルの読み込み
face_cascade = cv2.CascadeClassifier(cascadepath + 'haarcascade_frontalface_default.xml')
#カスケードファイル使って顔認証
faces = face_cascade.detectMultiScale(gray)
for (x,y,w,h) in faces:
    #顔部分を四角で囲う
    cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
    cv2.imshow('img',img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


#other cascade xml
#haarcascade_eye.xml
#haarcascade_eye_tree_eyeglasses.xml
#haarcascade_frontalcatface.xml
#haarcascade_frontalcatface_extended.xml
#haarcascade_frontalface_alt.xml
#haarcascade_frontalface_alt2.xml
#haarcascade_frontalface_alt_tree.xml
#haarcascade_frontalface_default.xml
#haarcascade_fullbody.xml
#haarcascade_lefteye_2splits.xml
#haarcascade_licence_plate_rus_16stages.xml
#haarcascade_lowerbody.xml
#haarcascade_profileface.xml
#haarcascade_righteye_2splits.xml
#haarcascade_russian_plate_number.xml
#haarcascade_smile.xml
#haarcascade_upperbody.xml
