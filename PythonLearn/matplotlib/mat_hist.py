#! python3
# -*- coding:utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt

'''
  matplotlib
  hist ヒストグラム
'''

#hist ヒストグラム
# タイトル追加
fig, ax = plt.subplots()
ax.set_title('score')
# x軸にscore、y軸にfreq
ax.set_xlabel('score')
ax.set_ylabel('freq')
# 目盛りを変更
ax.set_xticks([50,75,80,100]) 
ax.set_yticks([0,10,20,30,40,80,100])
# data create
# random data. 1:range minimum 2: range maximum 3:dimension
data = np.random.randint(50,100,(2500,))

# ヒストグラムを描画する（表示する幅は50〜100）、階級数（棒の数）は20
ax.hist(data, range=(50, 100), bins=20)
plt.show()

#複数ヒストグラムを並べて表示もできる。
fig, ax = plt.subplots()
y0 = np.random.normal(50,100,2500)
y1 = np.random.normal(50,100,2500)
y2 = np.random.normal(50,100,2500)

labels = ['y0', 'y1', 'y2']
ax.hist((y0, y1, y2), label=labels)
ax.legend(loc='best')
plt.show()
