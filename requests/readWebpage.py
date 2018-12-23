#! python3
#-*- encoding:utf-8 -*-
#webページ取得サンプル
import sys
import requests

#getメソッド。httpメソッドのgetに相当。
r = requests.get('http://gihyo.jp/lifestyle/clip/01/everyday-cat')
if r.status_code == 200:
	print(r.text[:50])
else:
	print('status-code:' + str(r.status_code))

#json()でjson形式のレスポンスも取得可能。
#

#他httpメソッドに対応したメソッドもある。
# postメソッド  辞書コレクションでパラメータを指定する。
payload = {'key1:value1', 'key2:value2'}
r = requests.post('http://httpbin.org/post',data=payload)

# putメソッド  辞書コレクションでパラメータを指定する。
#r = requests.put('http://httpbin.org/put',data=payload)
#print(r.text[:50])

# deleteメソッド
#r = requests.delete('http://httpbin.org/delete')

# headメソッド
#r = requests.head('http://httpbin.org/delete')

# optionメソッド
#r = requests.options('http://httpbin.org/get')


