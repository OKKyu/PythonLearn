#! python3
# -*- coding: utf-8 -*-
# モジュールインポート色々

#fiboファイルを読み込む。fiboにはfib,fib2関数が定義されている。
import fibo
fibo.fib(100)
fibo.fib2(100)

#fibo内で定義されているfib,fib2をインポートする。
#それぞれfib,fib2という名前で読み込まれる。
from fibo import fib,fib2
fib(100)
fib2(100)

#fibo内の関数をすべて読み込む方法もある。
#ただし何をインポートしたかが読み取りにくいため推奨されない。
#可読性が落ちるし、すでに定義済みの同名モジュールを誤って上書きする危険性がある。
#from fibo import *

#as句で別名をつけることも可能。
import fibo as fibonacchi
fibonacchi.fib(100)

#モジュールをスクリプト化することも可能。以下を追加することでスクリプト化する。
#以下if文内の処理がスクリプトとして実行された場合のみ動作するようになる。
if __name__ == "__main__" :
	import sys
	fib(int(58))
