#!python3
# -*- coding:utf-8 -*-
import requests
from bs4 import BeautifulSoup

import re  # 正規表現ライブラリ

r = requests.get('https://gihyo.jp/lifestyle/clip/01/everyday-cat')
soup = BeautifulSoup(r.content, 'html.parser')

a_tags = soup.find_all('a')  # 該当タグを全て検索
print(len(a_tags))

# 正規表現も使える。先頭文字がbで始まるタグを検索。
print("re.compile(\^b):")
for tag in soup.find_all(re.compile('^b')):
    print(tag.name)

# リストで複数条件を指定可能。
print("html,head tag:")
for tag in soup.find_all(['html', 'head']):
    print('{}'.format(tag.name))

# クラス名で検索も可能。recursive=Falseで孫以下を検索しないようにすることも可。
print("div[class=XXX]:")
for tag in soup.find_all('div', class_='readingContent01', recursive=False):
    print(tag)

# キーワード引数で属性の１つを指定することも可能。キーワード引数は複数渡すことも可能。
# 以下は正規表現に合致するhref属性を持つ要素を検索する。
print("[href^=cat]:")
for tag in soup.find_all(href=re.compile('^cat')):
    print(tag)

# テキストを持つタグも検索可能。
print("a::text= [X1,X2...]:")
for tag in soup.find_all(text=["DNA", "隠し撮り"]):
    print(tag.string)


# 他にも以下がある。以下はどれも正規表現、リストによる複数指定、limit、recursiveが使える。
# find_parents() / find_parent()
#find_next_siblings() / find_next_sibling()
#find_previous_siblings() / find_previous_sibling()
#find_all_next() / find_next()
#find_all_previous() / find_previous()
