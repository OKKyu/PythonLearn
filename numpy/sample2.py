#! python3
# -*- coding: utf-8 -*-
import numpy as np

#配列の作成
a = np.array([1,2,3])
print(a)

#numpyで作成した配列はただの配列ではないらしい。ndarrayとも呼ばれる。
#配列に演算をすると、全ての配列要素に演算がかかる。これをブロードキャストと呼ぶ。
print(a * 3) #[3,6,9]となる。
print(a + 2) #[3,4,5]となる。
print("-----")

#配列同士計算も可能。同じ位置にある要素同士での演算が行われる。
b = np.array([2,2,0])
print(a + b) #[3,4,3]
print(a / b) #[0.5,1,infinity]
print(a * b) #[2,4,0]
print("-----")

#行列のような内積を出す場合はdot()を使う。
print(np.dot(a,b))
