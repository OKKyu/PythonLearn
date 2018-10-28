#! python3
# -*- coding: UTF-8 -*-
# とても簡単グラフ表示

# randomでグラフのx軸、y軸の値を適当に作る。
import numpy as np
np.random.seed(1)
x = np.arange(10)
y = np.random.randint(1,100,10)
print(x)
print(y)

# matplotlibのpyplotを使用する。
# pyplotをインポートし、plotメソッドにx軸、y軸の値を代入。最後にshowを実行するだけ。
import matplotlib.pyplot as plt
plt.plot(x,y)
plt.show()