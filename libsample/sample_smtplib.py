#! python3
# -*- coding:utf-8

import smtplib

#open smtp. 
obj = smtplib.SMTP('smtp.gmail.com',587)

obj.ehlo()
obj.starttls()

obj.login('kyukyuinskt@gmail.com','oapmvbiaxxddvrtn')

info = {"from":'kyukyuinskt@gmail.com',
        "to":'kyukyuinskt@gmail.com',
        "subject":'Subject: python smtplib test \n',
        "msg":'HI!!!\n'}

obj.sendmail(info["from"], info["to"], info["subject"] + info["msg"])

obj.quit()

#gmail app passwd
#oapmvbiaxxddvrtn