#!python3
# -*- coding:utf-8 -*-

from tkinter import *
from tkinter import ttk

class Application(Tk.Frame):
    def __init__(self, master=None):
        Tk.Frame.__int__(self, master)
        self.pack()
        

root = Tk()
app = Application(master=root)
app.mainloop()