#! python3
# -*- coding:utf-8 -*-

'''
  matplotlibのサンプル
  scatter 散布図
'''

import matplotlib.pyplot as plt
import numpy as np

fig, ax = plt.subplots()
np.random.seed(123)
x = np.random.rand(10)
y1 = np.random.rand(10)
y2 = np.random.rand(10)
y3 = np.random.rand(10)
y4 = np.random.rand(10)
y5 = np.random.rand(10)
y6 = np.random.rand(10)
ax.scatter(x, y1, label='triangle down', marker='v')
ax.scatter(x, y2, label='triangle up', marker='^')
ax.scatter(x, y3, label='square', marker='s')
ax.scatter(x, y4, label='star', marker='*')
ax.scatter(x, y5, label='x', marker='x')
ax.scatter(x, y6, label='circle(default)', marker='o')
ax.legend()
plt.show()