#!python3
# -*- coding:utf-8 -*-

import numpy as np
import pandas as pd

'''
  This source code is a sample of using pandas.
  data concat each dataframe.
'''

df1 = pd.read_csv('201704health.csv', encoding='utf-8', index_col='日付', parse_dates=True)
print(df1)
df2 = pd.read_pickle('201704health.pickle')
print(df2)

print('combine column direction.')
#caition: if index of each dataframes is different, concat is wrong.
print(pd.concat([df1, df2], axis=1))
print('')

print('combine row direction.')
print(pd.concat([df1, df2], axis=0))