#!python3
# -*- coding:utf-8 -*-


'''
  this code was referrenced from 『退屈なことはPythonにやらせよう』
'''

import time
import pyautogui

try:
    pyautogui.FAILSAFE = True
    pyautogui.PAUSE = 0

    while True:
        pos_x, pos_y = pyautogui.position()
        print("x:{}, y:{}".format(str(pos_x).rjust(4), str(pos_y).rjust(4)))
        time.sleep(0.1)

except KeyboardInterrupt as ki:
    print("This program was forced shutdown by user.")
