#! python3
# -*- coding:utf-8 -*-

import cv2
import os, sys, traceback
import numpy as np
import matplotlib.pyplot as plt

def rangeHSV_FrTo(imgPath,imgName,plot=False):
    img = cv2.imread(imgPath + os.sep +imgName, cv2.IMREAD_COLOR)
    img = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
    hue,satur,val = cv2.split(img)
    
    stdHue = __getFrTo(hue,plot)
    stdSatur = __getFrTo(satur,plot)
    stdval = __getFrTo(val,plot)
        
    return stdHue, stdSatur, stdval

def __getFrTo(img,plot=False):
    flatt = img.flatten()
    if plot == True:
        plt.hist(flatt, bins=255)
        plt.show()
    
    avg = np.average(img)
    std = np.std(img)
    stdFr = avg - (std)
    stdTo = avg + (std)
    print(avg)
    print(std)
    stdRange = [ i for i in flatt if i >= stdFr and i <= stdTo]
    
    if plot == True:
        plt.hist(stdRange, bins=255)
        plt.show()
        
    return [np.min(stdFr), np.max(stdTo)]



imgPath = sys.argv[1]
imgName = sys.argv[2]

hue, satur, val = rangeHSV_FrTo(imgPath, imgName, True)
print("hue range " + str(hue))
print("saturation range " + str(satur))
print("val range " + str(val))
