#! python3
# -*- coding: utf-8 -*-
'''
  This Sample Code refer to below website, BeautifulSoup Formal Homepage.
    http://kondou.com/BS4/#contents-children
'''
import requests
from bs4 import BeautifulSoup

r = requests.get('https://gihyo.jp/lifestyle/clip/01/everyday-cat')
soup = BeautifulSoup(r.content, 'html.parser')

# beautifulSoup can also use css selector.
a_tags = soup.select('body a')
print(len(a_tags))

a_tags = soup.select(' p > a')
for tag in a_tags:
    print('{},{},{}'.format(tag.get('id'), tag.get('name'), tag.get('class')))
