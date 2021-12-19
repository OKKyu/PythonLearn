#! python3
# -*- encoding:utf-8 -*-
# webページ取得サンプル
import sys
import requests

# getメソッド。httpメソッドのgetに相当。
# URLパラメータはキーワード引数params=に辞書を使って設定が可能。
#r = requests.get('https://gihyo.jp/lifestyle/clip/01/everyday-cat',params={'aa':1,'bb':2})
r = requests.get('https://gihyo.jp/lifestyle/clip/01/everyday-cat')
if r.status_code == 200:
    # HTMLデータ部はtextプロパティの中に格納されている。長いので先頭50文字のみ表示している。
    print(r.text[:50])
    # ヘッダーの取得。headers辞書に登録されている。
    # urllibのgetheaderと違いキーはlower caseとなっている。
    print(r.headers['content-type'])
    # エンコーディングも変数として取得できる。
    print(r.encoding)
else:
    print('status-code:' + str(r.status_code))

# 他httpメソッドに対応したメソッドもある。
# postメソッド  辞書コレクションでパラメータを指定する。
payload = {'key1': 'value1', 'key2': 'value2'}
r = requests.post('http://httpbin.org/post', data=payload)
if r.status_code == 200:
    print(r.text)
    # 返却結果がjsonの場合はjson()でjson形式のレスポンスも取得可能。
    print("json() methods")
    print(r.json())
else:
    print('status-code:' + str(r.status_code))

# putメソッド  辞書コレクションでパラメータを指定する。
#r = requests.put('http://httpbin.org/put',data=payload)
# print(r.text[:50])

# deleteメソッド
#r = requests.delete('http://httpbin.org/delete')

# headメソッド
#r = requests.head('http://httpbin.org/delete')

# optionメソッド
#r = requests.options('http://httpbin.org/get')

# get,post,put,delete,head,option共通で以下のキーワード引数指定ができる。
# headers={'user-agent':'my-agent-is-intelleon'}  httpヘッダーの設定
# auth=('User ID','User Password')                Basic Certification

#
s = requests.Session()
s.headers.update({'user-agent': 'my-agent-is-intelleon'})
s.auth = ('User ID', 'User Password')
s.get('http://httpbin.org/get', params=payload)


# わざわざstatus_codeで分岐せずとも、200 or not で例外を発生させる方法もある。
try:
    r = requests.get('https://gihyo.jp/lifestyle/clip/01/everyday-cat')
    r.raise_for_status()
except Exception as ex:
    print(r.text)
