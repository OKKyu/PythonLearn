#!python3
# -*- coding:utf-8 -*-

'''
  This code is sample of using pyautogui
  about mouse operations
  complement: in pyautogui, origin point (0,0) is the most left and top location on screen.
              
'''

import pyautogui

pyautogui.PAUSE = 1
pyautogui.FAILSAFE = True

print("before move :")
pos_x, pos_y = pyautogui.position()
print("x:{}, y:{}\n".format(pos_x, pos_y))

print("moveTo :")
#moveTo method make mouse pointer move to absolute coordinates.
#duration is amount of seconds that spend for move.
pyautogui.moveTo(240, 240, duration=1)
pos_x, pos_y = pyautogui.position()
print("x:{}, y:{}\n".format(pos_x, pos_y))

print("moveRel :")
#moveRel method make mouse pointer move to relative coordinates.
pyautogui.moveRel(240, 240, duration=1)
pos_x, pos_y = pyautogui.position()
print("x:{}, y:{}\n".format(pos_x, pos_y))

print("click :")
#click is perform as one set of mouseDown and mouseUp.
pyautogui.click()

#clic can indicate absolute coordinates.
#button='left' is same that left button of mouse was clicked.
#instead of 'left', You can indicate 'right' and 'middle'.
print("click :")
pyautogui.click(pos_x, pos_y, button='left')

#if you want to keep mouse down and up after, you can mouseDown and mouseUp instead.
print("down and up:")
pyautogui.mouseDown(duration=1)
pyautogui.mouseUp(duration=1)

#pyautogui can made mouse doubleClick.
print("doubleClick :")
pyautogui.doubleClick()

#pyautogui can made mouse dragging.
print("drag :")
pyautogui.dragRel(30, 30, duration=1)

#pyautogui can scroll with mousewheel.
for i in range(10):
    pyautogui.scroll(1)
