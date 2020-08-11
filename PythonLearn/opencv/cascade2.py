#! python3
# -*- coding:utf-8 -*-
#this sample code from
#https://www.tech-tech.xyz/haar-cascade.html

import cv2
import sys

fpath = "/home/puppy/pic/"
cascadepath = "./"
targetf = "tentaikansoku_1p.jpg"

if len(sys.argv) > 1 and sys.argv[1] is not None:
    targetf = sys.argv[1]

img = cv2.imread(fpath + targetf)
#gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#カスケードファイルの読み込み
try:
    box_cascade = cv2.CascadeClassifier(cascadepath + 'cascade.xml')
    boxes = box_cascade.detectMultiScale(img)
    for (x,y,w,h) in boxes:
        #四角で囲う
        cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
except Exception as ex:
    print(ex)

cv2.namedWindow('img',cv2.WINDOW_NORMAL)
cv2.resizeWindow('img',800,800)
cv2.imshow('img',img)

cv2.imwrite("/home/puppy/pic/result.jpg", img)

cv2.waitKey(0)
cv2.destroyAllWindows()
