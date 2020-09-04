#! python3
# -*- coding:utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt

'''
  matplotlibのサンプル
  plot 折れ線グラフ
'''

#plot 折れ線グラフ
#複数の折れ線を１図にプロットできる
fig, ax = plt.subplots()
year = [1985,2010,2008,2015,2018]
weight = [55.2, 50.0, 58.4, 52.1, 56.0]
heigth = [160.0, 160.2, 163.6, 161.1, 160.2]
ax.plot(year, weight, label='weight')
ax.plot(year, heigth, label='heigth')
ax.legend(loc='upper left')
plt.show()