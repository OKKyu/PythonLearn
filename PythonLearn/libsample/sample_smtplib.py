#! python3
# -*- coding:utf-8

import smtplib
from email.mime.text import MIMEText
from email.header import Header

# open smtp.
obj = smtplib.SMTP('smtp.gmail.com', 587)

obj.ehlo()
obj.starttls()

obj.login('', '')


msg = u'以下URLが本家サイト\nhttps://sqlitebrowser.org/dl/\nDebianだとaptで入れられるとのこと。\nsudo apt-get install sqlitebrowser\n'
msg = msg + u'ちなみにこのメールはPythonで送信しているのだ！（特に意味はない）\n'
info = MIMEText(msg, 'plain', 'utf-8')
info['Subject'] = Header(u'SQLiteツールあった', 'utf-8')
info['From'] = ''
info['To'] = ''
info['To'] = ''

# args can use string instead of MIMEText type.
obj.sendmail(info["From"], info["To"], info.as_string())

obj.quit()

