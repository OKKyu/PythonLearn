#! python3
# -*- coding: UTF-8 -*-
# 型の基本
import sys

#intとfloat、Decimal、Fractionなどをサポート。ビルトインでは複素数や虚数も扱える。j or Jで虚部を示す。
#int型代入
num = 30
print("num(int) " + str(num))

#float型代入
num = 30.6
print("num(float)" + str(num))

#int型代入
num = 22
print("num(int)" + str(num))

#string型代入  JavaScriptのように、変数の型は固定されないようである。
num = "121"
print("num(String)" + str(num))

#string型代入  エスケープには¥を使う。
st = '"Isn\'t," she said.'
print("st " + st)

#長い文字列の連結 () でくくり、任意の位置で複数のクォーテーションを使う。
text = ('very long,long,long,long,long,long,long,long,long'
        ',long,long,long,long,long,long,time,agooooooo.......')
print(text)

#変数どうしの連結 Javaと同じく + を使う。
text = text + 'very Evils man, Rorun Harlshead, is exist.'
print(text)

#文字列はインデックス指定して一部切り出しも可能。
#charに変換しないでいいし、substringも要らなさそう。これはお手軽。
#左から1〜4文字切り出し
print('index 1 4  ' + text[0] + text[1] + text[2] + text[3])

#右から1〜4文字切り出し
#-0はないため、右から切り出す場合は1開始となる。
print("index -1 -4  " + text[-1] + text[-2] + text[-3] + text[-4])

#上のような切り出し方をせずともスライスもサポートされている。
print('index 1 4  ' + text[0:4])

#最初のインデックスを省略すると、0 と見なされます。二番め のインデックスを省略すると、スライスする文字列のサイズとみなされます。
text = 'Python'
print("text :2" + text[:2])
print("text 2:" + text[2:])

#文字列はimmutable。一部文字列を変更しようとしてもエラーとなる。
#text[:2] = 'Po'

#文字列長はlen()で取得可能。
print('length:' + str(len(text)))

print('文字列のformat関数で{インデックス}の置換ができる。')
print('{0},Python{1}!'.format('Hello',sys.version))

print('これは便利。文字列の部分一致が簡単に調べられる。ただし真偽値で結果を返す。')
print(' 探したい文字 in 対象文字列')
print('お' in 'あいうえお')

print('split関数あり。')
print('あいうえ,おかき'.split(','))

print('splitの逆でjoin関数というのがある。指定した区切り文字で文字列を連結する。リストの要素を１個の文字列に連結したいときに使える。')
print('-'.join(['あいうえ','おかき']))

print('文字列置換、replaceもある。')
print('あいうえ-おかき'.replace('-',''))

#型判定の方法。
#組み込み関数typeとisinstanceがある。
#typeの場合
print(type('string'))
# <class 'str'>と出る

print(type(100))
# <class 'int'>と出る

print(type([0, 1, 2]))
# <class 'list'>と出る

#type()の返り値と任意の型を比較することで、そのオブジェクトが任意の型であるかを判定できる。
print(type('string') is str)


#isinstanceの場合
#isinstance(object, class)は、第一引数のオブジェクトが、第二引数の型のインスタンス、またはサブクラスのインスタンスであればTrueを返す関数。
#typeではサブクラスまでは判定しない。
print(isinstance('string', str))

#第二引数には型のタプルを指定することも可能。いずれかの型のインスタンスであればTrueを返す。
#いちいち if ... instanceof ... or ... instanceof ... と繰り返さないでもできる。
print(isinstance(100, (int, str)))




