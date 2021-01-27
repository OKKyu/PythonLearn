#!python3
# -*- coding:utf-8 -*-
import requests

r = requests.get("https://booklog.jp")

print("r.content : response body. This is binary")
print(r.content)
print("")
print("r.text : response body. This is str")
print(r.text)
print("")

print("r.encoding : response\'s encoding")
print(r.encoding)
print("")


print("r.cookies : It is sended from server.")
print(r.cookies)
print("")

print("r.headers : Http header information. It is expressed as dictionary.")
print(r.headers)
print("")

print("r.is_redirect: This response is redirect?. Type is boolean.")
print(r.is_redirect)
print("")

print("r.status_code: Http Status code.")
print(r.status_code)
print("r.reason: Explanation about causes of status code.")
print(r.reason)
print("")