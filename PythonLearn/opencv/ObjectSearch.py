#! python3
# -*- coding:utf-8 -*-
#rinkaku kenshutsu

import cv2
import numpy as np

circle = np.zeros((400,400,3), np.uint8)
#image,center point,length,color(BGR),thickness
cv2.circle(circle,(32,64), 32, (0,0,255), -1)
cv2.imshow("circle",circle)
cv2.waitKeyEx(0)

imgray = cv2.cvtColor(circle,cv2.COLOR_BGR2GRAY)

#threshold param 
# src: 入力画像
# threshold: 閾値
# maxValue: cv2.THRESH_BINARY, cv2.THRESH_BINARY_INV の場合に使用する
# thresholdType: Thresholding の方式 
#ret,thresh = cv2.threshold(imgray,127,255,0)
#image, contours, hierarchy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

contours, hierarchy = cv2.findContours(imgray,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
# contours, drawContour's Index, Contour's color(BGR), thickness
circle = cv2.drawContours(circle, contours, -1, (0,255,0), 5)
cv2.imshow("circle",circle)
cv2.waitKeyEx(0)

#calculate area size
for contour in contours:
    print("result contourArea:" + str(cv2.contourArea(contour)))
    x,y,w,h = cv2.boundingRect(contour)
    
    #display rectangle region.
    circle = cv2.rectangle(circle,(x,y),(x+w,y+h),(0,0,255),1)
    cv2.imshow("circle",circle)
    cv2.waitKeyEx(0)
    
    #cropping
    cv2.imshow("circle",circle[y:y+h,x:x+w])
    cv2.waitKeyEx(0)


