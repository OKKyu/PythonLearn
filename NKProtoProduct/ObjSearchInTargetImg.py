#! python3
# -*- coding:utf-8 -*-

import numpy as np
import cv2
import sys
from pathlib import Path

target = Path(sys.argv[1])
if target.is_file():
    img = cv2.imread(str(target))
    cv2.imshow("beforeContours",img)
    cv2.waitKeyEx(0)
    
    imgray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    #0:black 255:white
    #mode0: if over threshold, redraw maxvalue.
    #mode1: if under threshold,redraw maxvalue.
    ret,thresh = cv2.threshold(imgray,120,255,3)
    #cv2.line(thresh,(0,0),(350,350),255,20)
    cv2.imshow("afterBinarized",thresh)
    cv2.waitKeyEx(0)
    
    contours, hierarchy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    afterContours = cv2.drawContours(img, contours, -1, (0,255,0), 5)
    cv2.imshow("afterContours",afterContours)
    
    k = cv2.waitKey(0)
    if k == ord('s'): # wait for 's' key to save and exit
        cv2.imwrite(target.stem + "_DrawedContours" + target.suffix, afterContours)
        
    cv2.destroyAllWindows()