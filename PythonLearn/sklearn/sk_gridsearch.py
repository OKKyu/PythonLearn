#!python3
# -*- coding:utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import classification_report

#お決まりのトイデータ読み込み
iris = load_iris()
x_train, x_test, y_train, y_test = train_test_split(iris.data, iris.target, test_size=0.3, random_state=123)

#決定木のインスタンス化
dtc = DecisionTreeClassifier()

#グリッドサーチのパラメータを設定。
#ここでは決定木用のハイパーパラメータを設定しているのみという点に注意。
param_grid = {'max_depth':[3, 4, 5]}

#10分割の交差検証を行う。
#第一引数には決定木を、第二引数にはハイパーパラメータを代入する。
#決定木の深さが3,4,5の３通りをテストする。
#あくまでここで設定した３通りしか確かめない点に注意。
cv = GridSearchCV(dtc, param_grid=param_grid, cv=10)
cv.fit(x_train, y_train)

#学習結果
#最適と判定されたハイパーパラメータを表示する
print("best parameter :" + str(cv.best_params_))
#最適と判定されたモデルを表示する
print("best parameter :" + str(cv.best_estimator_))

#学習モデルによって推測する方法は今までと同じ。
y_pred = cv.predict(x_test)

#成績表示
print(classification_report(y_test, y_pred))