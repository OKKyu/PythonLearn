#! python3
# -*- coding: utf-8 -*-

import sys
import time
import thread

def f():
    i=1
    while True:
        print(i)
        i = i + 1
        time.sleep(1)

thread.start_new_thread(f, ())

while True:
    c = sys.stdin.read(1)
    if c == ' ':
        sys.exit()
