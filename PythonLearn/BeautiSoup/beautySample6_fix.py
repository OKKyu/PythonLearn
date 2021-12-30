#!python3
# -*- coding:utf-8 -*-
import requests
from bs4 import BeautifulSoup

r = requests.get('https://gihyo.jp/lifestyle/clip/01/everyday-cat')
soup = BeautifulSoup(r.content, 'html.parser')

# BeautifulSoupは取得した情報の編集機能も持っている。jQueryが持っているメソッドはほぼある。
# tag.string = "XXXX"   文字列は直接代入して直せる。
# append(), insert, insert_before, insert_after, wrap, unwrap, extract, etc...

