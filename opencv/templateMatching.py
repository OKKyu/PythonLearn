#! python3
# -*- coding:utf-8 -*-
#this sample code from
#https://www.tech-tech.xyz/3065942.html

import cv2

#file root folder.
fpath = "/home/puppy/pic/Tramp/"
targetImg = "TrampAllSet.png"
templateImg = "TrampD4.png"

#setup method
def matching(img, temp, imgName, tempName):
  #マッチングテンプレートを実行
  #比較方法はcv2.TM_CCOEFF_NORMEDを選択
  # args:入力画像、テンプレート画像、比較方法
  # return:各画素が入力画像とテンプレート画像の類似度を表すグレースケール画像になります。
  # cv2.TM_CCOEFF_NORMEDだと類似度が高いほど明るくなる.maxが類似度高.
  result = cv2.matchTemplate(img, temp, cv2.TM_CCOEFF_NORMED)
  cv2.imshow("after matchTemplate",result)
  cv2.waitKey(0)
  cv2.destroyWindow("after matchTemplate")
  
  #検出結果から検出領域の位置を取得
  min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
  top_left = max_loc
  w, h = temp.shape[::-1]
  bottom_right = (top_left[0] + w, top_left[1] + h)
  #検出領域を四角で囲んで保存
  result = cv2.imread(fpath + imgName)
  result = cv2.resize(result, (img.shape[1], img.shape[0]))
  cv2.rectangle(result,top_left, bottom_right, (255, 0, 0), 2)
  cv2.imwrite(fpath + "result.png", result)
  
  cv2.imshow(tempName + " Searched...", result)
  cv2.waitKey(0)
  cv2.destroyAllWindows()  

#そのままテンプレートを検索した場合
#画像をグレースケールで読み込む
img = cv2.imread(fpath + targetImg, cv2.IMREAD_GRAYSCALE)
temp = cv2.imread(fpath + templateImg, cv2.IMREAD_GRAYSCALE)
matching(img, temp, targetImg, templateImg)

#実験１ テンプレート画像を少しリサイズしてみる
temp = cv2.imread(fpath + templateImg, cv2.IMREAD_GRAYSCALE)
temp = cv2.resize(temp,(int(temp.shape[1] -10),  int(temp.shape[0] -10)))
cv2.imshow("resized template",temp)
cv2.waitKey(0)
cv2.destroyWindow("resized template")
matching(img, temp, targetImg, templateImg)

#実験２ テンプレート画像を半分に縮小してみる
temp = cv2.imread(fpath + templateImg, cv2.IMREAD_GRAYSCALE)
temp = cv2.resize(temp,(int(temp.shape[1] * 0.5),  int(temp.shape[0] * 0.5)))
cv2.imshow("resized template",temp)
cv2.waitKey(0)
cv2.destroyWindow("resized template")
matching(img, temp, targetImg, templateImg)

#実験３テンプレート画像だけでなく検索対象も半分に縮小してみる
img = cv2.imread(fpath + targetImg, cv2.IMREAD_GRAYSCALE)
img = cv2.resize(img,(int(img.shape[1] * 0.5),  int(img.shape[0] * 0.5)))
cv2.imshow("resized img",img)
cv2.waitKey(0)
cv2.destroyWindow("resized img")
matching(img, temp, targetImg, templateImg)