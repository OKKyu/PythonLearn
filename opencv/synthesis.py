#!python3
# -*- coding:utf-8 -*-
# 『Pythonで始めるOpenCV4プログラミング』
#  北山尚洋

import cv2
import sys, traceback
import numpy as np

def add(imgName1, imgName2):
    try:
        img1 = cv2.imread(imgName1)
        img2 = cv2.imread(imgName2)
        
        if img1 is None or img2 is None:
            print("no file reading...")
            sys.exit(1)
        
        #caution!
        #src file size have to same size each img1 and img2. and same type.
        img1 = cv2.resize(img1, (500,500))
        img2 = cv2.resize(img2, (500,500))
        
        cv2.imshow('image1', img1)
        cv2.imshow('image2', img2)
        
        dst = cv2.add(img1, img2)
        cv2.imshow('synthesize', dst)
        
        cv2.waitKey(0)
        cv2.destroyAllWindows()
        
    except Exception as ex:
        print("Error:", sys.exc_info()[0])
        print(sys.exc_info()[1])
        print(traceback.format_tb(sys.exc_info()[2]))
    finally:
        pass
    

def addScolor(imgName1):
    try:
        img1 = cv2.imread(imgName1)
        
        if img1 is None:
            print("no file reading...")
            sys.exit(1)
            
        cv2.imshow("img1",img1)
        
        height = img1.shape[0]
        width = img1.shape[1]
        blue = np.zeros((height, width, 3), np.uint8)
        blue[:,:] = [128, 0, 0]
        
        dst = cv2.add(img1, blue)
        cv2.imshow("after", dst)
        
        cv2.waitKey(0)
        cv2.destroyAllWindows()
        
    except Exception as ex:
        print("Error:", sys.exc_info()[0])
        print(sys.exc_info()[1])
        print(traceback.format_tb(sys.exc_info()[2]))
    finally:
        pass

def addMask(imgName1, imgName2):
    try:
        img1 = cv2.imread(imgName1)
        img2 = cv2.imread(imgName2)
        
        if img1 is None or img2 is None:
            print("no file reading...")
            sys.exit(1)
        
        #caution!
        #src file size have to same size each img1 and img2. and same type.
        img1 = cv2.resize(img1, (500,500))
        img2 = cv2.resize(img2, (500,500))
        
        cv2.imshow('image1', img1)
        cv2.imshow('image2', img2)
        
        #create mask
        height = img1.shape[0]
        width = img1.shape[1]
        img_mask = np.zeros((height, width), np.uint8)
        img_mask[ height//4:height*3//4, width//4:width*3//4 ] = [255]
        
        #add two image with mask.
        dst = cv2.add(img1, img2, mask = img_mask)
        cv2.imshow('dst1', dst)
        
        #add two image with mask.
        dst = cv2.add(img1, img2, mask = img_mask)
        cv2.imshow('dst1', dst)        
        
        cv2.waitKey(0)
        cv2.destroyAllWindows()
        
    except Exception as ex:
        print("Error:", sys.exc_info()[0])
        print(sys.exc_info()[1])
        print(traceback.format_tb(sys.exc_info()[2]))
    finally:
        pass

#add(sys.argv[1], sys.argv[2])
#addScolor(sys.argv[1])
addMask(sys.argv[1], sys.argv[2])