#!python3
# -*- coding:utf-8 -*-

'''
 this code about unicode encoding and decoding.
'''

#from str to unicode espace
print('from str to unicode espace')
s = 'あいうえお'
b = s.encode('unicode-escape')
print("before encode: " + s)
print("after encode:" + str(b))
print(type(b))

#from unicode escape to str
print('from unicode espace to str')
s_from_b = b.decode('unicode-escape')
print("after encode:" + s_from_b)
print(type(s_from_b))