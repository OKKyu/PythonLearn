#! python3
# -*- coding: utf-8 -*-

import requests
from bs4 import BeautifulSoup

r = requests.get('http://gihyo.jp/lifestyle/clip/01/everyday-cat')
soup = BeautifulSoup(r.content,'html.parser')

#beautifulSoup can also css selector.
a_tags = soup.select('body a')
print(len(a_tags))

a_tags = soup.select(' p > a')
for tag in a_tags:
    print('{},{},{}'.format(tag.get('id') , tag.get('name'), tag.get('class')))