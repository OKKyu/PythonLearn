#! python3
# -*- coding: utf-8 -*-
'''
  numpyによるデータ（配列）を生成する方法
'''
import numpy as np

#numpyにも連番生成用のメソッドarangeがある。
#標準のrangeメソッドと同様に使える。違いは返却結果がndarrayという点。
print("arange")
print(np.arange(1, 5))
#ndarray方式のスライス、インデキシングも使える。
print(np.arange(1, 20, 3)[[0, 1, 2]])
print("------\n")

#numpy配列の乱数生成
#randomとrandは0-1の乱数を生成する。引数には次元数を代入する
print("random")
np.random.seed(123)
print(np.random.random((2, 3)))
print("rand")
np.random.seed(123)
print(np.random.rand(2, 3))
print("------\n")

#randint　標準のrandom.randintと異なり第三引数のタプルに次元数を設定できる。
# リスト内包表現で回さないでいいので便利。
print("randint")
np.random.seed(123)
print(np.random.randint(0, 5, (2, 3)))
print("------\n")

#uniform　標準のrandom.uniformと異なり第三引数のタプルに次元数を設定できる。
# リスト内包表現で回さないでいいので便利。
print("uniform")
np.random.seed(123)
print(np.random.uniform(0, 5, (2, 3)))
print("------\n")

#randn 標準正規分布(平均=0, 標準偏差=1)に従う形でランダム値を返却する。
#１回実行しただけではよくわからないが、1万サンプルぐらい抽出してヒストグラムにすると
#それっぽくなる。rand同様、引数に次元数の指定が可能。
print("randn")
np.random.seed(123)
print(np.random.randn(10))

#normalメソッドでは平均、標準偏差も指定できる。
#normal(0,1,10)とするとrandnと同じ。
print("normal")
np.random.seed(123)
print(np.random.normal(0, 1, 10))
print("------\n")
#他にも正規分布以外の分布に基づく乱数生成も可能。興味があればnkmk辺りを参照。

#linspace 等間隔の配列を作る
#start〜stopまでの範囲を、第三引数の数で等分割する
print("linspace")
print(np.linspace(0, 10, 3))
print("------\n")

#diff 隣り合う要素間の差分を抜き出し、ndarrayで返す。
#右隣 - 左隣 と計算している。
print("diff")
print(np.diff([2, 2, 6, 1, 3]))
print("------\n")

#concatenate  要するにconcat。複数の配列を１つに連結する。
#２つ以上の配列を１つの配列にまとめて引数に代入する。
#配列はndarrayでなくでもよい。また、型が異なっていても一応結合できる。
#以下は整数と少数が混在した場合だが、少数へと昇格している。
print("concatenate")
l = np.arange(5)
n = np.arange(10, 20, 2)
o = [0.1, 0.3, 0.4]
p = np.concatenate([l, n, o])
print(p)
print(p.dtype)
print("------\n")

#hstack,vstack
#hは列の追加、vは行の追加を行う。concatenateの多次元バージョンと思えばいい。
l = np.array([[1, 2], [3, 4]])
n = np.array([[7], [8]])
o = np.array([9, 10])
print("hstack")
print(np.hstack([l, n]))
print("vstack")
print(np.vstack([l, o]))
print("------\n")

#行列のような内積を出す場合はdot()を使う。
a = np.array([1, 3, 4])
b = np.array([2, 2, 1])
print(np.dot(a,b))
print("------\n")

#同一値で初期化されたndarrayを生成する方法
#zero埋めされた配列の生成 0:false の配列を生成するのに使える。
z = np.zeros((2,4))
print(z)
print("------\n")
#1埋めされた配列の生成  1:true の配列として生成するのに使える。
z = np.ones((2,4))
print(z)
print("------\n")
#指定値で埋めた配列の生成
z = np.full((5,2), 99 ,dtype=np.int16)
print(z)
print("------\n")

#転地 行と列を入れ替える
t = np.array([[1, 2, 3], [4, 5, 6]])
print(t.T)
print("------\n")

#次元追加
d = np.arange(1,10)
print("add dimention with row direction.")
print(d[np.newaxis, :])
print(d[np.newaxis, :].shape)
print("add dimention with column direction.")
print(d[:, np.newaxis])
print(d[:, np.newaxis].shape)
print("------\n")