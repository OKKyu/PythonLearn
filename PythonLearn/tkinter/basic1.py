#!python3
# -*- coding:utf-8 -*-
'''
  This code is original tutorial from tkdocs.com.
  https://tkdocs.com/tutorial/firstexample.html
'''
import tkinter
from tkinter import Tk
from tkinter import ttk

# testing whether tkinter can available.
tkinter._test()

# window only.
root = Tk()
root.title('Pattern1')
root.geometry('200x200')
lbl = ttk.Label(root, text="Simple Basic Pattern1").grid(column=0, row=0, sticky=tkinter.E)
root.mainloop()
