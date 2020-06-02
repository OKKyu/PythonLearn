#! python3
# -*- coding:utf-8 -*-

import json

#convert from json's str to dict
frStr = '{ "one":1, "two":2, "tree":3 }'
toJsonDict = json.loads(frStr)
print(toJsonDict)
print(toJsonDict["one"])
print("len:" + str(len(toJsonDict)))

#convert from dict to json's str
frJson = { "ichi":1, "san":3, "ni":2 }
toStr = json.dumps(frJson)
print(toStr)
print("len:" + str(len(toStr)))

#case. When situation thad read json file.
f = open('./testjson.json','r')
frStr = f.read()
print("before conv json : " + frStr)
toJson = json.loads(frStr)
print("after conv json : " + str(toJson))
