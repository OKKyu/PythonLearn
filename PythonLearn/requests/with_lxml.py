#!python3
# -*- coding:utf-8 -*-
import requests
import lxml.html

#BeautifulSoupならリクエスト送信とcssセレクタによる抽出の両方ができるけど、
#requestsではリクエスト送信しかできない。
#よってrequestsの場合、htmlテキストをパースできるlxmlライブラリと併用するとよい。
response = requests.get('https://note.com')
#レスポンスのテキストを表示。この中から必要な要素をパースしてみる。
print("response body is....")
print(response.text)
print("")

#html文字列をfromstringに入れる。
#htmlボディ部全体をElementに置き換える。
root = lxml.html.fromstring(response.text)

#cssselectで取得できる。
#取得結果はElementインスタンスの１次元配列で返ってくる。
title = root.cssselect('title')
print("search title element:")
print(title)
#テキストノードを取得する場合はtext_content()を使う。
print(title[0].text_content())
print("")

#noteトップページのタイムラインから、各記事のタイトルと書いた人の名前を取得してみる。
print('---今日の記事リスト---')
articles = []
timelines = root.cssselect('section.o-gridNote')
for item in timelines:
  article_title = item.cssselect('div.o-gridNote__body h3')[0].text_content()
  article_author = item.cssselect('div.o-gridNote__footer a span')[0].text_content()
  articles.append({ 'title':article_title, 'author':article_author })
  print(article_title + " : written by " + article_author)

#簡単なバッチ処理ならScrapy使わないでもこれでできちゃいそうな。
#ただしスクロールイベントで動的に追加される記事とかは取れない。