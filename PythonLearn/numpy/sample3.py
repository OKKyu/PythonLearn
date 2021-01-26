#! python3
# -*- coding:utf-8 -*-
'''
  ユニバーサルファンクション
  map()のように、ndarray内の各要素に一括で処理を行える
'''
import random
import math
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
#度数法(0〜360)ではなく弧度法で指定しないといけない点に注意。
print("sin, cos")
#度数法で角度を設定
l = np.array([0, 30, 60, 90])
#弧度法に変換
l = l / 360 * math.pi * 2
#ユニバーサルファンクションを適用してみる
print(np.sin(l))
print(np.cos(l))
print(np.tan(l))
print("--------")

#おまけ　度数法と弧度法を互いに変換する便利関数がある。
print("radians " + str(np.radians(180)))
print("deg2rad " + str(np.deg2rad(180)))
print("rad2deg " + str(np.rad2deg(3.14)))

#平均、中央値、最瀕値
print("mean, median, mod")
l = np.array([1, 2, 2, 2, 3, 3, 4])
print(np.mean(l))
print(np.median(l))
#print(np.mod(l))
print("--------")

#積
print("prod")
print(np.prod(l))
print("--------")
#幾何平均
print("mean prod")
print(np.prod(l) ** (1/len(l)))
print("--------")


#四捨五入、切り捨て、切り上げ
print("round, trunc, floor, ceil")
# 配列 [-1.7, -1.5, -0.2, 0.2, 1.5, 1.7, 2.0] を作成
a = np.array([-1.7, -1.5, -0.2, 0.2, 1.5, 1.7, 2.0])
# 四捨五入 (小数点以下 .5 以上は繰上げ、.5未満は切捨て)
print(np.round(a))
# 切り捨て (小数部分を取り除く)
print(np.trunc(a))
# 切り捨て (小さい側の整数に丸める)
print(np.floor(a))
# 切り上げ (大きい側の整数に丸める)
print(np.ceil(a))
# ゼロに近い側の整数に丸める
print(np.fix(a))
print("--------")

#最大値、最小値
print("max, min")
print(np.max(a))
print(np.min(a))
print("--------")

#平方根
print("sqrt")
print("before " + str([1, 4, 9, 16]))
print("sqrt " + str(np.sqrt([1, 4, 9, 16])))
print("--------")