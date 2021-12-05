#!python3
# -*- coding:utf-8 -*-
'''
  messagebox.py
    How to use simple useful messagebox as like "alert" in javascript.
'''
import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.attributes('-topmost', True)
root.withdraw()
root.lift()

# メッセージボックス（情報）
messagebox.showinfo("showinfo", "シンプルな情報表示")

# メッセージボックス（警告）
messagebox.showwarning("showwarning", "警告表示")

# メッセージボックス（エラー）
messagebox.showerror("showerror", "エラー表示")

# メッセージボックス（はい・いいえ）
ret = messagebox.askyesno("askyesno", "はい、いいえを尋ねるメッセージボックス")
messagebox.showinfo("return code:", str(ret))

# メッセージボックス（はい・いいえ）
ret = messagebox.askquestion("askquestion", "質問を投げるメッセージボックス")
messagebox.showinfo("return code:", str(ret))

# メッセージボックス（OK・キャンセル）
ret = messagebox.askokcancel("askokcancel", "OKまたはキャンセルを選択させるメッセージボックス")
messagebox.showinfo("return code:", str(ret))

# メッセージボックス（再試行・キャンセル）
ret = messagebox.askretrycancel("askretrycancel", "再試行、キャンセルを選択させるメッセージボックス")
messagebox.showinfo("return code:", str(ret))
