#! python3
# -*- coding:utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt

'''
  matplotlibのサンプル
  bar 棒グラフ
'''

#bar 棒グラフ
fig, ax = plt.subplots()
x = [1, 2, 3]
y = [10, 2, 3]
ax.bar(x, y, tick_label=['A', 'B', 'C'])
ax.set_xlabel('class')
ax.set_ylabel('num of people')
plt.show()

#horizontal bar
fig, ax = plt.subplots()
ax.barh(x, y, tick_label=['A', 'B', 'C'])
plt.show()

#multi bar
fig, ax = plt.subplots()
x = [1, 2, 3]
y1 = [10, 2, 3]
y2 = [4, 6, 9]

#最初の棒をプロット
width = 0.4
ax.bar(x, y1, width=width, tick_label=['A', 'B', 'C'], label='y1')

#棒グラフを並べる場合、最初にプロットした棒幅分、後からプロットした棒を
#右方向にずらす必要がある。ちょっと面倒。
x2 = [ num + width for num in x ]
ax.bar(x2, y2, width=width, tick_label=['A', 'B', 'C'], label='y2')

ax.set_xlabel('class')
ax.set_ylabel('num of people')
ax.legend()

plt.show()