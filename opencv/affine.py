#! python3
# -*- coding:utf-8 -*-
# 『Pythonで始めるOpenCV4プログラミング』
#  北山尚洋

import cv2
import sys, traceback

def flip(imgName):
    try:
        img = cv2.imread(imgName)
        
        if img is None:
            print("no file reading...")
            sys.exit(1)
        
        cv2.imshow('original', img)
        
        #up-down reverse
        dst = cv2.flip(img,0)
        cv2.imshow('flip0', dst)
        
        #left-right reverse
        dst = cv2.flip(img,1)
        cv2.imshow('flip1', dst)
        
        #up-down and left-right both reverse
        dst = cv2.flip(img,-1)
        cv2.imshow('flip-1', dst)
        
        cv2.waitKey(0)
        cv2.destroyAllWindows()
    except Exception as ex:
        print("Error:", sys.exc_info()[0])
        print(sys.exc_info()[1])
        print(traceback.format_tb(sys.exc_info()[2]))
    finally:
        pass
        
def resize(imgName):
    try:
        img = cv2.imread(imgName)
        
        if img is None:
            print("no file reading...")
            sys.exit(1)
        
        cv2.imshow('original', img)
        
        #resizing....
        # take care of relasion between shape and 2nd args tuple.
        #  shape[1] = col (width) , tuple[0] = width
        #  shape[0] = row (height) , tuple[1] = height
        
        #50% shurink
        dst = cv2.resize(img, (int(img.shape[1] * 0.5), int(img.shape[0] * 0.5)))
        cv2.imshow('0.5%', dst)
        
        #200% growth
        dst = cv2.resize(img, (int(img.shape[1] * 2), int(img.shape[0] * 2)))
        cv2.imshow('2.0%', dst)
        
        #width 300% , height 20%
        dst = cv2.resize(img, (int(img.shape[1] * 3), int(img.shape[0] * 0.2)))
        cv2.imshow('w3.0% h0.2%', dst)
        
        cv2.waitKey(0)
        cv2.destroyAllWindows()
    except Exception as ex:
        print("Error:", sys.exc_info()[0])
        print(sys.exc_info()[1])
        print(traceback.format_tb(sys.exc_info()[2]))
    finally:
        pass

def rotate(imgName):
    try:
        img = cv2.imread(imgName)
        
        if img is None:
            print("no file reading...")
            sys.exit(1)
        
        cv2.imshow('original', img)
        
        height = img.shape[0]
        width = img.shape[1]
        center = (int(width / 2), int(height / 2))
                
        #get setting
        # center 回転原点
        # 33.0   回転角度
        # 1.0    スケーリング？
        affin_trans = cv2.getRotationMatrix2D(center, 33.0, 1.0)
        
        #Rorring
        dst = cv2.warpAffine(img, affin_trans, (width, height))
        cv2.imshow("result:", dst)
        
        cv2.waitKey(0)
        cv2.destroyAllWindows()
    except Exception as ex:
        print("Error:", sys.exc_info()[0])
        print(sys.exc_info()[1])
        print(traceback.format_tb(sys.exc_info()[2]))
    finally:
        pass

def trimming(imgName):
    try:
        img = cv2.imread(imgName)
        
        if img is None:
            print("no file reading...")
            sys.exit(1)
        
        cv2.imshow('original', img)
        
        height = img.shape[0]
        width = img.shape[1]
        
        #splice
        dst = img[140:height, 80:width]
                        
        #display
        cv2.imshow("result:", dst)
        
        cv2.waitKey(0)
        cv2.destroyAllWindows()
    except Exception as ex:
        print("Error:", sys.exc_info()[0])
        print(sys.exc_info()[1])
        print(traceback.format_tb(sys.exc_info()[2]))
    finally:
        pass

#flip(sys.argv[1])
#resize(sys.argv[1])
#rotate(sys.argv[1])
trimming(sys.argv[1])