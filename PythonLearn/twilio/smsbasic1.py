#!python3
# -*- coding:utf-8 -*-
import time
import sys
import os
import json
from twilio.rest import Client

with open("/root/twilio-auth.json", "rb") as f:
    auth_json = json.loads(f.read())
    os.environ.setdefault("account_SID", auth_json["account_SID"])
    os.environ.setdefault("auth_token", auth_json["auth_token"])
    os.environ.setdefault("from_twilio_number", auth_json["from_twilio_number"])

to_phone = "+81XXYYYYZZZZ"
message_body = "Hey, Could you recieve this message? \n Year! That\'s good!!"

# If there are command line variables, set it to
if len(sys.argv) > 1:
    if len(sys.argv[1]) >= 10 and sys.argv[1][1:].isdecimal() == True:
        to_phone = sys.argv[1]
    else:
        message_body = sys.argv[1]
elif len(sys.argv) > 2:
    to_phone = sys.argv[1]
    message_body = sys.argv[2]

twilio_cli = Client(os.environ.get("account_SID"), os.environ.get("auth_token"))
message = twilio_cli.messages.create(body=message_body,
                                     from_=os.environ.get("from_twilio_number"), to=to_phone)

# debug from to
print("------------ start ------------")
print(message.sid)
print(message.from_)
print(message.to)
print(message.date_created)
print("-------------------------------")

# debug while sending.
while True:
    print("------------ sending ------------")
    updated_message = twilio_cli.messages(message.sid).fetch()

    if updated_message != None:
        print(updated_message.status)
        print(updated_message.date_sent)
        print("")
        if updated_message.status in ["delivered", "failed", "undelivered"]:
            break
    time.sleep(1)

