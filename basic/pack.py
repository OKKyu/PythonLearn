#! python3
# -*- coding: utf-8 -*-
# package参照のサンプル

# パッケージの完全修飾名インポート
import packageSample.sample1
# 利用時にも完全修飾名で指定する必要がある
packageSample.sample1.method1("完全修飾名で実行(packageSample.sample1.method1)：")

# 常に完全修飾名で指定するのはしんどい。
# from パッケージ名 import item でやると、item名のみで参照可能となる。as句も使える。
from packageSample import sample1 as sam1
sam1.method1("モジュール名で実行(sample1.method1)：", val1=4)

# item にはサブモジュール（フォルダ）名までを指定しても良いし、変数、関数名まで指定することも可能。
from packageSample.sample1 import method1
method1("関数名で実行(method1)：",val2=3)

# 以下のようにワイルドカードを使うと、fromで指定したモジュール内にあるitemをすべて参照する。
# ただし、モジュール内の__init__.pyの__all__リストがある場合、__all__リストに指定されたモジュールのみがインポートされる。
from packageSample import *
# sample1は__all__リストにあるためすべてのitemがインポートされる。
sample1.method2()
sample1.method3()
# sample2は__all__リストにあるためすべてのitemがインポートされる。
sample2.method()
# sample3は__all__リストにないためインポートされない。コメントを外すとエラーになる。
#sample3.method()

# 以下は内部参照のテスト。詳細はsample4.pyを参照されたし。
from packageSample.subpack1 import sample4 as sam4
sam4.callSample2()
sam4.callSample3()
