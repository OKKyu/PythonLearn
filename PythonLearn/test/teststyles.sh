#!/bin/sh
# pip install pyflakes
# pip install pep8 x
# pip install pycodestyle o
# pip install pylint

# pep8 renamed by pycodestyle.
# pep8 test_target.py
# pycodestyle:PEP8のコーディングスタイルとの整合性を確認する
# 主に改行の仕方やインデント、コメントブロックの付け方など、書式フォーマットに関するチェックが行われる。
echo " ---- start pycodestyle (old name is pep8) ---- "
pycodestyle $1
echo " ----- end pycodestyle  ----- "
# 他の使用方法 カレントディレクトリ以下をチェックする場合
# pycodestyle --statistics -qq . 
# --show-source  : 該当箇所のソースコードも表示する --statisticsとは併用できない模様。
# --show-pep8 o  : 修正例を表示する                --statisticsとは併用できない模様。
# --ignore=E226,E302,E41 : 指定したエラーコードの警告は無視する
# 設定ファイル
#  --config=ファイルの場所、名前  とすることでプロジェクト固有の設定ファイルを格納できる。
#   設定ファイルの内容
#    [pep8]
#      ignore = E226,E302,E41
#      max-line-length = 160


# pyflakes:文法エラー（論理エラー）のチェックを行う。スタイルチェックはしない。
# なんとオプションがhelpとversionしかない。代わりにflake8を使うとのこと。
# 別途取り扱う。
echo " ---- start pyflakes  ---- "
pyflakes $1
echo " ----- end pyflakes ----- "
# 


# pyflakes:文法エラー（論理エラー）とコーディングスタイルのチェックを行う。
# pycodestyleとは異なるスタイル基準でチェックする。よってpycodestyleで警告ゼロになってもpylintでは引っかかることはある。
# docstringの有無チェックなど。また、文法エラーにかかるとスタイルチェックが抑制される。文法エラーを解消するとスタイルチェック
# が実行されるようである。
echo " ---- start pylint  ---- "
pylint $1
echo " ----- end pylint ----- "
