#! python3
# -*- coding:utf-8 -*-
# regular expression sample

import re

#first arguments is pattern. 2nd is target string.
#if matches, return match object about that first position.
m = re.search('def', 'abcdef')
m.group(0)
