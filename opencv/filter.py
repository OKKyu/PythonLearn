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
        adjustImShow("3x3", dst,1000,1000)
        
        dst = cv2.blur(img, (6,6))
        adjustImShow("6x6",dst,1000,1000)

        dst = cv2.blur(img, (20,20))
        adjustImShow("20x20",dst,1000,1000)
        
        dst = cv2.blur(img, (2,100))
        adjustImShow("2x100",dst,1000,1000)
        
        dst = cv2.blur(img, (100,100))
        adjustImShow("100x100",dst,1000,1000)
        
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
        
        adjustImShow("original",img,800,800)
        
        #blur
        #2nd args needs odd value.
        dst = cv2.medianBlur(img,11)
        adjustImShow("11",dst,800,800)
        
        dst = cv2.medianBlur(img,33)
        adjustImShow("33",dst,800,800)
        
        dst = cv2.medianBlur(img,99)
        adjustImShow("99",dst,800,800)        
        
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
        
        adjustImShow("original",img,800,800)
        
        #gaussian
        dst = cv2.GaussianBlur(img, (13,13), 10, 10)
        adjustImShow("result",dst,800,800)
        
        dst = cv2.GaussianBlur(img, (13,13), 52, 8)
        adjustImShow("result2",dst,800,800)
        
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
        
        adjustImShow("original",img,800,800)
        
        dst = cv2.Laplacian(img,-1)
        adjustImShow("result",dst,800,800)
        
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
        
        adjustImShow("original",img,800,800)
        
        dst = cv2.Sobel(img,-1,0,1)
        adjustImShow("result",dst,800,800)
        
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
        
        adjustImShow("original",img,800,800)
        
        dst = cv2.Canny(img, 40.0, 200.0)
        adjustImShow("result",dst,800,800)
        
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
        
        adjustImShow("original", img, 800, 800)
        
        #minimize, after revert original size.
        dst = cv2.resize(img, (int(img.shape[1] * 0.2), int(img.shape[0] * 0.2)), interpolation=cv2.INTER_NEAREST )
        dst = cv2.resize(dst, (int(img.shape[1]), int(img.shape[0])), interpolation=cv2.INTER_NEAREST )
        adjustImShow("mozaic", dst, 800, 800)
        
        cv2.waitKey(0)
        cv2.destroyAllWindows()
        
    except Exception as ex:
        print("Error:", sys.exc_info()[0])
        print(sys.exc_info()[1])
        print(traceback.format_tb(sys.exc_info()[2]))
    finally:
        pass
    
def custom(imgName):
    #this code refered below site.
    #https://symfoware.blog.fc2.com/blog-entry-2126.html
    try:
        img = cv2.imread(imgName,cv2.IMREAD_COLOR)
        
        if img is None:
            print("no file reading...")
            sys.exit(1)
        
        adjustImShow("original", img,800,800)
        
        kernel = np.array([ [0,0,0],
                            [0,2,0],
                            [0,0,0]],dtype=np.float32)
        ddepth = -1
        
        dst = cv2.filter2D(img, ddepth, kernel)
        adjustImShow("custom", dst, 800, 800)
        
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

#reverse
#colorReverse(sys.argv[1])

#blur
#blur(sys.argv[1])
#medianBlur(sys.argv[1])
#gaus(sys.argv[1])

#edge detection
#laplacian(sys.argv[1])
#sobel(sys.argv[1])
#canny(sys.argv[1])

#expantion
#dilate(sys.argv[1])
#shulink
#erode(sys.argv[1])

#other
#equalize
#boxfilter(sys.argv[1])
mozaic(sys.argv[1])
#custom(sys.argv[1])
