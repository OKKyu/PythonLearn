#!python3
# -*- coding:utf-8 -*-

#decorator is simply description that wrapping function with other function.
#bellow 2 code is same.


#before, define wrapping function
def debug_log(func):
    def log_and_calc(x):
        print("debug!!")
        return func(x)
    return log_and_calc
    
#1) use decorator
@debug_log
def myFunc(x):
    return x ** 2

#2) no use decorator
def myFunc(x):
    return x ** 2
myFunc = debug_log(myFunc)

print(myFunc(3))

#デザインパターンのadapterだったっけ？みたいな処理をする。
#wrapされた関数を機能拡張させる。