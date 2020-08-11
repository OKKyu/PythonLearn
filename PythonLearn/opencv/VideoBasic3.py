#! python3
# -*- coding:utf-8 -*-
# 『Pythonで始めるOpenCV4プログラミング』
#  北山尚洋

import cv2
import sys,traceback
import numpy as np

def adjustImShow(wname,img,height,width):
    cv2.namedWindow(wname, cv2.WINDOW_NORMAL)
    cv2.resizeWindow(wname,height,width)
    cv2.imshow(wname,img)

capture = None
try:
    capture = cv2.VideoCapture(0)
    
    imgList = []
    while True:
        ret, img = capture.read()
        
        #display simple
        adjustImShow("simple", img,800,800)

        #gray scale
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        adjustImShow("gray", gray,800,800)
        
        #canny
        #canny = cv2.Canny(img,40.0,200.0)
        canny = cv2.Laplacian(img, -1)
        adjustImShow("canny", canny,800,800)
        
        #noize reduction
        if len(imgList) > 10:
            imgList.pop(0)
            reduced = np.average(imgList, axis=(0))
            reduced = np.array(reduced, dtype=np.uint8)
            #reduced = cv2.Canny(reduced, 40.0, 200.0)
            reduced = cv2.Laplacian(reduced, -1)
            adjustImShow("reduced", reduced,800,800)
            
        imgList.append(img)
            
        #ret,dst = cv2.threshold(lap,15,255,cv2.THRESH_BINARY)
        #contours = cv2.findContours(gaus, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)[-2]
        #for contour in contours:
        #    if cv2.contourArea(contour) > int(500):
        #        x,y,w,h = cv2.boundingRect(contour)
        #        cv2.rectangle(dst,(x,y), (x+w,y+h), (0,255,0),5)        
        
        #adjustImShow("dst", dst,800,800)
        
        key = cv2.waitKey(1)
        if key & 0xFF == ord('q'):
            break
    
except Exception as ex:
    print("Error:", sys.exc_info()[0])
    print(sys.exc_info()[1])    
finally:
    if capture is not None:
        capture.release()
    cv2.destroyAllWindows()