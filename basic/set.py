#! python3
# -*- coding: utf-8 -*-
# setの基本

print('Javaのセットと同じく重複値を持たないコレクション。')
set1 = { 'aa', 'bb'}
print(set1)
print('add関数で要素を追加する。重複値を入れても追加されない。')

for i in range(3):
	print('cc追加 ' + str(i + 1) + '回目')
	set1.add('cc')

print(set1)
print('実行するとわかるが、登録順序も保証されない。ここ注意。\n')

print('集合の積も取れる。これは便利。以下はset1とset2で重複する値,bbだけが表示される。')
set2 = {'bb'}
print(set1 & set2)

#if you want to create empty set, please use set() method.
set3 = set()