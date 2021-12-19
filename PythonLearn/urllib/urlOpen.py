#! python3
# -*- encoding:utf-8 -*-
# webページ取得サンプル
import sys
from urllib.request import urlopen

if len(sys.argv) > 1:
    f = urlopen(sys.argv[1])
    # urlopenの戻り値はHTTPResponseクラス。これはopen関数の戻り値であるファイルオブジェクトのように扱える。
    print('type:' + str(type(f)))
    # httpレスポンスのヘッダーを取得する。
    print('Content-type:' + f.getheader('Content-Type'))
    # エンコーディングを取得する。エンコーディングが明示されていない場合はutf-8にする。
    contentCharset = f.info().get_content_charset(failobj='utf-8')
    # readでレスポンスボディ(bytes)を取得できる。接続は自動でcloseされる。
    print('readBody:' + f.read().decode(contentCharset))
    # httpステータスを取得する。
    print('Status:' + str(f.status))
else:
    print('URLがコマンドライン引数に指定されていません。')
