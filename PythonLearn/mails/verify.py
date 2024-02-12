#!python3
# -*- coding:utf-8 -*-

'''
 https://gitea.ksol.io/karolyi/py3-validate-email
 試してみたが、効果はさっぱり分からない・・・存在するはずのメアドでも、gmailが "Cannot assign requested address"と返事する。
'''
import requests
from validate_email import validate_email_or_fail

try:
    is_valid = validate_email_or_fail(
        email_address='adagiomusika6846t@gmail.com',
        check_format=True,
        check_blacklist=True,
        check_dns=True,
        dns_timeout=10,
        check_smtp=True,
        smtp_timeout=10,
        # smtp_helo_host='smtp.gmail.com',
        # smtp_from_address='adagiomusika6846t@gmail.com',
        smtp_skip_tls=False,
        smtp_tls_context=None,
        smtp_debug=False
        #address_types=frozenset([IPv4Address, IPv6Address])
    )
except Exception as ex:
    print(ex)

'''
  https://stackoverflow.com/questions/53561296/python-correct-method-verify-if-email-exists
  https://isitarealemail.com/
  
  Email存在チェックサービスサイト。従来からWebAPIとして利用可能な実装がなされている。docsリンク先にマニュアルあり。
  これが使いやすい。アカウントを作成しなくても使える。ただし１日100件まで（同アドレスを重複してチェックした場合もカウントされる）。
  また1,000件を超えると課金が必要。詳細は本家サイトを参照。
'''

email_address = str(input('Email: '))
response = requests.get(
    "https://isitarealemail.com/api/email/validate",
    params={'email': email_address})

status = response.json()['status']
if status == "valid":
    print("email is valid")
elif status == "invalid":
    print("email is invalid")
else:
    print("email was unknown")

