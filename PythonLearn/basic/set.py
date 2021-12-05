#! python3
# -*- coding: utf-8 -*-
'''
  set.py
    Basics of set object in python.
'''

print('Javaのセットと同じく重複値を持たないコレクション。')
set1 = {'aa', 'bb'}
print(set1)
print('add関数で要素を追加する。重複値を入れても追加されない。')

for i in range(3):
    print('cc追加 ' + str(i + 1) + '回目')
    set1.add('cc')

print(set1)
print('ccが１個しかない。実行するとわかるが、登録順序も保証されない。ここ注意。\n')

print('集合の積も取れる。これは便利。以下はset1とset2で重複する値,bbだけが表示される。')
print('set2 = {\'bb\',\'dd\'}')
set2 = {'bb', 'dd'}
print(set1 & set2)

# if you want to create empty set, please use set() method.
set3 = set()

print('その他集合型の操作')
print('和集合 a+b')
print(set1.union(set2))
print('積集合 a&b と同じ')
print(set1.intersection(set2))
print('差集合 a-b と同じ')
print(set1.difference(set2))
print('対象差集合 a^bと同じ')
print(set1.symmetric_difference(set2))
print('')

print('共通データを持たないかを判定することも可能 isdisjoint')
print(set1.isdisjoint(set2))

print('set1がset2の部分集合（内包されている集合）かどうか issubset')
print(set1.issubset(set2))

print('set1がset2の上位集合（内包している集合）かどうか issuperset')
print(set1.issuperset(set2))
print("")

# 破壊的メソッド
print('add')
set1.add('hh')
print(set1)
print('discard 引数値が存在しない場合何もしない。')
set1.discard('hh')
print(set1)
print('remove 引数値が存在しない場合はKeyErrorが出る')
set1.remove('aa')
print(set1)
print('update 引数に指定したシーケンス値を全て加える')
set1.update(set2)
print(set1)
print('pop 先頭データを１つ取り出してsetから削除する')
print(set1.pop())
print(set1)

print('セット内包表記')
print('辞書内包表記と似ているが、コロンを抜くとセット内包表記となる。')
set1 = {i for i in range(3, 30, 3)}
print(set1)
set1.add(3)
print(set1)
