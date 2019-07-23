#! python3
# -*- coding:utf-8 -*-
# regular expression sample

import re

#first arguments is pattern. 2nd is target string.
#if matches, return match object about that first position.
m = re.search('def', 'abcdef')
print(m.group(0))

#re.sub（正規表現, “置換する文字列”, 置換対象の文字列）
print(re.sub("a","b","abds"))