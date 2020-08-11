#!python3
# -*- coding:utf-8 -*- 
import copy

#if object haven't other object inbody, shallow and deep copy has no difference each other.
#shallow copy
a = [1,2,3]
b = copy.copy(a)
print(a is b)
#this also shallow copy
b = a[:]
b = list(a)
b[1] = a[1]

#if object have other object inbody, shallow copy isn't duplicate data that other object. deep copy is duplicate.
a = [1,2,[9,10]]

#shallow copy
b = copy.copy(a)
print(a is b)
print(a[2] is b[2])
print(a[2][0] is b[2][0])

#deep copy
b = copy.deepcopy(a)
print(a is b)
print(a[2] is b[2])
print(a[2][0] is b[2][0])

#つまりshallowの場合はコピー対象の一番上層しか複製しないが、
#deepの場合は最下層まで複製する、と考えればよいか。
