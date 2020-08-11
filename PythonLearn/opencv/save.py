#! python3
# -*- coding:utf-8 -*-

import numpy as np
import cv2

img = cv2.imread('/home/puppy/pic/UriHamushi.jpg', cv2.IMREAD_GRAYSCALE)
cv2.imshow('image',img)
k = cv2.waitKey(0)
if k == ord('s'): # wait for 's' key to save and exit
    cv2.imwrite('/home/puppy/pic/UrihamushiGray.png',img)
    cv2.destroyAllWindows()