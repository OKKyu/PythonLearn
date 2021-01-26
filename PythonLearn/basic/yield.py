#!python3
# -*- coding:utf-8 -*-

#yield can only declare into function.
#if yield has located outside function, exception occured.
#yield 'aaa'

def yieldTest1():
    print("yield1 start")
    yield ['aaa', 'bbb']
    yield ['ccc', 'ddd']
    print("yield1 end")
    
def yieldTest2():
    print("yield2 start")
    for i in range(0,4):
        yield i
        i = i + 1
    print("yield2 end")
        
#yield 1 record
#implicitly, yield method has converted generator class.
#it's looks like iterable object.
print(yieldTest1())
y1 = yieldTest1()
print(y1)
for item in y1:
    print("yield1 item")
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
print(y2.__next__())
print(y2.__next__())
#If Iteration number was over max count, Error will occur.
print(y2.__next__())

print("process end")
# 関数の実行そのものを停止して呼び出し元に戻る、と考えれば良いか。