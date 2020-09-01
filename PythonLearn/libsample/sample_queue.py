#!python3
# -*- coding: utf-8 -*-
import traceback
import numpy as np
from queue import Queue
from queue import Full

#Queue Common Methods.
#maxsize : allow insert number.
#          if maxsize <= 0, can insert infinity in queue unless allowed memory.
q = Queue(maxsize=10)
print(":: que check methods ::")
print(":: size:" + str(q.qsize()))
print(":: empty :" + str(q.empty()))
print(":: full :" + str(q.full()))
print("")

#insert
for i in range(0,10):
    q.put(i)

print(":: contents que ::")
print(":: size:" + str(q.qsize()))
print(":: empty :" + str(q.empty()))
print(":: full :" + str(q.full()))
print("")

#insert over maxsize
try:
    #if timeout is not None, freeze at line that over maxsize...
    #And Throw Full Exception.
    #by the way, scale of timeout is second.
    q.put(11, block=True, timeout=1)
    print(":: size no changed:" + str(q.qsize()))
except Full as full:
    print(traceback.format_exc())

try:
    #if keyword args block=False, non locked, and timeout parameter is ignored.
    #And Throw Full Exception.
    q.put(11, block=False, timeout=10)
    #below methods is equal that put(item, False) .
    q.put_nowait(11)
except Full as full:
    print(traceback.format_exc())

#get items by First in First Out
print(":: get items ::")
for i in range(q.qsize()):
    print(q.get(block=True, timeout=None))

print(":: after get que ::")
print(":: size:" + str(q.qsize()))
print(":: empty :" + str(q.empty()))
print(":: full :" + str(q.full()))
print("")


#other kinds of queue is below.

#LifoQueue
#Queue is FIFO , but LifoQueue is LIFO
from queue import LifoQueue
q = LifoQueue()
for i in range(10):
    q.put(i)

print(":: get LIFO Queue ::")
for i in range(q.qsize()):
    print(q.get())

#PriorityQueue
#minimum size is outputed first.
#no relation about inputed sequense.
from queue import PriorityQueue
q = PriorityQueue()
q.put(3)
q.put(1)
q.put(5)
q.put(-2)

print(":: get Priority Queue ::")
for i in range(q.qsize()):
    print(q.get())
