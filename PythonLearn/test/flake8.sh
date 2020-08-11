#!/bin/sh
# pip install flake8

# flake8:pep8スタイルチェックとpyflakesの論理エラーチェックを行う。
# また循環的複雑度もチェックする。

echo " ---- start flake8  ---- "
flake8 $1
echo " ----- end flake8 ----- "

# エラーの種類
#    E***/W***: pep8 のエラー及び警告。
#    F***: PyFlakes の検知。
#    C9**: McCabeによる循環的複雑度の検知。
# hackingをインストールするとH***系エラーも追加される。
# カスタマイズもできるらしい。


