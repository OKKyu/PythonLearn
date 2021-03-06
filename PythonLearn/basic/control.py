#! python3
# -*- coding: utf-8 -*-
'''
  control.py
    This code is sample of control syntax.
'''

import sys

# print('if文の例')
if len(sys.argv) == 2:
    print('hello,' + sys.argv[1])
elif len(sys.argv) == 3:
    print('Danke!,' + sys.argv[1] + ' und ' + sys.argv[2])
elif len(sys.argv) == 4:
    print('CheyChey,' + sys.argv[3])
else:
    print('........')

# 条件式にはand,or,notが使える。

# print('for文の例')
# 要素を順番どおりに出力する
words = ['cat', 'window', 'defensestrate']
for w in words:
    print(w, len(w))

# print('ループ内部でリストを修正する例　スライスで複製したものをループさせると、無限ループを防げる')
# うっかり 'in words' とスライスを付け忘れると、insertによって要素数が増える→増えた分をループ処理する→また条件を満たすので
# ループする...といった具合に無限ループする。
for w in words[:]:
    if len(w) > 6:
        words.insert(0, w)
print(words)

# range()
# pythonではfor文を回数分実行する際にrange()を使う。以下は0〜4インデックスの計5回の処理を行う。
for i in range(5):
    print(i)

# 範囲指定も可能。
for i in range(5, 10):
    print(i)

# 第三引数に増加量を指定できる。
for i in range(0, 10, 3):
    print(i)

# マイナスも可能。
for i in range(-10, -20, -1):
    print(i)

# インデックスで繰り返し処理をする場合はlenを組み合わせる。
a = ['Mary', 'had', 'a', 'little', 'lamb']
for i in range(len(a)):
    print(i, a[i])
print("")

# for、while文にelse文をもたせることができる。
# in句内の要素が１個もなくループが１度も回らないときに実行される。
# ループが終了したときに１回のみ実行される。breakされたときには実行されない。
for n in range(2, 10):
    for x in range(2, n):
        if n % x == 0:
            print(n, 'equals', x, '*', n // x)
            break
    else:
        # loop fell through without finding a factor
        print(n, 'is a prime number')

# pass文 処理行の記述を構文上求められるが、なんの動作も必要がない（させない）場合に使う。
if True:
    pass

# 補足：条件式が偽となる値
# None, False, 整数のゼロ(0, 0.0, 0.0j), 空文字列, 空リスト,タプル,辞書
# 上記以外は真

# pythonにはcase文がない。if文が面倒な場合、dictのkeyに条件文字、valに関数を入れることで擬似的にcase文が作れる。
# ただしdefault句の代わりがない。以下Noneの代わりにdefaultの関数を入れるとよいか。

# 関数の定義


def bb():
    print("BB")


# 関数をvalueとして代入する。lambdaも関数なのでセットできる。
case = {"aa": lambda x: print(x),
        "bb": bb
        }
# aaの場合の処理を実行する。ただgetしただけでは関数が返却されるだけなので、関数を実行するために()を書く。
case.get("aa")(12321)
case.get("bb")()
case.get("cc", None)
