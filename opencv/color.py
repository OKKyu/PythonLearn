#! python3
# -*- coding:utf-8 -*-
# 『Pythonで始めるOpenCV4プログラミング』
#  北山尚洋
import sys, cv2, traceback
import matplotlib.pyplot as plt

def equalize(imgName):
    try:
        #equalizeHist with OpenCV2 is only grayscale.
        img = cv2.imread(imgName, cv2.IMREAD_GRAYSCALE)
        
        if img is None:
            print("no file reading...")
            sys.exit(1)
        
        cv2.imshow("before", img)
        
        dst = cv2.equalizeHist(img)
        cv2.imshow("after", dst)
        
        cv2.waitKey(0)
        cv2.destroyAllWindows()
    except Exception as ex:
        print("Error:", sys.exc_info()[0])
        print(sys.exc_info()[1])
        print(traceback.format_tb(sys.exc_info()[2]))
    finally:
        pass

def colorDivide(imgName):
    try:
        img = cv2.imread(imgName, cv2.IMREAD_COLOR)
        
        if img is None:
            print("no file reading...")
            sys.exit(1)
        
        cv2.imshow("before", img)
        
        bgr = cv2.split(img)
        
        #weak:0 blakc
        #strong:255 white
        blue = bgr[0]
        green = bgr[1]
        red = bgr[2]
        
        cv2.imshow("blue",blue)
        cv2.imshow("green",green)
        cv2.imshow("red",red)
        
        cv2.waitKey(0)
        cv2.destroyAllWindows()
        
        #histgram
        import matplotlib.pyplot as plt
        
        # 目盛りを変更
        xtickmem = [ i for i in range(0,255,10) ]
        
        plt.xlabel("color bit")
        plt.ylabel("num of pixel")
        plt.xticks(xtickmem)
        
        plt.hist([blue.flatten(), green.flatten(), red.flatten()], label=['blue','green','red'] \
                 , color=['blue','green','red'], bins=256, range=(0,255))
        plt.show()
    except Exception as ex:
        print("Error:", sys.exc_info()[0])
        print(sys.exc_info()[1])
        print(traceback.format_tb(sys.exc_info()[2]))
    finally:
        pass

#equalize(sys.argv[1])
#colorDivide(sys.argv[1])
