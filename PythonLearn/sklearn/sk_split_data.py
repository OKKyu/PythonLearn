#!python3
# -*- coding:utf-8 -*-

'''
  scikit-learnによる学習用・テスト用データの分割
'''

import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.datasets import load_iris

#sklearn.datasetsからトイデータを読み込む
# 読み込まれてたデータの構造はこうなっている。
#  data:   説明変数となるデータ。    １次元目はデータ数、２次元目は１サンプルが持つ全ての説明変数。
#  target: 目的変数となる整数ラベル。おかげで一からlabel encodingしないでよい。dataのインデックスに対応している。
#  target_names:目的変数となるラベル。
#  DESCR: 当該トイデータについての要約が英文で記載されている。
iris = load_iris()
print(iris)

#学習データ、テストデータに分割する
# test_size : 第一引数に入力したデータのうち何割をテストデータに回すかを指定する。 以下は 7割が学習用、3割がテスト用に
#             配分される。
# random_state : 学習用、テスト用データへと割り振られる乱数のシードを設定する。本番では要らない。
X_train, X_test, Y_train, Y_test = train_test_split(iris.data, iris.target, test_size=0.3, random_state=123)
print(X_train.shape)
print(X_test.shape)
print(Y_train.shape)
print(Y_test.shape)

