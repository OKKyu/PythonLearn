#! python3
# -*- coding: utf-8 -*-
'''
  function.py
    関数の基本
    def 関数名( [引数...] ) :
        インデントして処理内容を記載してゆく
'''


def initlog(args):
    print("input:" + sys.argv[0])

# 引数にデフォルト値の指定が可能。
# また、デフォルト値が指定された引数は入力を省略できる。
# デフォルト値のない引数は必須引数となる。何でも省略可能なJavaScriptとは少し違う。


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

# 重要　スコープについて
# JavaScriptに近い仕組みとなっている。
# 関数を定義すると、その関数内部のローカル変数用の領域（シンボルテーブル）が確保される。
# 関数内部でローカル変数を参照すると、まず関数自身が持つシンボルテーブルを参照し、そこに
# なければ関数の一つ外の関数のシンボルテーブルを参照する。なければ更に外側の関数を参照・・・と
# 繰り返し、最終的にはグローバル領域のシンボルテーブルを参照する。(グローバルの後に組み込みの名前テーブルを参照とある？）
# 何もしなければ、外部の変数は参照しかできない。


# 追記 グローバル変数は原則関数内では参照しかできない。
# 関数内でグローバル変数へ代入を行う場合には、global 変数名 で宣言してから行う。
message = "paiza"


def sum(x, y):
    a = 3
    global message
    message += "paiza"
    print(message + "hello" + str(a))
    return x + y


a = 10
b = 20
num = sum(a, b)
print(num)
print(message + "hello" + str(a))


# 重要
# 引数のデフォルト値は初回実行時にのみ初期化される。
# 引数のデフォルト値にリストなどを宣言している場合、関数を複数回呼び出すと前回実行時に保管されていたリストが使用される。
# 例えば以下はリストの要素が累積していく。
# デフォルト値の設定がない引数（以下の場合はa）については
# 関数呼び出しのたびに入力が必須のため、この問題は起きない。
def f(a, L=[]):
    L.append(a)
    return L


print(f(1))
print(f(2))
print(f(3))

# 後続の関数呼び出しでデフォルト値を共有したくない場合は以下のようにする。


def f(a, L=None):
    if L is None:
        L = []
    L.append(a)
    return L

# キーワード引数
# 関数の呼び出し時、引数名=value という形式でも呼び出し可能。


def parrot(voltage, state):
    print("voldage:" + voltage)
    print("state:" + state)


parrot("1000", "stable")
parrot(voltage="1000", state="stable")

# ただし以下はエラーとなる。
# parrot(voltage=5.0, 'dead')  # non-keyword argument after a keyword argument
# parrot(110, voltage=220)     # duplicate value for the same argument
# parrot(actor='John Cleese')  # unknown keyword argument

# 任意引数リスト
# 引数名に*をつけることでJavaでいうところの可変長引数...が使える。


def write_multiple_items(separator, *args):
    print(separator.join(args))


write_multiple_items("/", "alan", "kate", "ling")

# ただし、任意引数リストの後にはキーワード変数しか指定できない制約がある。
# 以下のように定義はできるが、


def write_multiple_items2(*args, separator):
    print(separator.join(args))


# 呼び出し時にseparatorをキーワード指定していないとエラーになる
# write_multiple_items2("/", "alan","kate","ling")
# 指定すると実行できる。
write_multiple_items2("alan", "kate", "ling", separator="/")

# 任意辞書リストもある。制約については任意引数リストと同じ。
# また、任意辞書リストは一番最後の引数としてのみ宣言できる。
# def write_multiple_items3(**words, *args, separator):  NG
# def write_multiple_items3(*args, **words, separator):  NG
# これはOK


def write_multiple_items3(*args, separator, **words):
    print(separator.join(args))
    for key, val in words.items():
        print(key + separator + val)


# wordsは省略可能
write_multiple_items3("alan", "kate", "ling", separator="/")
write_multiple_items3("alan", "kate", "ling", separator="/", aa="aaa", bb="bbb")

#


def write_multiple_items4(separator, *args, **words):
    print(separator.join(args))
    for key, val in words.items():
        print(key + separator + val)


#
write_multiple_items4("/", "alan", "kate", "ling", bb="bbb")

# 引数の宣言について
# 以下ルールを設けていればトラブルは減らせると思う。
#  1)初期値なし引数、初期値有り引数、任意引数リスト、任意辞書リストの順に宣言する
#  2)オブジェクトやシーケンスを受け取る引数の場合、極力初期値はNoneにしておく。
#    またチュートリアルのように、引数がNoneかどうかをチェックする。
#    *これは他引数でも同様のことが言える。pythonの引数は型が自由だから
#     必要なものがインプットされているか逐次チェックしたほうが良い。
