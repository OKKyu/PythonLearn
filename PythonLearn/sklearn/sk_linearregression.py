#!python3
# -*- coding:utf-8 -*-

'''
  scikit-learnによる線形回帰の実行
  線型回帰：ある目的変数を説明変数で説明する。式にすると以下の通り。
            y = x1 + x2 + ... + b
            説明変数(x1)が１個の場合は単回帰、複数ある場合は重回帰と呼ぶ。
            しかし理論値と観測値は異なることのほうが多い。そこで説明変数に
            誤差を調整するためのパラメータこと"重み"を設定し、かつ目的変数と
            説明変数の誤差の二乗が最小となるように重みを計算する。最小二乗法という。
             誤差関数 = { y - (w1x1 + w2x2 + ... + b)}**2  +
                        { y - (w1x1 + w2x2 + ... + b)}**2  +
                           ..... 以下繰り返し .....
            このモデルは説明変数と目的変数の関係が線形であるという前提のもと使用する。
            直線で表せない場合は多項式回帰やサポートベクトルを使うこともある。
'''

import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import load_boston
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

#データロード
boston = load_boston()
#LinearRegressionの場合、yにクラスではなく目的変数を入力する。
x_train, x_test, y_train, y_test = train_test_split(boston.data, boston.target, test_size=0.3, random_state=123)

#インスタンス生成
lr = LinearRegression()

#学習
lr.fit(x_train, y_train)

#予測
y_pred = lr.predict(x_test)

#結果を表示
print("test data num:" + str(len(x_test)))

#プロット
fig, ax = plt.subplots()
ax.scatter(y_pred, y_test, marker='o', label='plot')
ax.set_xlabel("predict value")
ax.set_ylabel("actual value")
ax.legend(loc="best")
plt.show()

#性能評価
#クラス分類とは異なり予測値が返却されるので、y_pred == y_test になることはほどんどない。

error = np.sum(np.abs(y_test - y_pred))
print('Mean absolute error:' + str(error))


