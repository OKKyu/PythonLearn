#! python3
# -*- coding:utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt

'''
  サブプロットを複数設定するサンプルコード
'''

#one subplot
x = [1, 2, 3]
y = [2, 4, 8]
#描画オブジェクトfigとサブプロットaxを生成する
fig, ax = plt.subplots()
#サブプロット(折れ線)にデータを設定
ax.plot(x, y)
#タイトルを設定
ax.set_title('00P-style')
#表示
plt.show()

#two subplot
x2 = [1, 2, 3]
y2 = [1, 15, 4]
#サブプロットを２つ生成する
fig, axes = plt.subplots(2)
axes[0].plot(x, y)
axes[1].plot(x2, y2)
axes[0].set_title('figure one')
axes[1].set_title('figure two')

plt.show()

#サブプロットを４つ生成する (2x2)
fig, axes = plt.subplots(2,2)
#以下も同じ2x2となる
#fig, axes = plt.subplots(nrows=2, ncols=2)
axes[0, 0].set_title('figure one')
axes[0, 1].set_title('figure two')
axes[1, 0].set_title('figure tree')
axes[1, 1].set_title('figure four')
plt.show()


