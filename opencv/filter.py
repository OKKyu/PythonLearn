#! python3
# -*- coding:utf-8 -*-

import cv2
import sys, traceback
import numpy as np

def colorReverse(imgName):
    try:
        img = cv2.imread(imgName,cv2.IMREAD_COLOR)
        
        if img is None:
            print("no file reading...")
            sys.exit(1)
                
        #reverse
        dst = cv2.bitwise_not(img)
        cv2.imshow("not",dst)
        
        #dst = cv2.bitwise_and(img,img)
        #cv2.imshow("and",dst)
        
        #dst = cv2.bitwise_or(img,img)
        #cv2.imshow("or",dst)
        
        #dst = cv2.bitwise_xor(img,img)
        #cv2.imshow("xor",dst)        
        
        cv2.waitKey(0)
        cv2.destroyAllWindows()
        
    except Exception as ex:
        print("Error:", sys.exc_info()[0])
        print(sys.exc_info()[1])
        print(traceback.format_tb(sys.exc_info()[2]))
    finally:
        pass

#bokashi 
def blur(imgName):
    try:
        img = cv2.imread(imgName,cv2.IMREAD_COLOR)
        
        if img is None:
            print("no file reading...")
            sys.exit(1)
        
        cv2.imshow("original", img)
        
        #blur
        #2nd args is kernel size (x,y).
        dst = cv2.blur(img, (3,3))
        cv2.imshow("3x3",dst)
        
        dst = cv2.blur(img, (6,6))
        cv2.imshow("6x6",dst)

        dst = cv2.blur(img, (20,20))
        cv2.imshow("20x20",dst)
        
        dst = cv2.blur(img, (2,100))
        cv2.imshow("2x100",dst)
        
        dst = cv2.blur(img, (100,100))
        cv2.imshow("100x100",dst)         
        
        cv2.waitKey(0)
        cv2.destroyAllWindows()
        
    except Exception as ex:
        print("Error:", sys.exc_info()[0])
        print(sys.exc_info()[1])
        print(traceback.format_tb(sys.exc_info()[2]))
    finally:
        pass

#bokashi 
def medianBlur(imgName):
    try:
        img = cv2.imread(imgName,cv2.IMREAD_COLOR)
        
        if img is None:
            print("no file reading...")
            sys.exit(1)
        
        cv2.imshow("original", img)
        
        #blur
        #2nd args needs odd value.
        dst = cv2.medianBlur(img,11)
        cv2.imshow("11",dst)
        
        dst = cv2.medianBlur(img,33)
        cv2.imshow("33",dst)
        
        cv2.waitKey(0)
        cv2.destroyAllWindows()
        
    except Exception as ex:
        print("Error:", sys.exc_info()[0])
        print(sys.exc_info()[1])
        print(traceback.format_tb(sys.exc_info()[2]))
    finally:
        pass

#bokashi 
def gaus(imgName):
    try:
        img = cv2.imread(imgName,cv2.IMREAD_COLOR)
        
        if img is None:
            print("no file reading...")
            sys.exit(1)
        
        cv2.imshow("original", img)
        
        #gaussian
        dst = cv2.GaussianBlur(img, (13,13), 10, 10)
        cv2.imshow("result",dst)
        
        dst = cv2.GaussianBlur(img, (13,13), 52, 8)
        cv2.imshow("result2",dst)        
        
        cv2.waitKey(0)
        cv2.destroyAllWindows()
        
    except Exception as ex:
        print("Error:", sys.exc_info()[0])
        print(sys.exc_info()[1])
        print(traceback.format_tb(sys.exc_info()[2]))
    finally:
        pass

#edge detection
def laplacian(imgName):
    try:
        img = cv2.imread(imgName,cv2.IMREAD_COLOR)
        
        if img is None:
            print("no file reading...")
            sys.exit(1)
        
        cv2.imshow("original", img)
        
        dst = cv2.Laplacian(img,-1)
        cv2.imshow("result",dst)
        
        cv2.waitKey(0)
        cv2.destroyAllWindows()
        
    except Exception as ex:
        print("Error:", sys.exc_info()[0])
        print(sys.exc_info()[1])
        print(traceback.format_tb(sys.exc_info()[2]))
    finally:
        pass

#edge detection
def sobel(imgName):
    try:
        img = cv2.imread(imgName,cv2.IMREAD_COLOR)
        
        if img is None:
            print("no file reading...")
            sys.exit(1)
        
        cv2.imshow("original", img)
        
        dst = cv2.Sobel(img,-1,0,1)
        cv2.imshow("result",dst)
        
        cv2.waitKey(0)
        cv2.destroyAllWindows()
        
    except Exception as ex:
        print("Error:", sys.exc_info()[0])
        print(sys.exc_info()[1])
        print(traceback.format_tb(sys.exc_info()[2]))
    finally:
        pass

#edge detection
def canny(imgName):
    try:
        img = cv2.imread(imgName,cv2.IMREAD_COLOR)
        
        if img is None:
            print("no file reading...")
            sys.exit(1)
        
        cv2.imshow("original", img, cv2.WINDOW_NORMAL)
        cv2.resizeWindow("original",600,600)
        
        dst = cv2.Canny(img, 40.0, 200.0)
        cv2.imshow("result",dst)
        cv2.resizeWindow("result",600,600)
        
        cv2.waitKey(0)
        cv2.destroyAllWindows()
        
    except Exception as ex:
        print("Error:", sys.exc_info()[0])
        print(sys.exc_info()[1])
        print(traceback.format_tb(sys.exc_info()[2]))
    finally:
        pass


def dilate(imgName):
    try:
        img = cv2.imread(imgName,cv2.IMREAD_COLOR)
        
        if img is None:
            print("no file reading...")
            sys.exit(1)
        
        cv2.imshow("original", img)
        
        kernel = np.ones((3,3), np.uint8)
        dst = cv2.dilate(img, kernel, iterations=1)
        cv2.imshow("dilate",dst)
        
        cv2.waitKey(0)
        cv2.destroyAllWindows()
        
    except Exception as ex:
        print("Error:", sys.exc_info()[0])
        print(sys.exc_info()[1])
        print(traceback.format_tb(sys.exc_info()[2]))
    finally:
        pass

def erode(imgName):
    try:
        img = cv2.imread(imgName,cv2.IMREAD_COLOR)
        
        if img is None:
            print("no file reading...")
            sys.exit(1)
        
        cv2.imshow("original", img)
        
        kernel = np.ones((3,3), np.uint8)
        dst = cv2.erode(img, kernel, iterations=1)
        cv2.imshow("erode",dst)
        
        cv2.waitKey(0)
        cv2.destroyAllWindows()
        
    except Exception as ex:
        print("Error:", sys.exc_info()[0])
        print(sys.exc_info()[1])
        print(traceback.format_tb(sys.exc_info()[2]))
    finally:
        pass

def boxfilter(imgName):
    try:
        img = cv2.imread(imgName,cv2.IMREAD_COLOR)
        
        if img is None:
            print("no file reading...")
            sys.exit(1)
        
        cv2.imshow("original", img)
        
        dst = cv2.boxFilter(img,-1,(9,9))
        cv2.imshow("box",dst)
        
        cv2.waitKey(0)
        cv2.destroyAllWindows()
        
    except Exception as ex:
        print("Error:", sys.exc_info()[0])
        print(sys.exc_info()[1])
        print(traceback.format_tb(sys.exc_info()[2]))
    finally:
        pass

def mozaic(imgName):
    try:
        img = cv2.imread(imgName,cv2.IMREAD_COLOR)
        
        if img is None:
            print("no file reading...")
            sys.exit(1)
        
        cv2.imshow("original", img)
        
        #minimize, after revert original size.
        dst = cv2.resize(img, (int(img.shape[1] * 0.2), int(img.shape[0] * 0.2)), interpolation=cv2.INTER_NEAREST )
        dst = cv2.resize(dst, (int(img.shape[1]), int(img.shape[0])), interpolation=cv2.INTER_NEAREST )
        cv2.imshow("mozaic",dst)
        
        cv2.waitKey(0)
        cv2.destroyAllWindows()
        
    except Exception as ex:
        print("Error:", sys.exc_info()[0])
        print(sys.exc_info()[1])
        print(traceback.format_tb(sys.exc_info()[2]))
    finally:
        pass

#reverse
#colorReverse(sys.argv[1])

#blur
#blur(sys.argv[1])
#medianBlur(sys.argv[1])
#gaus(sys.argv[1])

#edge detection
#laplacian(sys.argv[1])
#sobel(sys.argv[1])
canny(sys.argv[1])

#expantion
#dilate(sys.argv[1])
#shulink
#erode(sys.argv[1])

#equalize
#boxfilter(sys.argv[1])

#mozaic(sys.argv[1])