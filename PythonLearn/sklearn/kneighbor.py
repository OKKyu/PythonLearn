#! python3
# -*- coding:utf-8 -*-

import sys
from sklearn.neighbors import KNeighborsClassifier
import pandas as pd
import matplotlib.pyplot as plt
from sklearn import metrics

base_dir = sys.argv[1]
dfTrain = pd.read_csv(base_dir + '/train.csv',index_col=0)
dfTrain = dfTrain.dropna()
dfData = dfTrain.drop(['Survived','Pclass','Name','Sex','Parch','Ticket','Fare','Cabin','Embarked'],axis=1)

knn = KNeighborsClassifier(n_neighbors=4)
knn.fit(dfData, dfTrain['Survived'])

dfTest =  pd.read_csv(base_dir + '/test.csv',index_col=0)
dfTest = dfTest.fillna(0)
dfTestData = dfTest.drop(['Pclass','Name','Sex','Parch','Ticket','Fare','Cabin','Embarked'],axis=1)

Y_pred = knn.predict(dfTestData)
print(len(Y_pred))

dfAnswer = pd.read_csv(base_dir + 'gender_submission.csv', index_col=0)
dfAnswer = dfAnswer.fillna(0)

# 精度確認用のライブラリの実行
print(metrics.accuracy_score(dfAnswer, Y_pred))    # 予測精度計測
print(metrics.classification_report(dfAnswer, Y_pred))