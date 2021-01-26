#! python3
# -*- coding:utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt

'''
  matplotlibのサンプル
  pie 円グラフ
'''

#pie 円グラフ
labels = ['beef', 'pork', 'chicken']
x = [10, 3, 1]
fig, ax = plt.subplots()
#プロットの順番：デフォルトでは３時の方向から反時計周りになっている。
#１２時方向から開始するにはstarangleを、時計周りにするにはcounterclockを設定する。
#比率表示をする場合はautopctを設定する。
#影を付ける場合はshadowを設定する。
#一部要素を切り出したオシャンティなデザインにする場合はexplodeを設定する。
explode = [0.0, 0.8, 0.0]
ax.pie(x, labels=labels, startangle=90, counterclock=False, autopct='%1.2f%%', shadow=True, \
       explode=explode)
#円グラフのアスペクト比を保つ場合に設定する
ax.axis('equal')

#その他
ax.set_title('amount of consumption of meat', family='fantasy', size=10, weight='bold')

plt.show()