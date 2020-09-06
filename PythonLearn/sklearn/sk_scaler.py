#!python3
# -*- coding:utf-8 -*-

'''
  scikit-learnの正データ規化方法
'''

import numpy as np
import pandas as pd
from sklearn.preprocessing import MinMaxScaler, StandardScaler

#テストデータ作成
df = pd.DataFrame({ 'A': range(1,6),
                    'B': [100, 200, 400, 500, 800]})
print('df describe')
print(df.describe())
print('')

#分散正規化
# 特徴量の平均が0、標準偏差が1となるように特徴量を変換する処理。
# 特徴量の幅が異なるデータに対してもスケールを揃えて処理が可能となる。
# 　例えば画像認識などでwidthとheightがバラバラな画像を扱う場合などで使用できる。
stdsc = StandardScaler()
print('after standart scalized')
print(stdsc.fit_transform(df))
print('')

#最小最大正規化
# 特徴量の最小値が0、最大値が1となるように変換する処理。

