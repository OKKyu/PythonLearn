#! python3
# -*- coding:utf-8 -*-
'''
  dict.py
    How to use dictionary object.
'''

# create empty dictionary
dict1 = {}

# create filled dictionary. pair of key and value.
dict1 = {'a': 12, 'b': 33, 'c': 42}

# you can use int,str, and other various type.
# andalso youcan use a kind of type data by  value.
dict_variable = {1: 'aiu', 2.23: True, 'nin': 12345}

# dictionary can return values as list like.
for k in dict1.keys():
    print('key names, ' + k)
for v in dict1.values():
    print('values, ' + str(v))
for k, v in dict1.items():
    print('key and values, ' + k + ':' + str(v))

# you can check by 'in' that dictionary contains a key or a value.
print('dict1 have key a ?, it\'s ' + str('a' in dict1))
print('dict1 have value 43 ?, it\'s ' + str(43 in dict1))

# get method
print('dict1 haven b, returned:' + str(dict1.get('b', 0)))
print('dict1 haven\'t dd, alternate value returned:' + str(dict1.get('dd', 0)))

# setdefault method
# if you want to add new key&value pair when dictionary have no key you want to add,
# you can use setdefault method.
dict1.setdefault('a', 21)
print(dict1['a'])
dict1.setdefault('ee', 343)
print(dict1['ee'])

# clear all elements.
dict1.clear()
print('clear dict1')
print(dict1)

# clear and return value by key.
dict1 = {'a': 12, 'ee': 300}
print('pop dict1 a')
print(dict1.pop('a'))
print('pop dict1 a')
print(dict1.pop('a', None))
print(dict1)

# clear and return key&value by key.
dict1 = {'a': 12, 'ee': 300}
print('popitem dict1')
print(dict1.popitem())
print(dict1)

# clear multi elements by keys.
dict1 = {'a': 12, 'ee': 300}
print('del dict1 a and ee')
del dict1['a'], dict1['ee']
print(dict1)

# 辞書内包表記
# リスト内包表記の辞書版。
# 1) zipでkeyとvalueを結合する方法
l1 = ["a", "b", "c"]
l2 = [i for i in range(3)]
dict2 = {k: v for k, v in zip(l1, l2)}
print(dict2)
# 2) zipなし
dict2 = {str(i): i for i in range(0, 8, 2)}
print(dict2)
