#! python3
# -*- coding:utf-8 -*-

import numpy as np
import cv2
import sys
from pathlib import Path
import matplotlib as plt

def execScan(path, target):
    #read src image
    img = cv2.imread(str(target))
    #img = cv2.resize(img,(1024, 1024))
    #cv2.imshow("beforeContours",img)
    
    #Convert Gray Scale
    imgray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    #cv2.imshow("afterGrayScale",imgray)
    cv2.imwrite(str(path.absolute()) + "/afterGrayScale.jpg",imgray)
    
    #Binarize
    #0:black 255:white
    #cv2.THRESH_BINARY: if over threshold, redraw maxvalue. if under threshold redraw 0.
    #cv2.THRESH_BINARY_INV: if under threshold,redraw maxvalue. if over threshold redraw 0.
    #cv2.THRESH_TRUNC     : if over threshold,redraw by threshold. if under threshold,not redraw.
    #ret,thresh = cv2.threshold(imgray,128,255,cv2.THRESH_BINARY_INV)
    ret,thresh = cv2.threshold(imgray,210,255,cv2.THRESH_TRUNC)
    
    ret,thresh = cv2.threshold(imgray,100,255,cv2.THRESH_BINARY)
    
    #cv2.imshow("afterBinarized",thresh)
    cv2.imwrite(str(path.absolute()) + "/afterBinarized.jpg",thresh)
    
    contours, hierarchy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    afContours = []
    for i,contour in enumerate(contours):
        area = cv2.contourArea(contour)

        if area > 50000 and area < 2600000:
            print("result contourArea:" + str(area))
            afContours.append(contour)
            x,y,w,h = cv2.boundingRect(contour)
            cv2.imwrite(str(path.absolute()) + "/trackimg/croppedImg" + str(i) + ".jpg", thresh[y:y+h,x:x+w])
            
    afterContoursWrite = cv2.drawContours(img, afContours, -1, (0,255,0), 1)
    #cv2.imshow("afterContoursWrite",afterContoursWrite)
    cv2.imwrite(str(path.absolute()) + "/afterContours.jpg",afterContoursWrite)
    
    k = cv2.waitKey(0)
    if k == ord('s'): # wait for 's' key to save and exit
        cv2.imwrite(target.stem + "_DrawedContours" + target.suffix, afterContoursWrite)
        
    cv2.destroyAllWindows()
    
#argv[1]: target directory
#argv[2]: target file
path = Path(sys.argv[1])
if path.is_dir():
    target = Path(str(path.absolute()) + "/" + sys.argv[2])
    if target.is_file():
        execScan(path, target)
