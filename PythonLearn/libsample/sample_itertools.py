#!python3
# -*- coding:utf-8 -*-

import itertools

lis = [1, 2, 3, 4]
for pair in itertools.combinations(lis, 2):
    print(pair)
