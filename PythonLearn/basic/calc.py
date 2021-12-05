#! python3
# -*- coding: UTF-8 -*-
# 四則演算の基本
'''
    calc.py
    Sample Code that basic of calculation on python.
'''
import sys

# 四則演算はJavaやJavaScriptと同じ。
# 割り算をすると返却値は小数点となる。
print("1+2 " + str(1 + 2))
print("3-1 " + str(3 - 1))
print("6*5 " + str(6 * 5))
print("6/2 " + str(6 / 2))
print("6%5 " + str(6 % 5))

# pythonでは小数点以下を切り捨て除算をする場合は//を使う。
print("6//2 " + str(6 // 2))

# pythonでは累乗計算を**を使って計算できる。以下は6の2乗
print("6**2 " + str(6**2))

# 等号 = は変数への値代入。
# また、変数は型を宣言しないでよい。自動で型が決定されている。
width = 55
height = 20
print("width = 55")
print("height = 20")
print("width * height " + str(width * height))

# 値を代入しない変数の宣言は不可能。
# 以下コメントアウトを外すと"name not defined"例外が発生する。
# name

# 対話モード限定
# 最後に表示された結果は変数 _ に代入される。
