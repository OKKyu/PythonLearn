#!python3
# -*- coding:utf-8 -*-

#decorator is simply description that wrapping function with other function.
#below 2 code is same.


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
print(myFunc(3))

#2) no use decorator
def myFunc(x):
    return x ** 2
myFunc = debug_log(myFunc)

print(myFunc(3))

#wrapされた関数を機能拡張させる。
#クラスメソッドをオーバーライドしたような挙動になるが、
#・メソッド名が変わる
#・ラップされた関数の処理の前に拡張した処理が実行される。
#decoratorとなる関数は上記debug_logのように、拡張した関数を返却するように実装する。
#また同時に、拡張した関数の中で代入された関数を実行し返却させる。