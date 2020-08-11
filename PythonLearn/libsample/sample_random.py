#!python3
# -*- coding:utf-8 -*-
import random

'''
 genereation random value.
'''
#random: this method return one number at random from 0.0 to 1.0
print(random.random())

#uniform: this method return one number at random into any range.
print(random.uniform(0.0, 0.5))

#randrange: the method return one item into sequence at random.
#           the value selected into range.
print(random.randrange(5))
#  It is also set start and step args. 
print(random.randrange(start=0, stop=5, step=1))

#randint: this method return one number at random into any range.
print(random.randint(0, 5))

'''
  random selecting
'''
#choice: the method return one item into sequence at random.
print(random.choice(['apple', 'pear', 'banana']))

#sample: the method return some item into sequence at random.
#        item's number is 2nd args.
print(random.sample(range(10),3))

#choices: the method return some item into sequence at random.
#        item's number is 2nd args.
#        choices is supported after version 3.6 .
#print(random.choices(range(10),k=3))

'''
補足
  sampleは１回ランダムで選択された要素を次回選択することはない（非復元抽出）。
  choicesは１回ランダムで選択された要素を次回選択することも有りうる（復元抽出）。
  
  例えば以下配列があるとする。
    l = [1,2,3,4]
  
  sampleで上記配列からランダムに２個抽出する場合、[1,1]や[3,3]などのように同じインデックスに
  格納された値が重複して出現することはない。一方でchoicesの場合は重複して抽出される。
  
  内部の動作をイメージするとこんなだろう。
    sample(list, sample_num):
        result = []
        #対象リストから取得したい個数分繰り返す
        for i in range(sample_num +1):
              #ランダムに要素を１個選んで除外する。
            result.append(list.pop(random.randint(0,len(list)))
        return result
        
    choices(list, k=0):
        result = []
        #対象リストから取得したい回数分繰り返す。
        for i in range(k +1):
              #ランダムに要素を１個選ぶ。
            result.append(list[(random.randint(0,len(list))])
        return result
        
  またsampleの場合も、同じインデックスを選択しないだけであって同じ値華道家のチェックはしていない。
  対象リストに重複値が格納されている場合には同じ値を出力する。
  例えば配列 [2, 2, 2, 2]からsampleメソッドで4回取り出す場合、結果は 2,2,2,2となる。
'''