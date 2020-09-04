#! python3
# -*- coding:utf-8 -*-
import matplotlib.pyplot as plt
import numpy as np

'''
  matplotlibの共通設定
'''

#グラフのスタイル
plt.style.use('classic')
fig, ax = plt.subplots()
ax.plot([1, 2, 3], [1, 2, 3])
plt.show()
plt.style.use('ggplot')

#グラフのタイトル
fig, axes = plt.subplots(2)
axes[0].set_title('title one')
#軸ラベル
axes[0].set_xlabel('horizon')
axes[0].set_ylabel('vertical')
#凡例
axes[0].plot([1, 2, 3], [2, 4, 12], label='legend label')
axes[0].legend(loc='best')
plt.show()

#保存も可能。eps, jpeg, jpg, pdf, pgf, png, ps, raw, rgba, svg, svgz, tif, tiffがサポートされている。
fig.savefig('./test_plot_save.png')
fig.savefig('./test_plot_save.jpg')