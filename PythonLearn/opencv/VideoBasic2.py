#! python3
# -*- coding:utf-8 -*-
import cv2

cap = cv2.VideoCapture(0)

for i in range(0,19):
  print("" + str(cap.get(i)))

cap.release()
