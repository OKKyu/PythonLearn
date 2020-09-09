#! python3
# -*- coding:utf-8 -*-

from sklearn.datasets import load_digits
from sklearn.neural_network import MLPClassifier
from sklearn.externals import joblib

#load training data
digits = load_digits()
clf = MLPClassifier(hidden_layer_sizes=(100,), max_iter=1000, tol=0.000001, random_state=None)
print(digits.DESCR)
#fit learning model
print(digits.data)
print(digits.target)

clf.fit(digits.data, digits.target)
pre1 = clf.predict(digits.data)

#save learning instance to serialze object
savePath = './'
fname = 'test.joblib'

# joblibを使ってオブジェクトをダンプ
joblib.dump(clf, savePath + fname)

# joblibを使ってオブジェクトをロード
clf2 = joblib.load(savePath + fname)
pre2 = clf2.predict(digits.data)

# pre1とpre2は同じ結果が出るはず（X_trainが同じ値なら）
print('pre1 length ' + str(len(pre1)))
print('pre2 length ' + str(len(pre2)))
print('pre1 content')
print(pre1)
print('pre2 content')
print(pre2)
pre2[0] = 99
print('Match rate ' + str(len(pre2[pre1==pre2]) / len(pre1)) )
