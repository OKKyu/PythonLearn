#!/bin/python3
# -*- coding:utf-8 -*-
# referrerence:
#  https://qiita.com/sira/items/a0e8c5e523bc9bedc803
import time
import socket
ETH_P_ALL = 3
interface = 'wlan0'
dst = b'\xff\xff\xff\xff\xff\xff'   # destination MAC address
src = b'\x50\xc4\xdd\x90\x13\xd0'   # source MAC address
proto = b'\x88\x99'                 # Ethernet frame type
payload = 'Hello, world!000000000000000000000000000000000'.encode()  # payload
payload = b'\23\5e\bb\2f\13\ba\ff\50\c4\dd\90\13\d0\04\00\00\00\00\00\00\00\00\00\00\00\00\00\00\00\00\00\00\00'
# family:AF_PACKET, type:SOCK_RAW.
s = socket.socket(socket.AF_PACKET, socket.SOCK_RAW, socket.htons(ETH_P_ALL))
s.bind((interface, 0))

for i in range(100000):
    print("Sent :" + str(i))
    s.sendall(dst + src + proto + payload)
    time.sleep(0.02)
print('Sent!')
s.close()
