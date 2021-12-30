#! python3
# -*- coding:utf-8 -*-
import requests
from bs4 import BeautifulSoup

'''
  参考サイト
  http://kondou.com/BS4/#contents-children
'''

r = requests.get('https://gihyo.jp/lifestyle/clip/01/everyday-cat')
soup = BeautifulSoup(r.content, 'html.parser')

# findによる検索
div = soup.find('div', class_='readingContent01')  # 指定したクラスを持つdiv要素を取得。複数条件に合う場合は先頭の要素を取得する。
li = div.find('li')  # divタグの中の先頭のliタグを取得する。cssセレクタではなく、タグ名１個のみ指定可能。
print(type(li))  # bs4.element.tagが返却される。find_allの場合はtagのリストが返却される。

# タグ名による探索
# 直下のタグはタグ名の変数に格納されている。
print(li.a['href'])  # liタグの中のaタグのhref属性値を取得する。
print(li.a.text)  # 文字、テキストノードを取得する
# つまりタグ名のツリー構造はピリオドでチェーンさせることができ、属性値は[]で指定する。
# しかしピリオドで指定したタグがなかったり、属性値がなかったりするとエラーで止まる。
# タグはfindなどで検索し、属性値はgetで検索し、値がない場合に処理分岐させるほうがセーフティ。

# tagクラスの基本的な変数およびメソッド
print('basics variables and methods.----------')
print('div.name:' + div.name)
print('div.classes:' + ''.join(div['class']))
print('div.attrs:' + ''.join([k + ',' + ",".join(v) for k, v in div.attrs.items()]))

# print(div['id'])   存在しない属性名を参照しようとするとエラーになる。これは面倒くさい。
# キーの存在チェックとして 'id' in div という聞き方もある。
print('get single attribute(id):' + str(div.get('id')))  # 辞書のgetメソッドを使うと、存在しないキーの場合にNoneを返す。エラーにしたくない場合はこれを使う。
print('div.parent:name ' + div.parent.name + " classes " + ''.join(div.parent['class']))
print('div.parents: len' + str(len(list(div.parents))))  # 祖先要素
print('div.contents: len' + str(len(list(div.contents))))  # 子要素 タグのリストが返ってくる
print('div.children: len' + str(len(list(div.children))))  # 子要素 こちらはイテレーター
print('div.descendants: len' + str(len(list(div.descendants))))  # 子孫要素
# string は使いづらい。子要素がStringオブジェクト１個のみの場合、あるいは子要素がタグだけどそのタグ内にStringオブジェクト
# １個しかない場合に、文字列のみを返す。それ以外はnone
#print('div.string:' + div.string)
# strings, stripped_stringsは子要素、子孫要素が持つ全ての文字列を返す。
# strippedは余計な改行文字やスペースを除去する。こっちが見やすい。
print('div.strings:' + ''.join(div.strings))
print('-' * 30)
print('div.stripped_strings:')
for s in div.stripped_strings:
    print(s)
print('-' * 30)

# 兄弟要素
print('div.nextsibling:' + str(div.next_sibling))  # next_siblingsもある
print('div.previous_sibling:' + str(div.previous_sibling))  # previous_siblingsもある

# 上下移動
print('div.next_element:' + str(div.next_element))  # next_elements
print('div.previous_element:' + str(div.previous_element))  # previous_elements
