#!python3

import urllib.parse as parse

print('from string to urlencode')
a = parse.quote('あいうえお', encoding='utf-8')
print(a)

print('from urlencode to string')
a = parse.unquote(a, encoding='utf-8')
print(a)
