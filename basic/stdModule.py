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
