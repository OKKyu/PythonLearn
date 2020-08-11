#! python3
# -*- coding:utf-8 -*-
import hashlib

#setting pw
password = b"PassWord12345"

#md5
print(hashlib.md5(password).hexdigest())
#sha256
print(hashlib.sha256(password).hexdigest())
#sha512
print(hashlib.sha512(password).hexdigest())

#other method
m = hashlib.sha256()
m.update(b"PassWord12345")
print(m.hexdigest())