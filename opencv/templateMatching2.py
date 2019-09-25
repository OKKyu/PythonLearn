#! python3
# -*- coding:utf-8 -*-
#this sample code from
#https://www.tech-tech.xyz/3065942.html

import cv2
import numpy as np
import sys

fpath = "/home/puppy/pic/"
targetf = "Tramp/TrampAllSet.png"
templatef = "Tramp/TrampD.png"

if len(sys.argv) > 1 and sys.argv[1] is not None:
    targetf = sys.argv[1]

if len(sys.argv) > 2 and sys.argv[2] is not None:
    templatef = sys.argv[2]

#画像をグレースケールで読み込む
img = cv2.imread(fpath + targetf, cv2.IMREAD_GRAYSCALE)
temp = cv2.imread(fpath + templatef, cv2.IMREAD_GRAYSCALE)
#マッチングテンプレートを実行
result = cv2.matchTemplate(img, temp, cv2.TM_CCOEFF_NORMED)
#類似度の設定(0~1)
threshold = 0.9
#検出結果から検出領域の位置を取得
loc = np.where(result >= threshold)
#検出領域を四角で囲んで保存
result = cv2.imread(fpath + targetf)
w, h = temp.shape[::-1]
for top_left in zip(*loc[::-1]):
    bottom_right = (top_left[0] + w, top_left[1] + h)
    cv2.rectangle(result,top_left, bottom_right, (255, 0, 0), 2)
cv2.imwrite(fpath + "result2.png", result)