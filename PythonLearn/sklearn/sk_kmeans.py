#!python3
# -*- coding:utf-8 -*-

'''
 scikit-learnによるk-mean法。
 k-meanはクラスタリング手法の１つ。クラス（ラベル）がまだ付与されていないデータを
 クラス分けする。分割方法の詳細については書籍を参照。ランダムにクラスをデータに割り振って、
 各クラスごとの最も中心となる点を計算し、中心点をもとにクラスを振り直す。
'''

import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from sklearn.cluster import KMeans

#データを準備する
iris = load_iris()
#Petal widthと Sepal widthのみを取る。また、今回はクラス分けを機械学習で行うので、
#正解ラベルtargetは使わない。
X = iris.data[:100, [0,2]]

#クラスタ前を表示
fig, ax = plt.subplots()
ax.scatter(X[:, 0], X[:, 1])
plt.show()

#クラスタリング k-meansを実行する
# n_clusters  クラス数
# init        初期クラスの設定方法
# n_init      クラスタリングを実行する回数
# tol         k-meansを打ち切る許容誤差。n_initの回数分クラスタリングがまだ実行されていない場合でも、
#             許容誤差を下回る場合に処理を打ち切る。
kmean = KMeans(n_clusters=3, init='random', n_init=10, random_state=123)
y_km = kmean.fit_predict(X)

fig, ax = plt.subplots()

#クラス0のインデックスをXに与え、Xのx座標とy座標をプロットしている。
ax.scatter(X[y_km == 0, 0], X[y_km == 0, 1], marker='o', label='class 0')
ax.scatter(np.mean(X[y_km == 0, 0]), np.mean(X[y_km == 0, 1]), marker='x', color='red')

#クラス1のインデックスをXに与え、Xのx座標とy座標をプロットしている。
ax.scatter(X[y_km == 1, 0], X[y_km == 1, 1], marker='s', label='class 1')
ax.scatter(np.mean(X[y_km == 1, 0]), np.mean(X[y_km == 1, 1]), marker='x', color='red')

#クラス2のインデックスをXに与え、Xのx座標とy座標をプロットしている。
ax.scatter(X[y_km == 2, 0], X[y_km == 2, 1], marker='v', label='class 2')
ax.scatter(np.mean(X[y_km == 2, 0]), np.mean(X[y_km == 2, 1]), marker='x', color='red')

ax.set_xlabel('Sepal Width')
ax.set_ylabel('Pepal Width')
ax.legend()
plt.show()