#!python3
# -*- coding:utf-8 -*-
import time
import sys
import os
import json
from twilio.rest import Client

with open(sys.argv[1], "rb") as f:
    auth_json = json.loads(f.read())
    os.environ.setdefault("account_SID", auth_json["account_SID"])
    os.environ.setdefault("auth_token", auth_json["auth_token"])
    os.environ.setdefault("from_twilio_number", auth_json["from_twilio_number"])

to_phone = "+81XXYYYYZZZZ"
message_body = "Hey, Could you recieve this message? \n Year! That\'s good!!"

# If there are command line variables, set it to
if len(sys.argv) > 1:
    if len(sys.argv[1]) <= 12 and sys.argv[1][1:].isdecimal() == True:
        to_phone = sys.argv[1]
    else:
        message_body = sys.argv[1]
elif len(sys.argv) > 2:
    to_phone = sys.argv[1]
    message_body = sys.argv[2]

twilio_cli = Client(os.environ.get("account_SID"), os.environ.get("auth_token"))

# sample1 using demo sample file from twilio web site.
call = twilio_cli.calls.create(from_=os.environ.get("from_twilio_number"), to=to_phone,
                               url="http://demo.twilio.com/docs/voice.xml")

print("------------ start ------------")
print(call.sid)
print(call.from_)
print(call.to)
print(call.date_created)
print("-------------------------------")

# debug while sending.
while True:
    print("------------ sending ------------")
    updated_call = twilio_cli.calls(call.sid).fetch()

    if updated_call != None:
        print(updated_call.status)
        print(updated_call.start_time)
        print(updated_call.date_updated)
        print("")
        if updated_call.status in ["completed"]:
            print(updated_call.end_time)
            break
    time.sleep(1)
