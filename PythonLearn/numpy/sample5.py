#! python3
# -*- coding: utf-8 -*-
import numpy as np

lis = np.array([4, 6])

#L0 Norm
print('norm 0')
print(np.linalg.norm(lis, ord=0))

#L1 Norm
#単純にベクトルの各要素の絶対値を足し合わせる。
#X=4, Y=6の場合、 4+6 となる
print('norm 1')
print(np.linalg.norm(lis, ord=1))

#L2 Norm
#原点からベクトルを終点とした直線距離を求める。←の実際の長さを計算する。
print('norm 2')
print(np.linalg.norm(lis, ord=2))