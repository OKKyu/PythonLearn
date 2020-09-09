#!python3
# -*- coding:utf-8 -*-

'''
  scikit-learnによるランダムフォレストの実行
'''

import numpy as np
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
#GraphVizによって決定木を可視化するツール
from pydotplus import graph_from_dot_data
from sklearn.tree import export_graphviz

#テストデータ読み込み
iris = load_iris()
x_train, x_test, y_train, y_test = train_test_split(iris.data, iris.target, test_size=0.3, random_state=123)

#インスタンス作成
# n_estimators: 決定木の数
rf = RandomForestClassifier(n_estimators=100, random_state=123)

#学習
rf.fit(x_train, y_train)

#出力
#RandomForestの場合はn個決定木を持っているので、そのうち１つを選択すること。
dot_data = export_graphviz(rf.estimators_[0], filled=True,
                           rounded=True,
                           class_names= ['Setosa', 'Versicolor', 'Virginica'],
                           feature_names= ['Sepal Length', 'Sepal Wigth', 'Petal Length', 'Petal Width'],
                           out_file=None)
#プロット出力
graph = graph_from_dot_data(dot_data)
graph.write_png('randomforest.png')

#予測
y_pred = rf.predict(x_test)
cnt_correct = np.count_nonzero(y_pred == y_test)
per_correct = cnt_correct / len(y_test)

#結果を表示
print("test data num:" + str(len(x_test)))
print("predict correct num:" + str(cnt_correct))
print("predict wrong num:" + str(len(x_test) - cnt_correct))
print("per of correct is :" + "{:1.2f}".format(per_correct))
