#! python3
# -*- encoding:utf-8 -*-
# webページ取得サンプル Basic認証が必要な場合
# This code is referred from
#  https://docs.python.org/3/library/urllib.request.html#module-urllib.request
import sys
import urllib.request
# Create an OpenerDirector with support for Basic HTTP Authentication...
#auth_handler = urllib.request.HTTPBasicAuthHandler()
# auth_handler.add_password(realm=None,
#                          uri=sys.argv[3],
#                          user=sys.argv[1],
#                          passwd=sys.argv[2])
#opener = urllib.request.build_opener(auth_handler)
# ...and install it globally so it can be used with urlopen.
# urllib.request.install_opener(opener)
urllib.request.urlopen(sys.argv[3])
