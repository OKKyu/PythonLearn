#!python3
# -*- coding:utf-8 -*-

import numpy as np
import pandas as pd

'''
  This source code is a sample of using pandas.
  complement of absent data.
'''

df = pd.read_csv('./201705health.csv', encoding='utf-8', index_col='日付', parse_dates=True)
print('before complement')
print(df)
print('')

print('drop na rows')
print(df.dropna())
print('')

print('complement by fixed value')
print(df.fillna(0))
print('')

print('complement by value just before it.')
print(df.fillna(method='ffill'))
print('')

print('complement with mean value')
print(' This mean value is calculated by only non-absented datas.')
print(df.fillna(df.mean()))
print('')

print('complement with median value')
print(df.fillna(df.median()))
print('')

print('complement mode value')
print(df.fillna(df.mode().iloc[0, :]))
print('')