#! python3
# -*- coding:utf-8 -*-
from sklearn.neighbors import KNeighborsClassifier
import pandas as pd
import matplotlib.pyplot as plt

fpath = '/home/puppy/Downloads/kaggle/Titanic/'
dfTrain = pd.read_csv(fpath + '/train.csv',index_col=0)
dfTrain = dfTrain.dropna()
dfData = dfTrain.drop(['Survived','Pclass','Name','Sex','Parch','Ticket','Fare','Cabin','Embarked'],axis=1)

knn = KNeighborsClassifier(n_neighbors=4)
knn.fit(dfData, dfTrain['Survived'])

dfTest =  pd.read_csv(fpath + '/test.csv',index_col=0)
dfTest = dfTest.fillna(0)
dfTestData = dfTest.drop(['Pclass','Name','Sex','Parch','Ticket','Fare','Cabin','Embarked'],axis=1)

Y_pred = knn.predict(dfTestData)
print(len(Y_pred))
print(Y_pred)
# 精度確認用のライブラリインポートと実行
#from sklearn import metrics
#metrics.accuracy_score(Y_test, Y_pred)    # 予測精度計測