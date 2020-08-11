#! python3
# -*- coding:utf-8 -*-
import cv2
import numpy as np
import sys

# Create a black background image
line = np.zeros((512,512,3), np.uint8)

# Draw a diagonal blue line with thickness of 5 px
# bgImage,start point,end point,color(BGR),thickness
cv2.line(line,(0,0),(511,511),(255,0,0),5)
cv2.imshow("line",line)
cv2.waitKeyEx(0)

cv2.line(line,(52,0),(511,511),(0,255,0),12)
cv2.imshow("line",line)
cv2.waitKeyEx(0)
cv2.destroyWindow("line")

# rectangle
# bgImage,start point,end point,color(BGR),thickness
rect = np.zeros((512,512,3), np.uint8)
cv2.rectangle(rect,(384,0),(510,128),(0,255,0),3)
cv2.imshow("rect",rect)
cv2.waitKeyEx(0)
cv2.destroyWindow("rect")

#put text
#added target image, text, stPoint,font,?, color(BGR),thickness,linetype?
font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(rect,'OpenCV',(10,500), font, 4,(255,255,255),2,cv2.LINE_AA)
cv2.imshow("img",rect)
cv2.waitKeyEx(0)

img = cv2.imread('/home/puppy/pic/pillowBasic001.jpg')
img = cv2.resize(img,(int(img.shape[1] * 0.25), int(img.shape[0] * 0.25)))
cv2.putText(img,'OpenCV',(20,30), font, 1, (255,255,255),2,cv2.LINE_AA)
cv2.imshow("img",img)
cv2.waitKeyEx(0)
cv2.destroyAllWindows()

sys.exit(0)