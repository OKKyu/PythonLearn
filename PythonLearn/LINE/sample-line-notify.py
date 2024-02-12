#!python3
# -*- coding:utf-8 -*-
# refference is below...
#  https://qiita.com/moriita/items/5b199ac6b14ceaa4f7c9
#
# LINE-Notify formal site.
#  https://notify-bot.line.me/ja/
#
import sys
import os
import requests

# prepare
url = "https://notify-api.line.me/api/notify"
access_token = sys.argv[1]
headers = {'Authorization': 'Bearer ' + access_token}

# send message
#message = 'Heeey! This is message from K.N.! with using LINE-Notify WEB API'
#message = message + os.linesep + 'This API is very simple and easy-to-use.'
message = sys.argv[2]
payload = {'message': message}
r = requests.post(url, headers=headers, params=payload,)
