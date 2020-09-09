#!python3
# -*- coding:utf-8 -*-

'''
  sklearnによる主成分分析
  　高次元のデータに対して分散が大きい方向を探して、元の次元と同じかそれよりも低くする手法。
'''

import numpy as np
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA

#テスト用データの作成
np.random.seed(123)
X = np.random.random(size=50)
Y = 2 * X + 0.5 * np.random.rand(50)

#テスト用データの表示
fig, ax = plt.subplots()
ax.scatter(X,Y)
ax.set_xlim(0, 1.1)
ax.set_ylim(0, 3.1)
plt.show()

#主成分分析実行
#n_componentsには変換後の次元数を指定している
pca = PCA(n_components=2)
X_pca = pca.fit_transform(np.hstack((X[:, np.newaxis], Y[:, np.newaxis])))
print(X_pca)

fig, ax = plt.subplots()
ax.scatter(X_pca[:, 0], X_pca[:, 1])
ax.set_xlim(-1.1, 1.1)
ax.set_ylim(-1.1, 1.1)
plt.show()