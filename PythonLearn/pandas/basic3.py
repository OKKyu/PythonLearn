#!python3
# -*- coding:utf-8 -*-

import numpy as np
import pandas as pd

'''
  This source code is a sample of using pandas library.
  Data maintenance about DataFrame.
'''

df = pd.read_excel('201704health.xlsx')
print('check that data is reading successfully')
print(df.head(4))
print("")

#Data filtering by conditions.
df_over10000 = df[df["歩数"] > 10000]
print("filtered 歩数 > 10000 data:")
print(df_over10000)
print("filtered 歩数 > 10000 shape:" + str(df_over10000.shape))
print("")

#Data filtering by query. This method can use like sql query.
df_filtered = df.query(' 歩数 >= 10000 and 摂取カロリー <= 1800 ')
print('filterd by query method. 歩数 >= 10000 and 摂取カロリー <= 1800 ')
print(df_filtered)
print("")

#convert dateString to date.
#By indicate new column name in loc, can add new column and
#apply(pd.to_datetime) has convert dateString to datetime type.
df.loc[:, 'date'] = df.loc[:, '日付'].apply(pd.to_datetime)
print('convert and add date column.')
print(df)
print(str(df.dtypes))
print("")

#Change column type.
df.loc[:, '摂取カロリー'] = df.loc[:,'摂取カロリー'].astype(np.float32)
print('change column type from int to float32.')
print(df['摂取カロリー'].head(4))
print("")

#setting index column.
df = df.set_index("date")
print('set index column.')
print(df.head(4))
print("")

#sorting data.
print('sort data, 歩数、カロリー')
print(df.sort_values(by=['歩数', '摂取カロリー'], ascending=False).head(10))
print("")

#remove unneccesary column
df = df.drop("日付", axis=1)
print(df.head(4))
print("")

#Insert new data column with calculated values.
df.loc[:, '歩数／カロリー'] = df.loc[:,'歩数'] / df.loc[:,'摂取カロリー']
print(df.loc[:, '歩数／カロリー'].head(4))
print("")

#apply by function.
def exercise_judge(ex):
    if ex <= 3.0:
        return "Low"
    elif 3.0 < ex <= 6.0:
        return "Mid"
    else:
        return "High"

df.loc[:, '運動指数'] = df.loc[:, '歩数／カロリー'].apply(exercise_judge)
print(df.head(4))
print("")

#One hot encoding:
df_moved = pd.get_dummies(df.loc[:, "運動指数"], prefix='運動指数')
print('One-hot encoding by 運動指数')
print(df_moved.head(6))

#save pickle.
df_moved.to_pickle('201704health.pickle')

#load dataframe from pickle file.
#df_loaded = pd.read_pickle('201704health.pickle')
