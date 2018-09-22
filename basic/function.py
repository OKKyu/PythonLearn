#! python3
# -*- coding: utf-8 -*-
import sys

#関数の基本
# def 関数名( [引数...] ) :
#      インデントして処理内容を記載してゆく
def initlog(args):
	print("input:" + sys.argv[0])

#引数にデフォルト値の指定が可能。
#また、デフォルト値が指定された引数はJavaScriptのように入力を省略できる。
def ask_ok(prompt, retries=4, reminder='Please try again!'):
    while True:
        ok = input(prompt)
        if ok in ('y', 'ye', 'yes'):
            return True
        if ok in ('n', 'no', 'nop', 'nope'):
            return False
        retries = retries - 1
        if retries < 0:
            raise ValueError('invalid user response')
        print(reminder)

#重要　スコープについて
#JavaScriptに近い仕組みとなっている。
#関数を定義すると、その関数内部のローカル変数用の領域（シンボルテーブル）が確保される。
#関数内部でローカル変数を参照すると、まず関数自身が持つシンボルテーブルを参照し、そこに
#なければ関数の一つ外の関数のシンボルテーブルを参照する。なければ更に外側の関数を参照・・・と
#繰り返し、最終的にはグローバル領域のシンボルテーブルを参照する。(グローバルの後に組み込みの名前テーブルを参照とある？）
#何もしなければ、外部の変数は参照しかできない。



