#! python3
# -*- coding: utf-8 -*-
import sys

#print('if文の例')
if len(sys.argv) == 2 :
   print('hello,' + sys.argv[1])
elif len(sys.argv) == 3:
   print('Danke!,' + sys.argv[1] + ' und ' + sys.argv[2])
elif len(sys.argv) == 4 :
   print('CheyChey,' + sys.argv[3] )
else:
	print('........')
	
#print('for文の例')
#要素を順番どおりに出力する
words = ['cat','window','defensestrate']
for w in words:
	print(w,len(w))

#print('ループ内部でリストを修正する例　スライスで複製したものをループさせると、無限ループを防げる')
#うっかり 'in words' とスライスを付け忘れると、insertによって要素数が増える→増えた分をループ処理する→また条件を満たすので
#ループする...といった具合に無限ループする。
for w in words[:]:
	if len(w) > 6:
		words.insert(0,w)
print(words)

#range()
#pythonではfor文を回数分実行する際にrange()を使う。以下は0〜4インデックスの計5回の処理を行う。
for i in range(5):
	print(i)

#範囲指定も可能。
for i in range(5,10):
	print(i)

#第三引数に増加量を指定できる。
for i in range(0,10,3):
	print(i)

#マイナスも可能。
for i in range(-10,-20,-1):
	print(i)

#インデックスで繰り返し処理をする場合はlenを組み合わせる。
a = ['Mary', 'had', 'a', 'little', 'lamb']
for i in range(len(a)):
    print(i, a[i])

#for、while文にelse文をもたせることができる。
#これはループが終了したときに１回のみ実行される。ただしbreakされたときには実行されない。
for n in range(2, 10):
     for x in range(2, n):
         if n % x == 0:
             print(n, 'equals', x, '*', n//x)
             break
     else:
         # loop fell through without finding a factor
         print(n, 'is a prime number')

#pass文 処理行の記述を構文上求められるが、なんの動作も必要がない（させない）場合に使う。
while True:
	pass




