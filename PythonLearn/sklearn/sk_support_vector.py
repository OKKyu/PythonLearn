#!python3
# -*- coding:utf-8 -*-

'''
  サポートベクトルマシンの用法
'''

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.datasets import load_iris
from sklearn.svm import SVC

#サポートベクトルマシンの使用
#後々パラメータを変更したサンプルを用意するので、関数化する。
def plot_boundary_margin_sv(D0, T0, D1, T1, kernel, C, xmin=-1, xmax=1, ymin=-1, ymax=1):
    #インスタンス生成
    svc = SVC(kernel=kernel, C=C)
    
    #学習
    #説明変数の配列のタプルと、目的変数の配列のタプルを渡す。
    svc.fit(np.vstack((D0, D1)), np.hstack((T0, T1)))
    
    #学習結果を表示
    fig, ax = plt.subplots()
    ax.scatter(D0[:, 0], D0[:, 1], marker='o', label='class 0')
    ax.scatter(D1[:, 0], D1[:, 1], marker='x', label='class 1')
    
    #決定境界とマージンのプロット
    #図の両端までを等間隔で仕切る
    xx, yy = np.meshgrid(np.linspace(xmin, xmax, 100), np.linspace(ymin, ymax, 100))
    xy = np.vstack([xx.ravel(), yy.ravel()]).T
    p = svc.decision_function(xy).reshape((100, 100)) #ここの説明、本が端折ってやがる。
    #境界を引く
    ax.contour(xx, yy, p,
               colors='k', levels=[-1, 0, 1],
               alpha=0.5, linestyles=['--', '-', '--'])
    
    #サポートベクトルをプロットする
    ax.scatter(svc.support_vectors_[:, 0], svc.support_vectors_[:, 1],
               s=250, facecolors='none', edgecolors='black')
    
    ax.legend(loc='best')
    plt.show()

#使用
#以下はサポートベクトルマシンの説明を見やすくするために、境界が明確なサンプルデータを
#作成している。
np.random.seed(123)

#X軸Y軸ともに０〜１の分布データ
d0 = np.random.uniform(size=(100, 2))
#そのラベル
t0 = np.repeat(0, 100)

#X軸Y軸ともにー１〜０の分布データ
d1 = np.random.uniform(-1.0, 0.0, size=(100, 2))
#そのラベル
t1 = np.repeat(1, 100)

#散布図にプロット
fig, ax = plt.subplots()
ax.scatter(d0[:, 0], d0[:, 1], marker='o', label= 'class 0')
ax.scatter(d1[:, 0], d1[:, 1], marker='x', label= 'class 1')
ax.legend(loc='best')

plt.show()

#線形で判定する。
plot_boundary_margin_sv(d0, t0, d1, t1, kernel='linear', C=1e6)


#直線でない場合
# [データ数 , x軸y軸] の2次元データをランダムに作成する。
d0 = np.random.random(size=(100,2))
#これはデータを非直線にするための恣意的な操作。
t0 = (d0[:, 1] > 3*(d0[:, 0]-0.5) ** 2 + 0.5).astype(int)
#表示してみる。
fig, ax = plt.subplots()
ax.scatter(d0[t0 == 0, 0], d0[t0 == 0, 1], marker='x', label='class 0')
ax.scatter(d0[t0 == 1, 0], d0[t0 == 1, 1], marker='o', label='class 1')
plt.show()

#動径基底関数(radial basis function)で境界を決める。
plot_boundary_margin_sv(d0[t0 == 0, :], t0[t0 == 0], d0[t0 == 1, :], t0[t0 == 1], kernel='rbf',
                        C=1e3, xmin=0, ymin=0)

