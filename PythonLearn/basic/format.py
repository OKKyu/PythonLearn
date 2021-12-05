#! python3
# -*- coding:utf-8 -*-
'''
  format.py
    How to control displaying format.
'''

import math
# simple format.
print('{} and {}'.format('aa', 'bb'))

# Indicating by index of args.
print('{1} and {0}'.format('aa', 'bb'))

# Indicating format with each values.
print('{:5.2f} and {:f}'.format(123.1, 123.1))

# Indicating by keywrods.
print('{neipia:1.4f} and {pi:1.2f}'.format(pi=math.pi, neipia=math.e))

# "format" method can convert from int to str.
# If it is gaved 2nd arguments in b,o,or x, it displayed as byte, octet, or hex.
i = 255
print(format(i, 'b'))
print(format(i, 'o'))
print(format(i, 'x'))
print(type(format(i, 'b')))
print(type(format(i, 'o')))
print(type(format(i, 'x')))
print(format(i, '#010b'))
print(format(i, '#010o'))
print(format(i, '#010x'))
