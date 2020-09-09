#!python3
# -*- coding:utf-8 -*-

'''
  scikit-learnによる決定木の実行
  決定木：複数ある特徴量のうちいくつかを選択し、しきい値以上か未満かによってデータを
          ２グループに分割する。分割された単位をノードという。分割生成されたノードに
          対して更に同様の処理を繰り返し行う。深さはハイパーパラメータで設定可能。
          疑問１：複数ある特徴量のうちどれから先に使うのか？
          疑問２：しきい値はどのようにして決めているのか？
          疑問３：決定木をもとに予測する時にはどのような判定ロジックが流れているのか？
        　疑問４：精度を向上させるために行うべき取り組みを、予測結果から推測できるのか？
                  画像認識のニューラルネットワークであれば学習データの追加、推測に失敗した
                  データと成功したデータの比較分析などが思い浮かぶ。決定木も似たようなものか。
        　
'''

import math
import numpy as np
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
#GraphVizによって決定木を可視化するツール
from pydotplus import graph_from_dot_data
from sklearn.tree import export_graphviz
from sklearn.metrics import classification_report

#テストデータ読み込み
iris = load_iris()
x_train, x_test, y_train, y_test = train_test_split(iris.data, iris.target, test_size=0.3, random_state=123)

#決定木をインスタンス化する 決定木の最大の深さを3にしている
tree = DecisionTreeClassifier(max_depth=3)

#学習
#ランダムフォレストと異なり特徴量の自動選出はされないはず。どうやって順番を決めているのか。
tree.fit(x_train, y_train)

#出力
dot_data = export_graphviz(tree, filled=True,
                           rounded=True,
                           #class_names= iris.target_names,
                           class_names= ['Setosa', 'Versicolor', 'Virginica'],
                           #feature_names= iris.feature_names,
                           feature_names= ['Sepal Length', 'Sepal Wigth', 'Petal Length', 'Petal Width'],
                           out_file=None)
#プロット出力
graph = graph_from_dot_data(dot_data)
graph.write_png('tree.png')

#予測
y_pred = tree.predict(x_test)
cnt_correct = np.count_nonzero((y_pred == y_test))
per_correct = cnt_correct / len(y_test)

#結果を表示
print("test data num:" + str(len(x_test)))
print("predict correct num:" + str(cnt_correct))
print("predict wrong num:" + str(len(x_test) - cnt_correct))
print("per of correct is :" + "{:1.2f}".format(per_correct))

#成績表示
print(classification_report(y_test, y_pred))