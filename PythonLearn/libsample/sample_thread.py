#! python3
# -*- coding: utf-8 -*-

import sys
import time
import threading

def f(a, b):
    print(str(a) + "  " + str(b))
    i=1
    for i in range(1, 6):
        print(i)
        i = i + 1
        time.sleep(1)
thObj = threading.Thread(target=f, args=(123,456))
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
