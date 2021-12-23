#!python3
# -*- coding:utf-8 -*-
'''
  This code is original tutorial from tkdocs.com.
  https://tkdocs.com/tutorial/firstexample.html
'''
import tkinter
from tkinter import *
from tkinter import ttk


def calculate(*args):
    '''
      Process of Button. 
      Converting value from feet to meter.
    '''
    try:
        value = float(feet.get())
        meters.set(int(0.3048 * value * 10000.0 + 0.5) / 10000.0)
    except ValueError:
        pass


# Create base window
root = Tk()
root.title('bbb')
# add frame
frame = ttk.Frame(root, padding='3 3 12 12')  # padding がよく分からん
frame.grid(column=0, row=0, sticky=(N, W, E, S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)


feet = StringVar()
feet_entry = ttk.Entry(frame, width=12, textvariable=feet)
feet_entry.grid(column=2, row=1, sticky=(W, E))

meters = StringVar()
ttk.Label(frame, textvariable=meters).grid(column=2, row=2, sticky=(W, E))

ttk.Button(frame, text='Calculate', command=calculate, width=18).grid(column=3, row=3, sticky=W)

ttk.Label(frame, text='feet').grid(column=3, row=1, sticky=W)
ttk.Label(frame, text='is equivalent to').grid(column=1, row=2, sticky=E)
ttk.Label(frame, text='meters').grid(column=3, row=2, sticky=W)

feet_entry.focus()
root.bind("<Return>", calculate)

root.mainloop()
