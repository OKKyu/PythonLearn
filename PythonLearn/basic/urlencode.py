#!python3

import urllib.parse as parse

a = parse.quote('あいうえお', encoding='utf-8')
print(a)

a = parse.unquote(a, encoding='utf-8')
print(a)
