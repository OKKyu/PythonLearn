#! python3
# -*- coding:utf-8 -*-

import math
#simple format.
print('{} and {}'.format('aa', 'bb'))

#Indicating by index of args.
print('{1} and {0}'.format('aa', 'bb'))

#Indicating format with each values.
print('{:5.2f} and {:f}'.format(123.1, 123.1))

#Indicating by keywrods.
print('{neipia:1.4f} and {pi:1.2f}'.format(pi=math.pi, neipia=math.e))