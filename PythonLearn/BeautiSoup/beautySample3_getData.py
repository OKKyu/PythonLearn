#! python3
# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup

r = requests.get('https://gihyo.jp/lifestyle/clip/01/everyday-cat')
soup = BeautifulSoup(r.content, 'html.parser')

div = soup.find('div', class_='readingContent01')
for li in div.find_all('li'):  # divタグの中の全liタグを取得
    url = li.a['href']
    date,text = li.a.text.split(maxsplit=1)
    print('{},{},{}'.format(date,text,url))