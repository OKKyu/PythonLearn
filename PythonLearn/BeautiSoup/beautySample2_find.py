#! python3
# -*- coding:utf-8 -*-
import requests
from bs4 import BeautifulSoup

r = requests.get('https://gihyo.jp/lifestyle/clip/01/everyday-cat')
soup = BeautifulSoup(r.content, 'html.parser')

div = soup.find('div', class_='readingContent01')  # 指定したクラスを持つdiv要素を取得。複数条件に合う場合は先頭の要素を取得する。
li = div.find('li')  # divタグの中の先頭のliタグを取得する。cssセレクタではなく、タグ名１個のみ指定可能。
print(type(li))  # bs4.element.tagが返却される。find_allの場合はtagのリストが返却される。
print(li.a['href'])  # liタグの中のaタグのhref属性値を取得する。
print(li.a.text)  # 文字、テキストノードを取得する
# つまりタグ名のツリー構造はピリオドでチェーンさせることができ、属性値は[]で指定する。
# しかし属性についてはエラー防止のためgetで取るほうがいい。

# basics tags class
type(div)
print(div.name)
print(div['class'])
print(div.attrs)
# print(div['id'])   存在しない属性名を参照しようとするとエラーになる。これは面倒くさい。
print(div.get('id'))  # 辞書のgetメソッドを使うと、存在しないキーの場合にNoneを返す。エラーにしたくない場合はこれを使う。
# キーの存在チェックとして 'id' in div という聞き方もある。
print(div.parent)  # chidlren,nextSibling mo aru
print(dir(div))
