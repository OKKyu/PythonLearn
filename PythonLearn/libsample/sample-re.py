#! python3
# -*- coding:utf-8 -*-
# regular expression sample

import re

#1) search method only
#   first arguments is pattern. 2nd is target string.
#   if matches, return match object about that first position.
m = re.search('def', 'abcdef')
print(m.group(0))
#   range matched pattern in target string.
print("start index:" + str(m.start()) + " end index:" + str(m.end()))

#2) complie and search
#   first arguments is pattern.
cmp = re.compile('def')
#   you can search with cmp's search method instead of re's one.
m = cmp.search('abcdef')
print(m)

#   if no matched, search's result return None.
m = cmp.search('aaaaa')
print(m)

#3) grouping
cmp = re.compile(r'(\d\d\d)-(\d\d\d\d-\d\d\d\d)')
m = cmp.search('123-3322-1111')
print('phone number group matching...')
print(m.groups())
print(m.group(0))
print(m.group(1))
print(m.group(2))

#4) multi pattern
cmp = re.compile(r'Pokemon|Mario|Zelda')

gt = 'Super Mario Maker 2'
print(gt)
print('Game title classified is...')
m = cmp.search(gt)
print(m.group(0))

gt = 'Bress of the Wild (Legend of Zelda)'
print(gt)
print('Game title classified is...')
m = cmp.search(gt)
print(m.group(0))

#5) ninni matching
cmp = re.compile(r'Po(c)?ke(t )?Mon(ster)?')

gt = 'Pocket Monster Sword and Shield'
print('Game title is ...')
m = cmp.search(gt)
print(m.group(0))

gt = 'PokeMon Sword and Shield'
print('Game title is ...')
m = cmp.search(gt)
print(m.group(0))

#phone number matching
cmp = re.compile(r'^\d{3}-(\d{3,4}-\d{4})$|^(\d{3}-\d{4})$')
pn = '020-331-3334'
print(pn)
print(cmp.search(pn))
pn = '331-3334'
print(pn)
print(cmp.search(pn))
pn = '001-1234-3334'
print(pn)
print(cmp.search(pn))
pn = '4444-4444'
print(pn)
print(cmp.search(pn))

#6) findall
#   search returns only first matched str, findall returns all matched str by list object.
cmp = re.compile(r'\d{2}')
pn = '12a33'
print('search :' + cmp.search(pn).group(0))
print('findall :' + str(cmp.findall(pn)))

#7) How to replace matched str.
#re.sub（正規表現, “置換する文字列”, 置換対象の文字列）
print(re.sub("a","b","abds"))

