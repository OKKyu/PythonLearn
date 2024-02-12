#!python3
# -*- coding:utf-8 -*-
import itertools

lis = [x for x in range(0, 10)]
for pair in itertools.combinations(lis, 3):
    print(pair)
