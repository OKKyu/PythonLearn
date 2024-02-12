#! python3
# -*- coding:utf-8

import sys
import smtplib
from email.mime.text import MIMEText
from email.header import Header

# open smtp.
obj = smtplib.SMTP('smtp.gmail.com', 587)
# obj = smtplib.SMTP_SSL('smtp.gmail.com', 587)

obj.ehlo()
obj.starttls()

# if you want to check mail status, debug on
obj.set_debuglevel(2)

obj.login(sys.argv[1], sys.argv[2])

msg = u'以下URLが本家サイト\nhttps://sqlitebrowser.org/dl/\nDebianだとaptで入れられるとのこと。\nsudo apt-get install sqlitebrowser\n'
msg = msg + u'ちなみにこのメールはPythonで送信しているのだ！（特に意味はない）\n'
info = MIMEText(msg, 'plain', 'utf-8')
info['Subject'] = Header(u'SQLiteツールあった', 'utf-8')
info['From'] = sys.argv[3]
info['To'] = sys.argv[4]

# args can use string instead of MIMEText type.
#obj.sendmail(info["From"], info["To"], info.as_string())
obj.sendmail("kyinskt@gmail.co", info["To"], info.as_string())

obj.quit()

