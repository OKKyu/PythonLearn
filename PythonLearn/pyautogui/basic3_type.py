#!pyautogui
# -*- coding:utf-8 -*-

import pyautogui

pyautogui.typewrite("Hello! PyAutoGui!", 0.25)

# If you want to made pyautogui type as Enter, Space, Ctrl+v,
# You shoude use hotkey or typewrite with list.
#example1: hotkey
pyautogui.hotkey("enter")

# example2:typewrite with list
pyautogui.typewrite(["a", "b", "c", "\n"], 0.25)
pyautogui.typewrite(["space" for i in range(10)])
pyautogui.sleep(1)
pyautogui.typewrite(["enter"])
# other,write
# pyautogui.write(["enter"])

# shortcut key
# If you use by keyDown and keyUp, source code became to boared...
pyautogui.keyDown("ctrl")
pyautogui.keyDown("c")
pyautogui.keyUp("c")
pyautogui.keyUp("ctrl")
# other, press method.
pyautogui.press("enter", 5, interval=1)

# If you use with hotKey, you can write code very simply.
pyautogui.hotkey('ctrl', 'a')
pyautogui.hotkey('ctrl', 'c')
