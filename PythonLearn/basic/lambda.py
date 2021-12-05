#!python3
# -*- coding:utf-8 -*-
'''
  lambda.py
    Explaining what is lambda.
'''

# lambda is no-named function.
# define lambda. but this lambda isn't run.
print(lambda x, y: x * 2 + y)

# if define and run lamdba,
# 1) set varlable, and run.


def f(x, y):
    return x * 2 + y


print(f(1, 2))

# 2) wrapping lambda with (), and added args ended.
print((lambda x, y: x * 2 + y)(1, 2))
