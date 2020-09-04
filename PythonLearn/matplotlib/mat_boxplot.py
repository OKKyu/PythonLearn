#! python3
# -*- coding:utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt

'''
  matplotlibのサンプル
  boxplot 箱ひげ図
'''

#boxplot 箱ひげ図
fig, ax = plt.subplots()
x0 = np.random.normal(0,100,2500)
x1 = np.random.normal(0,100,2500)
x2 = np.random.normal(0,100,2500)

labels = ['x0', 'x1', 'x2']
ax.boxplot((x0, x1, x2), labels=labels)
ax.legend(loc='best')
plt.show()
