#! python3
# -*- coding: utf-8 -*-
'''
  numpyの基本　ndarrayの生成、演算、スライス、インデキシング、dtype、コピー
'''
import numpy as np

#配列の作成
# ndarray型というnumpy独自のオブジェクトが生成される。
# 処理高速化の秘密はndarrayによる効率の良いメモリ管理にあるという。
# ndarray使わないとあまり早くならない。
a = np.array([1,2,3])
print(a)
print("-----")

#numpyで作成した配列はただの配列ではないらしい。ndarrayとも呼ばれる。
#配列に演算をすると、全ての配列要素に演算がかかる。これをブロードキャストと呼ぶ。
print("broad cast")
print(a * 3) #[3,6,9]となる。
print(a + 2) #[3,4,5]となる。
print(a - 2) #[-1,0,1]となる。
print(a / 2) #[0.5, 1, 1.5]となる。
print(a ** 2) #[1, 4, 9]となる。
print(a % 2) #[1, 0, 1]となる。
print(np.mod(a, 2)) #[1, 0, 1]となる。これも剰余算
#処理としては、要素数が少ないオペランド（ここでは * 3や + 2)を、
#要素数が多いほうに合わせて増幅させて計算しているという。
#例えば上記の a * 3は、
#  [1, 2, 3] * [3, 3, 3] ← 3が増幅している
#として扱われ、各インデックス同士で掛け合わされるという。
print("-----")

#配列同士計算も可能。同じ位置にある要素同士での演算が行われる。
b = np.array([2,2,0])
print(a + b) #[3,4,3]
print(a / b) #[0.5,1,infinity]
print(a * b) #[2,4,0]
print("-----")

#要素数の確認
#ndarrayはshapeという要素数を保持したメンバを持つ
c = np.array([[5,6], [3,3], [8,9]])
print("b shape :" + str(b.shape))
print("c shape :" + str(c.shape))

#変形
#numpyでは要素の次元数を変更できる。
d = c.reshape((2,3))
print(d)
#ravel,flattenで１次元配列に変形できる。
#ravelは浅いコピー、flattenは深いコピー。
e = c.ravel()
f = c.flatten()
print(e)
print(f)
print("-----\n")
#深いコピーをする場合はcopy()を使う

#dtype
#ndarrayに格納される要素の型と精度を設定する。
#これによって容量の節約などが可能になるが、異なる型を格納する事は不可能。
print("dtype : " + str(d.dtype))
#ndarrayの生成時にdtypeを指定することができる
#特に指定しない場合はint64となるようである。恐らく最大の容量を確保する型になる。
g = np.array(range(1,10,2), dtype=np.int16)
print("g's dtype : " + str(g.dtype))

#スライス
lst = [[1,2], [3,4], [7,8]]
#標準のlistの場合はカンマ指定でインデキシング、スライスはできない。以下はエラーとなる
#print(lst[1, 0])
#numpyの場合はスライス可能。
#nda[1][0]とnda[1,0]は同じ操作となる。
nda = np.array(lst)
print(nda[1][0])
print(nda[1,0])
#多次元のスライスの場合は以下のようになる。
print(nda[1:3, 1:2])
#以下は同様の操作とならないので注意。
print(nda[1:3][1:2])
print("-----\n")


