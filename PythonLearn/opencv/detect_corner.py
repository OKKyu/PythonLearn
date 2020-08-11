#! python3
# -*- coding:utf-8 -*-
import sys
import cv2
import numpy as np

def corners(imgName):
    try:
        MAX_CORNERS = 100000
        BLOCK_SIZE = 1000
        QUALITY_LEVEL = 0.15
        MIN_DISTANCE = 20.0
        
        img = cv2.imread(imgName,cv2.IMREAD_COLOR)
        
        if img is None:
            print("no file reading...")
            sys.exit(1)
            
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        gray = cv2.bitwise_not(gray)
        corners = cv2.goodFeaturesToTrack(gray, MAX_CORNERS, QUALITY_LEVEL, 
                                          MIN_DISTANCE, blockSize = BLOCK_SIZE, useHarrisDetector=False)
        
        for i in corners:
            x,y = i.ravel()
            cv2.circle(img, (x,y), 4, (255,0,0,), 2)
        
        adjustImShow("img",img,800,800)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
        
    except Exception as ex:
        print("Error:", sys.exc_info()[0])
        print(sys.exc_info()[1])
        print(traceback.format_tb(sys.exc_info()[2]))
    finally:
        pass

def adjustImShow(wname,img,height,width):
    cv2.namedWindow(wname, cv2.WINDOW_NORMAL)
    cv2.resizeWindow(wname,height,width)
    cv2.imshow(wname,img)

corners(sys.argv[1])