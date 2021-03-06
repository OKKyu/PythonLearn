#! python3
# -*- coding: utf-8 -*-
import sys
#dir()関数でモジュールが定義している名前を参照できる。
#変数名、モジュール名、関数名、その他すべての名前を返す。
#dirはソートされた文字列のリストを返却する。

#以下はsysモジュール内で定義されている名前を表示する。
dir(sys)

#引数がない場合、現在定義されている名前を返す。
dir()

#オブジェクトが持つメンバの一覧を表示する方法
for x in dir(sys):
    print(x)