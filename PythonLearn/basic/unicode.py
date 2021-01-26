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

#-- base64 --
import base64

a = base64.b64encode(s.encode('utf-8'))
print('from str to unicode, base64')
print(a)

a = base64.b64decode(a)
a = a.decode('utf-8')
print('from base64 to unicode, str')
print(a)