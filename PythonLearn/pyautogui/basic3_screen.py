#!python3
# -*- coding:utf-8 -*-

import pyautogui

# pyautogui can capture full screenshot.
im = pyautogui.screenshot()

print(im.getpixel((50, 201)))
print(pyautogui.pixelMatchesColor(50, 200, im.getpixel((50, 201))))

# locateOnScreen return location of inputed image on screen.
box = pyautogui.locateOnScreen(im)
print(box)

# center method return center point of inputed image or tuple of bounding box.
pyautogui.center(box)
pyautogui.doubleClick()
