#!python3
# -*- coding:utf-8 -*-

'''
  scikit-learnの前処理のサンプルコード
'''

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import OneHotEncoder

#欠損値ありのデータを作成する
df = pd.DataFrame([ [1, 6, 11],
                    [np.nan, 7, 12],
                    [3, 8, 13],
                    [4, np.nan, 14],
                    [5, 10, 15]
                  ])
df.columns = ['A', 'B', 'C']
print("include nan value")
print(df.isnull())

#欠損値の補完 meanでもmedianでも、固定値でもいい
print('filled nan value')
df = df.fillna(df.mean())
print(df)
print('')

#LabelEncoder
#説明変数のうち定性データを整数値にラベリングし直す。
#別にLabelEncoderを用いずとも処理できるが、覚えておくとよい。
df = pd.DataFrame({ 'A': range(1,6) ,
                    'B':[ 'a', 'b', 'a', 'b', 'c' ]
                   })
print('before label encoding')
print(df)

le = LabelEncoder()
la_encoded = le.fit_transform(df['B'])
print('after label encoding')
print('caution: the result of process is returned list object')
print(la_encoded)
print('check a variety of classes.:' + str(le.classes_))
print('')

#One-Hot Encoding
#定性データをラベリングし直した後、各ラベル値に該当するかどうかを真理値で持たせるもの。
# 1)上記カラムBの内容(a,b,c)を(0,1,2)に変換。ここまではLabelEncoding
# 2)新たにカラムa,b,cを追加し、カラムBが1ならカラムaをTrueにし、他カラムb,cにFalseを入れる。
# 詳細は以下サンプルコードを動かしてみるべし。
# 注意：Imputerと同様に、OneHotEncoderは今後廃止されるという。
df['C'] = la_encoded
df = pd.concat([df, pd.get_dummies(df['C'], prefix='CHot')] ,axis=1)
print(df)