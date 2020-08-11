#! python3
# -*- coding:utf-8 -*-
#pandas is preprocessing library for data.
#データの入力
#データの並び替え
#データの修正
#CSVのエクスポート
#簡易的な描画などができます。
#Pandasを利用する場合は、
#    データ量が多い
#    外部サービスとのデータの連携が多い
#    複数のデータセットを扱う必要がある
#という場合には、非常に重宝します。

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

#read_csv
fpath = '/home/puppy/Downloads/kaggle/Titanic/'
df = pd.read_csv(fpath + '/gender_submission.csv',index_col=0)
#other pandas can read below.
#clipboard, google bigquery, excel (can other spreadsheet?), html, json, sql ,etc...

#convert from python's list to Dataframe
import pandas as pd
from sklearn.datasets import load_boston
boston = load_boston()
dfx = pd.DataFrame(boston.data, columns=boston.feature_names)

#read from first data to next 10 data. same as head of linux command.
df.head(10)

#read from last data to back 10 data. same as tail of linux command.
df.tail(10)

#display static infomations.
df.describe()

#display number of variable and infomation.
df.info()

#display column names,types
df.columns
df.dtypes

#bind two csv
df2 = pd.read_csv(fpath + '/gender_submission.csv',index_col=0)
df3 = pd.concat([df,df2])

#sort 
df.sort_values(by=["Survived"], ascending=False)


#matplotlib inital setting
fig, ax = plt.subplots()
fig.set_size_inches(11.7, 8.27)

#histgram
sns.distplot(df.Age,kde = True).set_title('タイトル') #列名Seriesを引数に。
plt.show()

df['Age'].hist(bins=10)
plt.show()

df.hist(column='Age', bins=10)
plt.show()

df['Age'].hist(by=df['Sex'])
plt.show()


#hakohige figure
sns.boxplot(x=df["列名"])
plt.show()

#stick figure
sns.countplot(x=df["列名"]).set_title("タイトル名")
plt.show()

#scatter figure
pg = sns.pairplot(df.dropna()) #NaNの削除
plt.show()

#non seaborn scatter figure
df.plot.scatter(x='Age', y='Survived')

#relative between each variables
df.corr()