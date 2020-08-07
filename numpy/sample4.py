#!python3
# -*- coding:utf-8 -*-
'''
  numpyの比較演算
'''
import numpy as np

l = np.array([-3, 0, 1, 4])
print(l)

#条件式 >,<,>=,<= などでndarrayを比較すると、true or falseの配列が戻る。
print(l > 0)
print(l == 1)
print(l % 2 == 0)

#count_nonzeroと併用すると、条件を満たす要素の数がカウントできる。
#これはこのメソッドがTrueを1、Falseを0とみなすためできる。
print(np.count_nonzero(l > 0))
print(np.count_nonzero(l == 1))
print(np.count_nonzero(l % 2 == 0))

#1つでもTrueがある場合を確認する場合はanyも使える
#anyは１つでも条件を満たす場合にTrue、１つも満たさない場合にFalseを返す
print(np.any(l == 1))

#全てTrueかどうかを確認する場合はallを使う
#返却結果はTrue or False
print(np.all(l >= 0))

#条件を満たす要素のみに絞り込んだ配列を取得できる。これが便利。
#この機能はndarrayでないと使えない。
print(l[l >= 1])
print(l[l % 2 == 0])