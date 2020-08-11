#! python3
# -*- coding:utf-8 -*-

import cv2
import sys, traceback
import numpy as np
import matplotlib.pyplot as plt

def findContours(imgName, drawMode, minArea):
    try:
        img = cv2.imread(imgName,cv2.IMREAD_COLOR)
        
        if img is None:
            print("no file reading...")
            sys.exit(1)
            
        dst = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
        adjustImShow("to gray",dst,800,800)
        
        ret, dst = cv2.threshold(dst, 50, 255, cv2.THRESH_BINARY)
        adjustImShow("threshold 1",dst,800,800)
              
        
        contours, hierarcy =  cv2.findContours(dst,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
        
        if drawMode == 1:
            afContours = []
            for contour in contours:
                if cv2.contourArea(contour) > int(minArea):
                    print("contour size: " + str(cv2.contourArea(contour)))
                    afContours.append(contour)
            img = cv2.drawContours(img,afContours, -1, (0,255,0), 1)
        else:
            for contour in contours:
                if cv2.contourArea(contour) > int(minArea):
                    print("contour size: " + str(cv2.contourArea(contour)))
                    x,y,w,h = cv2.boundingRect(contour)
                    cv2.rectangle(img,(x,y), (x+w,y+h), (0,255,0),5)
            
        adjustImShow("result",img,800,800)
        
        cv2.waitKey(0)
        cv2.destroyAllWindows()
        
    except Exception as ex:
        print("Error:", sys.exc_info()[0])
        print(sys.exc_info()[1])

def findContoursAdaptive(imgName, drawMode, minArea):
    try:
        img = cv2.imread(imgName,cv2.IMREAD_COLOR)
        
        if img is None:
            print("no file reading...")
            sys.exit(1)
            
        gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
        adjustImShow("gray",gray,800,800)
        
        dst = cv2.adaptiveThreshold(gray,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,3,3)
        adjustImShow("dst",dst,800,800)
        
        contours, hierarcy =  cv2.findContours(dst,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
        
        if drawMode == 1:
            afContours = []
            for contour in contours:
                if cv2.contourArea(contour) > int(minArea):
                    print("contour size: " + str(cv2.contourArea(contour)))
                    afContours.append(contour)
            img = cv2.drawContours(img,afContours, -1, (0,255,0), 1)
        else:
            for contour in contours:
                if cv2.contourArea(contour) > int(minArea):
                    print("contour size: " + str(cv2.contourArea(contour)))
                    x,y,w,h = cv2.boundingRect(contour)
                    cv2.rectangle(img,(x,y), (x+w,y+h), (0,255,0),5)
            
        adjustImShow("result",img,800,800)
        
        cv2.waitKey(0)
        cv2.destroyAllWindows()
        
    except Exception as ex:
        print("Error:", sys.exc_info()[0])
        print(sys.exc_info()[1])

def findContoursInRange(imgName, drawMode, minArea):
    try:
        img = cv2.imread(imgName,cv2.IMREAD_COLOR)
        
        if img is None:
            print("no file reading...")
            sys.exit(1)
            
        dst = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
        adjustImShow("to gray",dst,800,800)
        
        
        dst2 = cv2.inRange(dst,0,40)
        adjustImShow("in range row",dst2,800,800)
        
        dst3 = cv2.inRange(dst,210,240)
        adjustImShow("in range high",dst3,800,800)
        
        mix = cv2.bitwise_or(dst2,dst3)
        adjustImShow("mix",mix,800,800)
        cv2.imwrite("mix.png",mix)
        
        ret, dst = cv2.threshold(dst, 50, 255, cv2.THRESH_BINARY)
        adjustImShow("threshold 1",dst,800,800)
        
        contours, hierarcy =  cv2.findContours(dst,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
        
        if drawMode == 1:
            afContours = []
            for contour in contours:
                if cv2.contourArea(contour) > int(minArea):
                    print("contour size: " + str(cv2.contourArea(contour)))
                    afContours.append(contour)
            img = cv2.drawContours(img,afContours, -1, (0,255,0), 1)
        else:
            for contour in contours:
                if cv2.contourArea(contour) > int(minArea):
                    print("contour size: " + str(cv2.contourArea(contour)))
                    x,y,w,h = cv2.boundingRect(contour)
                    cv2.rectangle(img,(x,y), (x+w,y+h), (0,255,0),5)
            
        adjustImShow("result",img,800,800)
        
        cv2.waitKey(0)
        cv2.destroyAllWindows()
        
    except Exception as ex:
        print("Error:", sys.exc_info()[0])
        print(sys.exc_info()[1])

def findContoursHue(imgName, drawMode, minArea, frHue, toHue):
    try:
        img = cv2.imread(imgName,cv2.IMREAD_COLOR)
        
        if img is None:
            print("no file reading...")
            sys.exit(1)
            
        #conv bgr to hsv
        hsv = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
        hsv = cv2.GaussianBlur(hsv, (5, 5), 3)
        
        hue,Saturation,Value = cv2.split(hsv)
        
        # binary transformation (only use H channnel)
        _ret, img_H1 = cv2.threshold(hue, frHue / 360 * 179, 255, cv2.THRESH_BINARY_INV)
        _ret, img_H2 = cv2.threshold(hue, toHue / 360 * 179, 255, cv2.THRESH_BINARY_INV)
        dst = 255 - (img_H2 - img_H1)
        adjustImShow("dst",dst,800,800)
        
        dst = cv2.bitwise_not(dst)
        adjustImShow("dst",dst,800,800)
        
        contours, hierarcy =  cv2.findContours(dst,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
        
        if drawMode == 1:
            afContours = []
            for contour in contours:
                if cv2.contourArea(contour) > int(minArea):
                    print("contour size: " + str(cv2.contourArea(contour)))
                    afContours.append(contour)
            img = cv2.drawContours(img,afContours, -1, (0,255,0), 1)
        else:
            for contour in contours:
                if cv2.contourArea(contour) > int(minArea):
                    print("contour size: " + str(cv2.contourArea(contour)))
                    x,y,w,h = cv2.boundingRect(contour)
                    cv2.rectangle(img,(x,y), (x+w,y+h), (0,255,0),5)
            
        adjustImShow("result",img,800,800)
        
        cv2.waitKey(0)
        cv2.destroyAllWindows()
        
    except Exception as ex:
        print("Error:", sys.exc_info()[0])
        print(sys.exc_info()[1])

def findContoursHSV(imgName, drawMode, minArea, frHue, toHue, frSa, toSa, frVal, toVal):
    try:
        img = cv2.imread(imgName,cv2.IMREAD_COLOR)
        
        if img is None:
            print("no file reading...")
            sys.exit(1)
            
        #conv bgr to hsv
        hsv = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
        #hsv = cv2.GaussianBlur(hsv, (5, 5), 3)
        hsv = cv2.medianBlur(hsv,33)
        adjustImShow("hsv blur",hsv,800,800)
        
        hue,Saturation,Value = cv2.split(hsv)
        
        # binary transformation (only use H channnel)
        _ret, img_H1 = cv2.threshold(hue, frHue / 360 * 179, 255, cv2.THRESH_BINARY_INV)
        _ret, img_H2 = cv2.threshold(hue, toHue / 360 * 179, 255, cv2.THRESH_BINARY_INV)
        fHue = 255 - (img_H2 - img_H1)
        fHue = cv2.bitwise_not(fHue)
        adjustImShow("hue filter",fHue,800,800)
        
        _ret, img_S1 = cv2.threshold(Saturation, frSa , 255, cv2.THRESH_BINARY_INV)
        _ret, img_S2 = cv2.threshold(Saturation, toSa , 255, cv2.THRESH_BINARY_INV)
        fSa = 255 - (img_S2 - img_S1)
        fSa = cv2.bitwise_not(fSa)
        adjustImShow("satulation filter",fSa,800,800)
        
        _ret, img_V1 = cv2.threshold(Value, frVal , 255, cv2.THRESH_BINARY_INV)
        _ret, img_V2 = cv2.threshold(Value, toVal , 255, cv2.THRESH_BINARY_INV)
        fV = 255 - (img_V2 - img_V1)
        fV = cv2.bitwise_not(fV)
        adjustImShow("Value filter",fV,800,800)
        
        dst1 = cv2.bitwise_and(fHue,fSa)
        dst2 = cv2.bitwise_and(fHue,fV)
        dst = cv2.bitwise_and(dst1,dst2)
        adjustImShow("dst",dst,800,800)
        
        contours, hierarcy =  cv2.findContours(dst,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
        
        if drawMode == 1:
            afContours = []
            for contour in contours:
                if cv2.contourArea(contour) > int(minArea):
                    print("contour size: " + str(cv2.contourArea(contour)))
                    afContours.append(contour)
            img = cv2.drawContours(img,afContours, -1, (0,255,0), 1)
        else:
            for contour in contours:
                if cv2.contourArea(contour) > int(minArea):
                    print("contour size: " + str(cv2.contourArea(contour)))
                    x,y,w,h = cv2.boundingRect(contour)
                    cv2.rectangle(img,(x,y), (x+w,y+h), (0,255,0),5)
            
        adjustImShow("result",img,800,800)
        
        cv2.waitKey(0)
        cv2.destroyAllWindows()
        
    except Exception as ex:
        print("Error:", sys.exc_info()[0])
        print(sys.exc_info()[1])

def adjustImShow(wname,img,height,width):
    cv2.namedWindow(wname, cv2.WINDOW_NORMAL)
    cv2.resizeWindow(wname,height,width)
    cv2.imshow(wname,img)

#findContoursOrigin(sys.argv[1],sys.argv[2],sys.argv[3])

#gray scale
#findContoursGray(sys.argv[1],sys.argv[2],sys.argv[3])
#findContoursAdaptive(sys.argv[1],sys.argv[2],sys.argv[3])

#green 50 ~ 150
#findContoursHue(sys.argv[1],sys.argv[2],sys.argv[3],50,150)

#red 0 ~ 60, 300 ~ 360
#findContoursHue(sys.argv[1],sys.argv[2],sys.argv[3],0,60)
#findContoursHue(sys.argv[1],sys.argv[2],sys.argv[3],300,360)

#brown 20 ~ 50
#findContoursHue(sys.argv[1],sys.argv[2],sys.argv[3],30,70)

#findContoursHSV(sys.argv[1],sys.argv[2],sys.argv[3], 50,150, 0,250, 0,255)

