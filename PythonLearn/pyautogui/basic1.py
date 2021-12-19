#!python3
# -*- coding:utf-8 -*-

'''
  This code is sample of using pyautogui
  Basical settings
'''

import time
import pyautogui

# Setting wait time. Scale is seconds.
# If PAUSE parameters has been setted, process is stopped when pyautogui's function was runned.
pyautogui.PAUSE = 1

# Setting fail safe option.
# If FAILSAFE is true, User can break pyautogui by moving mouse pointer to most left-top position on screen.
# It is occured FailSafeException. (by the way, default value is True.)
pyautogui.FAILSAFE = True

# size function return screen width and height.
print("screen size:" + str(pyautogui.size()))
print("")
