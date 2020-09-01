#!python3
# -*- coding: utf-8 -*-
#deque: double-ended queue
import numpy as np
from collections import deque

#first arg is iterable. second arg is maxlength.
deq = deque(np.ones(3, dtype=np.int16),10)
print("initialize deq with iterable object and maxlength")
print(deq)
# first arg can also non iterable variables.
# and str is converted to list object that split char.
d = deque("ghi")
print(d)

#put right
deq.append(3)
print("append right")
print(deq)
#put left
deq.appendleft(2)
print("append left")
print(deq)
print("")

#count same value to first argument.
print("count method")
print("number of 0: " + str(deq.count(0)))
print("number of 1: " + str(deq.count(1)))
print("number of 2: " + str(deq.count(2)))
#if you want to count all items, can use len.
print("number of items: " + str(len(deq)))
print("")

#index
print("index method")
print("3 index is :" + str(deq.index(3)))
print("1's first index is :" + str(deq.index(1)))
#you can indicate search region.
#and if not finded, throw valueerror exception.
try:
  print("3 index in range 0~2 :" + str(deq.index(3, 0, 2)))
except ValueError as ve:
  print("if throws ValueError Exception, output message below.. ")
  print(" X is not in deque")
  print(ve)
print("")

#insert
print("insert method. It is likly to list's insert.")
print("insert value 9 into index 3.")
deq.insert(3,9)
print(deq)
print("")

#extend
print("extendleft method.")
print("extended iterable has reversed and appended.")
list = [13,14,15]
deq.extendleft(list)
print(deq)
print("")

#pop
print("pop (left) method.")
print("pop from right: " + str(deq.pop()))
print("pop from left: " + str(deq.popleft()))
print(deq)
print("")

#remove
print("remove method.")
print("remove 1 (first appeared)")
str(deq.remove(1))
print(deq)
print("")

#reverse
print("reverse method.")
str(deq.reverse())
print(deq)
print("")

#rotate
#shift n step right. if n is minus value, step left.
print("rotate method.")
print("shift 1 step right.")
deq.rotate(1)
print(deq)
print("shift 2 step left.")
deq.rotate(-2)
print(deq)
print("")