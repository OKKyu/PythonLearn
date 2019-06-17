#! python3
# -*- coding:utf-8 -*-
#rinkaku kenshutsu

import cv2
import numpy as np

circle = np.zeros((400,400,3), np.uint8)
#image,center point,length,color(BGR),?
cv2.circle(circle,(200,64), 32, (0,0,255), -1)
cv2.imshow("circle",circle)
cv2.waitKeyEx(0)

imgray = cv2.cvtColor(circle,cv2.COLOR_BGR2GRAY)
#ret,thresh = cv2.threshold(imgray,127,255,0)
#image, contours, hierarchy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
contours, hierarchy = cv2.findContours(imgray,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
# contours, drawContour's Index, Contour's color(BGR), thickness
circle = cv2.drawContours(circle, contours, -1, (0,255,0), 5)
cv2.imshow("circle",circle)
cv2.waitKeyEx(0)