#!python3
# -*- coding:utf-8 -*-

#yield can only declare into function.
#if yield has located outside function, exception occured.
#yield 'aaa'

def yieldTest1():
    yield 'aaa'
    
def yieldTest2():
    for i in range(0,10):
        yield i
        i = i + 1
        
#yield 1 record
#implicitly, yield method has converted generator class.
#it's looks like iterable object.
print(yieldTest1())
y1 = yieldTest1()
print(y1)
for item in y1:
    print(item)

#yield many record
y2 = yieldTest2()
print(y2)
print(y2.__next__())
print(y2.__next__())
print(y2.__next__())
y2 = yieldTest2()
print(y2.__next__())
print(y2.__next__())
