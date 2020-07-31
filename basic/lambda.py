#!python3
# -*- coding:utf-8 -*-

#lambda is no named function.
#define lambda. but this lambda is runned.
print(lambda x,y : x * 2 + y)

#if define and run lamdba,
# 1) set varlable, and run.
f = lambda x,y : x * 2 + y
print(f(1,2))

# 2) wrapping lambda with (), and added signature ended.
print( (lambda x,y : x * 2 + y) (1,2) )