#! python3
# -*- coding:utf-8
import cv2
import time
import sys
from pathlib import Path
from datetime import datetime,timedelta
from RPi import GPIO

class CheezeShutter():
    __waitSeconds = 1
    __captureNum = 1
    __cap = None
    __vidDeviceNum = 0
    __width = 1024
    __height = 768
    __autoCapMode = True
    __autoCapClockSeconds = 5
    
    def __init__(self):
        if len(sys.argv) > 1:
            conf = Path(sys.argv[1])
            if conf.is_file and conf.name() == 'cheezeShutter.conf':
                pass
                    
        self.__cap = cv2.VideoCapture(self.__vidDeviceNum)
        self.__cap.set(3,self.__width)
        self.__cap.set(4,self.__height)        
        
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(4,GPIO.OUT)
        
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
        GPIO.output(4,GPIO.HIGH)
        saveName = './Cheeze/shutter'
        picNum = 0
        while True:
            if Path(saveName + str(picNum) + '.png').exists():
                picNum += 1
            else:
                break                
        cv2.imwrite(saveName + str(picNum) + '.png',frame)
        GPIO.output(4,GPIO.LOW)

if __name__ == '__main__':
    chs = CheezeShutter()
    chs.shutter()
