#!python3
# -*- coding:utf-8 -*-
'''
  sample_app.py
'''
import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.attributes('-topmost', True)
root.withdraw()
root.lift()

# メッセージボックス（情報）
messagebox.showinfo("showinfo", "シンプルな情報表示")

