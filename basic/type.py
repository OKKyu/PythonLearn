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

#string型代入  エスケープには\を使う。
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
#左から1～4文字切り出し
print('index 1 4  ' + text[0] + text[1] + text[2] + text[3])

#右から1～4文字切り出し
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


