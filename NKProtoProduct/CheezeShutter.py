#! python3
# -*- coding:utf-8
import cv2
import time
import sys
from pathlib import Path
from datetime import datetime,timedelta,timezone

class CheezeShutter():
    __waitSeconds = 1
    __captureNum = 1
    __cap = None
    __saveFileName = '/home/puppy/pic/Cheeze/shutter'
    __vidDeviceNum = 1
    __width = 780
    __height =  780
    __autoCapMode = False
    __autoCapClockSeconds = 5
    
    def __init__(self):
        #if len(sys.argv) > 1:
        #    conf = Path(sys.argv[3])
        #    if conf.is_file and conf.name() == 'cheezeShutter.conf':
        #        pass
        if len(sys.argv) > 1:
            self.__autoCapMode = bool(int(sys.argv[1]))
        
        self.__cap = cv2.VideoCapture(self.__vidDeviceNum)
        self.__cap.set(cv2.CAP_PROP_FPS,30)
        self.__cap.set(cv2.CAP_PROP_FRAME_WIDTH,self.__width)
        self.__cap.set(cv2.CAP_PROP_FRAME_HEIGHT,self.__height)
        
    def shutter(self):
        startTime = datetime.now()
        print(startTime)
        try:
            while True:
                ret,frame = self.__cap.read()
                cv2.imshow('preview',frame)
                
                if(self.__autoCapMode == True):
                    if (datetime.now() - startTime) >= timedelta(seconds=self.__autoCapClockSeconds):
                        self.__saveFile(frame)
                        startTime = datetime.now()
                        print(startTime)
                
                wKey = cv2.waitKey(1)
                if wKey & 0xff == ord('w'):
                    self.__saveFile(frame)
                    time.sleep(self.__waitSeconds)
                elif wKey & 0xff == ord('q'):
                    break
                
        except Exception as ex:
            print(ex)
        finally:
            self.__cap.release()
            sys.exit(0)
            
    def __saveFile(self,frame):
        saveName = self.__saveFileName
        picNum = 0
        while True:
            if Path(saveName + str(picNum) + '.png').exists():
                picNum += 1
            else:
                break
                
        cv2.imwrite(saveName + str(picNum) + '.png',frame, (self.__width,self.__height))

if __name__ == '__main__':
    chs = CheezeShutter()
    chs.shutter()
