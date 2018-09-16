#! python3 
# -*- coding: UTF-8 -*-
# リスト（配列）の基本

#リスト宣言　JavaScriptと同じ
squares = [1,4,9,16,25]
print(squares)

#文字列や他シーケンスオブジェクト同様の添え字アクセスが可能。
print(squares[0])
print(squares[-1])
print(squares[-3:])

#全リスト要素をスライスした場合は新しいリストコピーを返却する。
newSqu = squares[:]
print("Original List:" + str(squares))
print("Copied List:" + str(newSqu))

#リストは可変のため要素の内容を変更できる。しかも型は問わない
newSqu[1] = 'hello'
print("Original List:" + str(squares))
print("Copied List:" + str(newSqu))

#リストの連結も可能
newSqu = newSqu + ['HeyHeyHeeey!','GYaaaaaAAA!!']
print("Copied List:" + str(newSqu))

#append()を使って末尾に要素を追加することも可。
newSqu.append(32111)
print("Copied List:" + str(newSqu))

#スライスを使って代入も可能。
newSqu[2:4] = [0,0,1]
print("Copied List:" + str(newSqu))

#削除も可能。
newSqu[2:5] = []
print("Copied List:" + str(newSqu))
#全部削除
newSqu[:] = []
print("Copied List:" + str(newSqu))

#len関数で要素数を取得可能。
print("Original List len:" + str(len(squares)))

#入れ子も可能。
listlist = [[1,3,5],['a','b','c']]
print("[0][1] :" + str(listlist[0][1]))
print("[1][2] :" + str(listlist[1][2]))




