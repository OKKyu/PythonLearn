#! python3
# -*- coding: utf-8 -*-
'''
  tuple.py
    Basics of tuple object.
'''

print('immutable非破壊なリスト。[] の代わりに () を使う。')
tuple1 = ('aa', 'bb')
print(tuple1)
print('リストとは異なり、append()やdelete()といった関数はない。')
print('また、要素が１個の場合でもカンマをつける必要がある。これは()が予約語と誤認されないようにするため。')

print(('cc',))
