#! python3
# -*- coding:utf-8 -*-
'''
  ユニバーサルファンクション
  map()のように、ndarray内の各要素に一括で処理を行える
'''
import random
import numpy as np

#abs 絶対値に変換する
np.random.seed(123)
print("abs")
l = np.random.randint(-10, 10, 5)
print(type(l))
print(np.abs(l))
#実はndarrayの場合は標準absでもできる。
#標準リストを標準absで処理しようとするとリストじゃないと怒られる。
print(abs(l))
#print(abs([ random.randint(-5,-1) for x in range(5) ]))
print("--------")

#sin, cos
#サイン、コサインに変換する
print("sin, cos")
l = np.array([0, 30, 60, 90])
print(np.sin(l))
print(np.cos(l))
print("--------")

#平均、中央値、最瀕値
print("mean, median, mod")
l = np.array([1, 2, 2, 2, 3, 3, 4])
print(np.mean(l))
print(np.median(l))
print(np.mod(l))
print("--------")

#四捨五入、切り捨て、切り上げ
print("round, trunc, floor, ceil")
# 配列 [-1.7, -1.5, -0.2, 0.2, 1.5, 1.7, 2.0] を作成
a = np.array([-1.7, -1.5, -0.2, 0.2, 1.5, 1.7, 2.0])
# 四捨五入 (小数点以下 .5 以上は繰上げ、.5未満は切捨て)
np.round(a)
# 切り捨て (小数部分を取り除く)
np.trunc(a)
# 切り捨て (小さい側の整数に丸める)
np.floor(a)
# 切り上げ (大きい側の整数に丸める)
np.ceil(a)
# ゼロに近い側の整数に丸める
np.fix(a)
print("--------")

#
print("maximum, mininum")
np.maximum(a)
np.minimum(a)
print("--------")