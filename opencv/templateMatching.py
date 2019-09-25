#! python3
# -*- coding:utf-8 -*-
#this sample code from
#https://www.tech-tech.xyz/3065942.html

import cv2

fpath = "/home/puppy/pic/"

#画像をグレースケールで読み込む
img = cv2.imread(fpath + "TrampAllSet.png", cv2.IMREAD_GRAYSCALE)
temp = cv2.imread(fpath + "TrampD4.png", cv2.IMREAD_GRAYSCALE)

#マッチングテンプレートを実行
#比較方法はcv2.TM_CCOEFF_NORMEDを選択
# args:入力画像、テンプレート画像、比較方法
# return:各画素が入力画像とテンプレート画像の類似度を表すグレースケール画像になります。
# cv2.TM_CCOEFF_NORMEDだと類似度が高いほど明るくなる.maxが類似度高.
result = cv2.matchTemplate(img, temp, cv2.TM_CCOEFF_NORMED)
cv2.imshow("after matchTemplate",result)
cv2.waitKey(0)

#検出結果から検出領域の位置を取得
min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
top_left = max_loc
w, h = temp.shape[::-1]
bottom_right = (top_left[0] + w, top_left[1] + h)
#検出領域を四角で囲んで保存
result = cv2.imread(fpath + "TrampAllSet.png")
cv2.rectangle(result,top_left, bottom_right, (255, 0, 0), 2)
cv2.imwrite(fpath + "result.png", result)

