#!python3
# -*- coding:utf-8 -*-

import matplotlib.pyplot as plt  # ヒストグラム表示用
from PIL import Image

# PIL.Imageで画像を開く
img = Image.open("./Mandrill.bmp")

# 画像の表示
img.show()

# ヒストグラムの取得
hist = img.histogram()

# ヒストグラムをmatplotlibで表示
plt.plot(range(len(hist)), hist)
plt.show()
