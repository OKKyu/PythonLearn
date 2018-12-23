#! python3
#-*- encoding:utf-8 -*-
#webページ取得サンプル
import sys
import requests

if len(sys.argv) > 1 :
	url = sys.argv[1]
		
	r = requests.head(url)
	if r.status_code == 200:
		if len(sys.argv) > 2 and sys.argv[2] == 'split':
			for key,item in r.headers.items():
				print(key, item)
		else:
			print(r.headers)
	else:
		print('status-code:' + str(r.status_code))
