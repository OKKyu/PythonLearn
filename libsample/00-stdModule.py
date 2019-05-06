#! python3
# -*- coding: utf-8 -*-
#pythonは標準モジュールライブラリを同梱している。
#sysモジュールはすべてのpythonインタープリタにビルトインされている。
#OS機能に依存しているモジュールもある。

import sys

#sys.path
# 変数 sys.path は文字列からなるリストで、インタプリタがモジュールを検索するときのパスを決定します。
# sys.path は環境変数 PYTHONPATH から得たデフォルトパスに、 PYTHONPATH が設定されていなければ
# 組み込みのデフォルト値に設定されます。標準的なリスト操作で変更することができます:

#標準的なリスト操作で変更も可能。
sys.path.append('/home/puppy/PythonLearning')

for i, item in enumerate(sys.path):
    print(str(i) + " : " + item)


#re 正規表現
#datetime 日付と時刻
#collections 組み込み以外のコレクション型
#math 数学関数
#random 疑似乱数
#itertools 反復可能オブジェクトへの操作
#sqlite3 SQLiteデータベースの操作
#csv CSV読み書き
#json JSONの読み書き
#os OS関連操作
#multiprocessing マルチプロセス操作
#subprocess 他プロセスの実行
#urllib  URL関連操作
#unittest ユニットテスト
#pdb  pythonのデバッガ
#sys  Pythonインタプリター関連の変数や関数