#!python3
# -*- coding:utf-8 -*-

import tkinter
from tkinter import Tk
from tkinter import ttk


class Application(tkinter.Frame):
    def __init__(self, master=None):
        tkinter.Frame.__init__(self, master)
        self.pack(expand=1)

        # title,size
        master.title("Pattern2")
        master.geometry("200x200")

        # add label
        ttk.Label(self, text="Simple Basic Pattern2").grid(column=0, row=0, sticky=tkinter.W)


root = Tk()
app = Application(master=root)
app.mainloop()
