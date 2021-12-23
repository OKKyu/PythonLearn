#! python3
# -*- coding:utf-8 -*-

import tkinter as tk
from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
from tkinter import ttk


class Application(tk.Frame):
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.pack(expand=1, fill=tk.BOTH, padx=10, pady=8, side=tk.TOP)

        # variable
        self.csvname = StringVar()
        self.csvname.set('csv name here')

        # frame1 csv file select.
        self.frame1 = tk.Frame(self, bd=1, relief=tk.SOLID, height=50)
        self.frame1.pack(expand=1, fill=tk.X, padx=2, pady=2)

        # frame1 widgets
        self.label_csvname = tk.Label(self.frame1, textvariable=self.csvname)
        self.label_csvname.grid(column=1, row=0, sticky=tk.W)
        self.button_selectcsv = tk.Button(self.frame1, text='ファイル選択', command=self.readcsv)
        self.button_selectcsv.grid(column=0, row=0, sticky=tk.W)

        # frame2 screen select
        self.frame2 = tk.Frame(self, bd=1, relief=tk.SOLID, height=100)
        self.frame2.pack(expand=1, fill=tk.X)

        # frame2 screenlist
        self.readscreenlist()

        # frame3 table view
        self.frame_treeview = tk.Frame(self, bg='white', bd=1, relief=tk.SOLID, height=250)
        self.frame_treeview.pack(expand=1, fill=tk.X, padx=2, pady=2)

        # frame4 footer, run button
        self.frame_footer = tk.Frame(self, padx=10)
        self.frame_footer.pack(fill=tk.X)

        self.button_run = tk.Button(self.frame_footer, text='実行', command=self.run)
        self.button_run.pack(side=tk.RIGHT)

    def readcsv(self):
        ft = [('data files', '*.csv')]
        result = tk.filedialog.askopenfilename(filetypes=ft)

        if result != None and len(result) > 0:
            # read data
            headers, datas = cfunc.readcsv(result)
            name = Path(result)
            self.csvname.set(name.name)

            # initialize tree view
            if ('tree' in dir(self)) == True:
                self.tree.destroy()
                self.ysb.destroy()
                self.xsb.destroy()

            # create tree view
            tree = ttk.Treeview(self.frame_treeview)

            # scroll bar
            ysb = ttk.Scrollbar(self.frame_treeview, orient=VERTICAL, command=tree.yview)
            tree.configure(yscrollcommand=ysb.set)
            ysb.pack(side="right", fill="y")

            xsb = ttk.Scrollbar(self.frame_treeview, orient=HORIZONTAL, command=tree.xview)
            tree.configure(xscrollcommand=xsb.set)
            xsb.pack(side="bottom", fill="x")

            # 列インデックスの作成
            tree["columns"] = tuple([idx for idx in range(len(headers))])
            # 表スタイルの設定(headingsはツリー形式ではない、通常の表形式)
            tree["show"] = "headings"

            # 各列の設定
            for idx, header in enumerate(headers):
                # 幅 先頭データの文字数に定数を掛ける
                if datas[0].get(header) != None:
                    width = len(datas[0].get(header, "two size")) * 20
                else:
                    width = len(header) * 20
                tree.column(idx, width=width)
                # カラム表示名
                tree.heading(idx, text=header)

            # データの挿入
            for data in datas:
                # データを入れる
                values = data.values()
                tree.insert('', 'end', values=list(values))

            # tree、headersの保持
            self.tree = tree
            self.headers = headers
            self.ysb = ysb
            self.xsb = xsb

            # display        print(hasattr(self, "tree"))
            tree.pack(fill=tk.BOTH)

    def readscreenlist(self):
        # ツリービュー作成
        # ツリービューのheightは行数
        # create tree view for screen names
        scr_tree = ttk.Treeview(self.frame2, height=3)

        # scroll bar
        scr_ysb = ttk.Scrollbar(self.frame2, orient=VERTICAL, command=scr_tree.yview)
        scr_tree.configure(yscrollcommand=scr_ysb.set)
        scr_ysb.pack(side="right", fill="y")

        scr_xsb = ttk.Scrollbar(self.frame2, orient=HORIZONTAL, command=scr_tree.xview)
        scr_tree.configure(xscrollcommand=scr_xsb.set)
        scr_xsb.pack(side="bottom", fill="x")

        # 列インデックスの作成
        scr_tree["columns"] = (0, )
        # 表スタイルの設定(headingsはツリー形式ではない、通常の表形式)
        scr_tree["show"] = "headings"
        # カラム表示名
        scr_tree.heading(0, text="入力したい画面")

        # 画面名ディレクトリの取得
        lst = Path(cfunc.form_img_path)
        if lst.exists() == False or lst.is_dir() == False:
            raise FileNotFoundError("There is no indicated directory. " + str(lst))

        for scr_parts_dir in lst.iterdir():
            if scr_parts_dir.is_dir == False:
                continue
            else:
                scr_tree.insert('', 'end', values=[scr_parts_dir.name])

        # display
        self.scr_tree = scr_tree
        scr_tree.pack(fill=tk.X)

    def run(self):
        if hasattr(self, "tree") == False:
            print("There is no view, no selected csv file yet.")
            return

        scr_selection = self.scr_tree.selection()
        selection = self.tree.selection()
        if len(selection) == 1 and len(scr_selection) == 1:
            data = self.tree.item(selection[0], 'values')
            dict_data = {key: val for key, val in zip(self.headers, data)}
            print(dict_data)
            cfunc.target_scr_name = self.scr_tree.item(scr_selection[0], 'values')[0]
            cfunc.run(self.headers, dict_data)


# ルートフレーム
root = Tk()
# タイトル
root.title("OneFormInputer")
# フレームの縦横サイズ
root.geometry("700x550")
# 独自定義した画面をルートフレームに設定する
app = Application(master=root)
# 実行
app.mainloop()
