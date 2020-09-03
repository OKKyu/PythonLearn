#!python3
# -*- coding:utf-8 -*-

import numpy as np
import pandas as pd

'''
  This source code is a sample of using pandas library.
  statistic functions.
'''

df = pd.read_csv('201704health.csv', encoding='utf-8')

print('statistic functions can use whole dataframe columns.')
print('mean')
print(df.mean())
print('')
print('statistic functions can use also one column.')
print('mean 歩数:')
print(df.loc[:, '歩数'].mean())

print('max')
print(df.max())
print('min')
print(df.min())
print('mode')
print(df.mode())
print('median')
print(df.median())
print('std')
print(df.std())
print('count')
print(df[ df.loc[:, '摂取カロリー']==2300 ].count())
print('')

print('describe summary')
print(df.describe())
print('')

print('correlation coefficient')
print(df.corr())