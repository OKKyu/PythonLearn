#! python3
# -*- coding:utf-8 -*-
#https://toukei.link/programmingandsoftware/statistics_by_python/histogram_by_python/

import pandas as pd  # データフレームを作成するライブラリ 
import random # 乱数を発生させるライブラリ
import numpy as np #数値計算を行うためのライブラリ
import matplotlib.pyplot as plt # ヒストグラムを作成するライブラリ

np.random.seed(10)
h = np.round([np.random.normal(171, 6, 50)]+[np.random.normal(158, 5, 50)],1)
h = h.flatten().tolist()

mydata = pd.DataFrame({
                    'id' :list(range(1, 101)),
                    'gender':np.repeat(np.array(["M","F"]), [50,50]).tolist(),
                    'height':h
})

# pd.DataFrame.to_html(mydata.head(5))
# pd.DataFrame.to_html(mydata.tail(5))

# column='height'で変数を指定。
# bins=10でヒストグラムの帯の数を指定。
mydata.hist(column='height', bins=10)

mydata.hist(column='height', bins=10, by = mydata["gender"])

# matplotlib.pyplotを利用して作成

plt.hist(h)
plt.title('Height by using matplotlib.pyplot') 