#! python3
# -*- coding:utf-8 -*-
#plot
# グラフ描画のためmatplotlibのpyplotをインポート
import matplotlib.pyplot as plt
year = [1985,2010,2008,2015,2018]
weight = [55.2, 50.0, 58.4, 52.1, 56.0]
plt.plot(year,weight)
plt.show()

#hist
# タイトル追加
plt.title('score')

# x軸にscore、y軸にfreq
plt.xlabel('score')
plt.ylabel('freq')

# 目盛りを変更
plt.xticks([50,75,80,100]) 
plt.yticks([0,10,20,30,40,80,100])

# data create
import numpy as np
# random data. 1:range minimum 2: range maximum 3:dimension
data = np.random.randint(50,100,(2500,))

# ヒストグラムを描画する（表示する幅は50〜100）、階級数（棒の数）は20
plt.hist(data, range=(50, 100), bins=20)
plt.show()