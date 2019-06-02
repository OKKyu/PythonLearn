#! python3
# -*- coding:utf-8 -*-
import cv2

img = cv2.imread('/home/puppy/pic/pillowBasic001.jpg', cv2.IMREAD_COLOR)
cv2.imshow("image",img)
cv2.waitKey(0)
cv2.destroyAllWindows()