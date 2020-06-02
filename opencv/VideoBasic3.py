#! python3
# -*- coding:utf-8 -*-
# 『Pythonで始めるOpenCV4プログラミング』
#  北山尚洋

import cv2
import sys,traceback
import numpy as np

capture = None
try:
    capture = cv2.VideoCapture(0)
    
    while True:
        ret, img = capture.read()
        
        #display simple
        cv2.imshow("simple", img)

        #gray scale
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        cv2.imshow("cvtColor", gray)

        #hist
        cv2.imshow("equalizeHist", cv2.equalizeHist(gray))

        #canny
        canny = cv2.Canny(img,40.0,200.0)
        cv2.imshow("canny", canny)
        
        #laplacian and erode
        eroded = cv2.erode(img, np.ones((3,3), np.uint8))
        lap = cv2.Laplacian(eroded, -1)
        cv2.imshow("laplacian", lap)
        
        key = cv2.waitKey(1)
        if key & 0xFF == ord('q'):
            break
    
except Exception as ex:
    pass
finally:
    if capture is not None:
        capture.release()
    cv2.destroyAllWindows()