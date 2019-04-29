#! python3
# -*- coding:utf-8 -*-
#This contents by bellow site
#http://dragstar.hatenablog.com/entry/2017/12/26/153214

import pickle
target = [1, 2, 3, 4, 5]
savePath = '/home/puppy/pic/'
fname = 'test.pickle'

print(target)

# リストオブジェクトをpickleを使ってダンプ
with open(savePath + fname, 'wb') as f:
  pickle.dump(target, f)

# pickleを使ってリストオブジェクトをロード
with open(savePath + fname, 'rb') as f:
  target2 = pickle.load(f)

print(target2)