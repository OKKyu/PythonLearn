#! python3
# -*- coding:utf-8 -*-
import time

#calculation time.
stime = time.time()
result = 2
for i in range(1,2):
    result = result * i
    #wait milliseconds.
    time.sleep(1)
etime = time.time()
print("result: " + str(result))
print("time: " + str(etime - stime))
print("end")