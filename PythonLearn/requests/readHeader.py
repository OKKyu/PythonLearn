#! python3
# -*- encoding:utf-8 -*-
# webページ取得サンプル
# read only http headers
import sys
import requests

if len(sys.argv) > 1:
    url = sys.argv[1]

    # urlを指定してHttpリクエストを送信している。そしてHttpレスポンスが戻り値として返却される。
    # timeoutに接続タイムアウトと読み込みタイムアウトを設定する事も可能。
    r = requests.head(url, timeout=(0.5, 1.0))
    if r.status_code == 200:
        if len(sys.argv) > 2 and sys.argv[2] == 'split':
            for key, item in r.headers.items():
                print(key, item)
        else:
            print(r.headers)
    else:
        print('status-code:' + str(r.status_code))
        print('reason:' + r.reason)
