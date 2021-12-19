#!python3
# -*- coding:utf-8 -*-
'''
  sample_pyperclip.py
    This is example of how copy to clipboard on python.
    Usually, It is used with pyautogui for paste another application.
'''
import pyperclip

a = "Hello!"
a += " Python"

pyperclip.copy(a)
