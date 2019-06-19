#! python3
# -*- coding:utf-8 -*-
import cv2
import numpy as np

#open video
cap = cv2.VideoCapture(0)

# Define the codec and create VideoWriter object
# FourCC は動画のコーデックを指定するための4バイトのコードで、使用可能なコードのリストは fourcc.org で確認できる．OS依存なので気を付けて選ぶこと．
fourcc = cv2.VideoWriter_fourcc(*'MJPG')
# filename,FourCC codec, framerate,width $ height
out = cv2.VideoWriter('output.avi',fourcc, 20.0, (640,480))

while True:
    ret ,frame = cap.read()
    
    if ret==True:
        #
        #frame = cv2.flip(frame,0)

        # write the flipped frame
        out.write(frame)    
        cv2.imshow('frame',frame)
        if cv2.waitKey(1) & 0xff == ord('q'):
            break
        
cap.release()
out.release()
cv2.destroyAllWindows()
    