#! python3
# -*- coding:utf-8 -*-

import cv2
import sys, traceback
import numpy as np
import matplotlib.pyplot as plt

def adjustImShow(wname,img,height,width):
    cv2.namedWindow(wname, cv2.WINDOW_NORMAL)
    cv2.resizeWindow(wname,height,width)
    cv2.imshow(wname,img)
    
def chkDilationAndErode(imgName, minArea,iterations=5):
    try:
        img = cv2.imread(imgName,cv2.IMREAD_COLOR)
        
        if img is None:
            print("no file reading...")
            sys.exit(1)
            

        adjustImShow("original",img,800,800)
        
        
        kernel = np.ones((3,3))
        
        #ups
        up = np.array(img)
        up = cv2.dilate(up,kernel,iterations=iterations)
        adjustImShow("up" + str(iterations),up,800,800)
        ret, upDst = cv2.threshold(cv2.cvtColor(up,cv2.COLOR_BGR2GRAY), 128, 255, cv2.THRESH_BINARY)
        adjustImShow("upDst" + str(iterations),upDst,800,800)
        
        #downs
        down = np.array(img)
        down = cv2.erode(down,kernel,iterations=iterations)
        adjustImShow("down" + str(iterations),down,800,800)
        ret, downDst = cv2.threshold(cv2.cvtColor(down,cv2.COLOR_BGR2GRAY), 128, 255, cv2.THRESH_BINARY)
        adjustImShow("downDst" + str(iterations),downDst,800,800)
            
        cv2.waitKey(0)
        cv2.destroyAllWindows()
            
    except Exception as ex:
        print("Error:", sys.exc_info()[0])
        print(sys.exc_info()[1])

def danbole1(imgName, minArea, frHue, toHue):
    try:
        img = cv2.imread(imgName,cv2.IMREAD_COLOR)
        
        if img is None:
            print("no file reading...")
            sys.exit(1)
            
        #conv bgr to hsv
        hsv = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
        hsv = cv2.medianBlur(hsv,33)
        adjustImShow("hsv blur",hsv,800,800)
        
        hue,Saturation,Value = cv2.split(hsv)
        
        # binary transformation (only use H channnel)
        fHue = cv2.inRange(hue, frHue, toHue)
        adjustImShow("hue filter",fHue,800,800)
        
        dst = fHue
        adjustImShow("dst",dst,800,800)
        
        contours, hierarcy =  cv2.findContours(dst,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
        
        for contour in contours:
            if cv2.contourArea(contour) > int(minArea):
                print("contour size: " + str(cv2.contourArea(contour)))
                x,y,w,h = cv2.boundingRect(contour)
                cv2.rectangle(img,(x,y), (x+w,y+h), (0,255,0),5)
            
        adjustImShow("result",img,800,800)
        
        cv2.waitKey(0)
        cv2.destroyAllWindows()
        
        cv2.imwrite(imgName + "result.jpg",img)
        
    except Exception as ex:
        print("Error:", sys.exc_info()[0])
        print(sys.exc_info()[1])

def danbole3(imgName, minArea, frHue, toHue, frSa, toSa, frVal, toVal, targetImg=None):
    try:
        img = cv2.imread(imgName,cv2.IMREAD_COLOR)
        if targetImg is not None:
            img = targetImg
        
        if img is None and targetImg is None:
            print("no file reading...")
            sys.exit(1)
            
        #kernel for dilate
        valKernel = np.ones((3,3), dtype=np.uint8)
        
        #conv bgr to hsv
        hsv = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
        hsv = cv2.GaussianBlur(hsv, (13, 13), 5)
        #hsv = cv2.dilate(hsv, valKernel, iterations=10)
        adjustImShow("hsv blur",hsv,800,800)
        
        hue,Saturation,Value = cv2.split(hsv)
        
        # binary transformation (only use H channnel)
        fHue = cv2.inRange(hue, frHue, toHue)
        adjustImShow("hue filter",fHue,800,800)
        
        fSa = cv2.inRange(Saturation, frSa, toSa)
        adjustImShow("satulation filter",fSa,800,800)
        
        #strong shadow
        Value = cv2.erode(Value, valKernel, iterations=20)
        fV = cv2.inRange(Value, frVal, toVal)
        #ret, fV = cv2.threshold(Value, frVal, 255, cv2.THRESH_BINARY)
        adjustImShow("Value filter",fV,800,800)
        
        dst1 = cv2.bitwise_and(fHue,fSa)
        dst2 = cv2.bitwise_and(fHue,fV)
        dst = cv2.bitwise_and(dst1,dst2)
        adjustImShow("dst",dst,800,800)
        
        contours, hierarcy =  cv2.findContours(dst,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
        
        for contour in contours:
            if cv2.contourArea(contour) > int(minArea):
                print("contour size: " + str(cv2.contourArea(contour)))
                x,y,w,h = cv2.boundingRect(contour)
                cv2.rectangle(img,(x,y), (x+w,y+h), (0,255,0),5)
            
        adjustImShow("result",img,800,800)
        
        cv2.waitKey(0)
        cv2.destroyAllWindows()
        
        cv2.imwrite(imgName + "result.jpg",img)
        
    except Exception as ex:
        print("Error:", sys.exc_info()[0])
        print(sys.exc_info()[1])

def drawGrids(imgPath, gridRowNum, gridColNum, frRect, toRect):
    #read
    img = cv2.imread(imgPath, cv2.IMREAD_COLOR)
    
    #clip image in range
    rangeImg = np.copy(img[ frRect[1]:toRect[1], frRect[0]:toRect[0]])
    
    #draw range
    cv2.rectangle(img, frRect, toRect, (0,255,255), 4)
    
    #draw grid in range
    rowHight = (toRect[1] - frRect[1]) / gridRowNum 
    colWidth = (toRect[0] - frRect[0]) / gridColNum 
    for y in range(gridRowNum):
        h = int(rowHight * (y+1) + frRect[1])
        cv2.line(img, (frRect[0],h), (toRect[0],h) ,(0,255,0), 4)
        
    for x in range(gridColNum):
        w = int(colWidth * (x+1) + frRect[0])
        cv2.line(img, (w,frRect[1]), (w,toRect[1]) ,(0,255,0), 4)
    
    #preview
    adjustImShow("img",img, 800,800)
    adjustImShow("rangeImg",rangeImg, 800,800)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    
    return rangeImg
    

#my room's danbole
#danbole1(sys.argv[1],10000)
#chkDilationAndErode(sys.argv[1],2000,100)
danbole3(sys.argv[1],sys.argv[2], 10,50, 20,160, 31,153)

#okiko danbole
#zooming2
#danbole3(sys.argv[1],sys.argv[2], 7,81, 2,47, 160,234)
#zooming3,4
#danbole3(sys.argv[1],sys.argv[2], 33,39, 12,14, 217,219)
#zooming5
#danbole3(sys.argv[1],sys.argv[2], 172,191, 87,136, 208,224)

#IMG_20200608_104100
#danbole1(sys.argv[1],0, 172,191)
#danbole3(sys.argv[1],sys.argv[2], 20,55, 20,150, 45,160)
#ret = drawGrids(sys.argv[1], 5,4, (100,520), (3724,2178))
ret = drawGrids(sys.argv[1], 5,4, (572,43), (2052,2122))
danbole3("",sys.argv[2], 10,50, 20,160, 31,153,ret)

#IMG_20200608_104100
#danbole1(sys.argv[1],0, 87,94)
#danbole3(sys.argv[1],sys.argv[2], 87,94, 87,125, 97,104)


#clip
#danbole001
#ret = drawGrids(sys.argv[1], 5,4, (486,1115), (2200,2780))
#danbole002
#ret = drawGrids(sys.argv[1], 5,4, (100,520), (3724,2178))
#IMG_20200608_104106
#ret = drawGrids(sys.argv[1], 5,4, (572,43), (2052,2122))