#! python3
# -*- coding: utf-8 -*-

import sys
import time
import threading

def f():
    i=1
    while True:
        print(i)
        i = i + 1
        time.sleep(1)
thObj = threading.Thread(target=f)
thObj.start()
#the above code is same as below.. but python2.
#  import thread
#  thread.start_new_thread(f, ())

#exit control
while True:
    c = sys.stdin.read(1)
    print("read " + c)
    if c == 'e':
        sys.exit()
