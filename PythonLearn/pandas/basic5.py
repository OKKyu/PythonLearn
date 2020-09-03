#!python3
# -*- coding:utf-8 -*-

import numpy as np
import pandas as pd

'''
  This source code is a sample of using pandas.
  absent data complement
'''

df = pd.read_csv('./201705health.csv', encoding='utf-8', index_col='日付', parse_dates=True)
print('before complement')
print(df)
print('')

print('drop na rows')
print(df.dropna())
print('')

print('complement fixed value')
print(df.fillna(0))
print('')

print('complement just before value')
print(df.fillna(method='ffill'))
print('')

print('complement mean value')
print(' This mean value is calculated by only non-absented datas.')
print(df.fillna(df.mean()))
print('')

print('complement median value')
print(df.fillna(df.median()))
print('')

print('complement mode value')
print(df.fillna(df.mode().iloc[0, :]))
print('')