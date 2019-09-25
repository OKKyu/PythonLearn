#! python3
# -*- coding:utf-8 -*-
#this sample code from
#https://www.tech-tech.xyz/sift-surf-akaze.html

import numpy as np
import cv2
import sys

fpath = "/home/puppy/pic/"
targetf = "dollar/d2.jpg"
templatef = "dollar/d_template.png"

if len(sys.argv) > 1 and sys.argv[1] is not None:
    targetf = sys.argv[1]

if len(sys.argv) > 2 and sys.argv[2] is not None:
    templatef = sys.argv[2]

img1 = cv2.imread(fpath + targetf,0)
img2 = cv2.imread(fpath + templatef,0)
#特徴抽出機の生成
detector = cv2.AKAZE_create()
#kpは特徴的な点の位置 destは特徴を現すベクトル
kp1, des1 = detector.detectAndCompute(img1, None)
kp2, des2 = detector.detectAndCompute(img2, None)
#特徴点の比較機
bf = cv2.BFMatcher()
matches = bf.knnMatch(des1,des2, k=2)
#割合試験を適用
good = []
match_param = 0.9
for m,n in matches:
    if m.distance < match_param*n.distance:
        good.append([m])
#cv2.drawMatchesKnnは適合している点を結ぶ画像を生成する
img3 = cv2.drawMatchesKnn(img1,kp1,img2,kp2,good, None,flags=2)
#img3 = cv2.drawMatchesKnn(img1,kp1,img2,kp2,matches, None,flags=2)
cv2.imwrite(fpath + "shift_result.png", img3)