# -*- coding:utf-8 -*-
import requests
from bs4 import BeautifulSoup

import re #正規表現ライブラリ

r = requests.get('http://gihyo.jp/lifestyle/clip/01/everyday-cat')
soup = BeautifulSoup(r.content, 'html.parser')

a_tags = soup.find_all('a') #該当タグを全て検索
print(len(a_tags))

#正規表現も使える。先頭文字がbで始まるタグを検索。
for tag in soup.find_all(re.compile('^b')):
    print(tag.name)

#リストで複数条件を指定可能。
for tag in soup.find_all(['html','head']):
    print('{}'.format(tag.name))