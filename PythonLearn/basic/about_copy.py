#!python3
# -*- coding:utf-8 -*-
'''
    about_copy.py
        This source is for proving difference with shallow copy and deep copy.
'''
import copy

# if object haven't other object inbody, shallow and deep copy has no difference each other.
print('-- simply copy of one dimension list')
# shallow copy
a = [1, 2, 3]
b = copy.copy(a)
print(a is b)
# this is also shallow copy
b = a[:]
b = list(a)
b[1] = a[1]
print(a is b)

# if object have other object inbody, shallow copy isn't duplicate data that other object. deep copy is duplicate.
print('-- Have to attension shallow copy : complexly dimension list')
a = [1, 2, [9, 10]]

# shallow copy
b = copy.copy(a)
print(a is b)
print(a[2] is b[2])
print(a[2][0] is b[2][0])

# deep copy
print('-- deep copy : complexly dimension list')
b = copy.deepcopy(a)
print(a is b)
print(a[2] is b[2])
print(a[2][0] is b[2][0])

# つまりshallowの場合はコピー対象の一番上層しか複製しないが、
# deepの場合は最下層まで複製する、と考えればよいか。
