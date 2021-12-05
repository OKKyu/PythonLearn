#! python3
# -*- coding:utf-8 -*-
'''
  serialize.py
    This code refered below web site.
    http://dragstar.hatenablog.com/entry/2017/12/26/153214
'''

import pickle
target1 = [1, 2, 3, 4, 5]
target2 = ['a', 'b', 'c', 'd', 'e']
savePath = './'
fname = 'test.pickle'

print([x for x in zip(target1, target2)])

# リストオブジェクトをpickleを使ってダンプ
with open(savePath + fname, 'wb') as f:
    pickle.dump(target1, f)
    pickle.dump(target2, f)

# pickleを使ってリストオブジェクトをロード
with open(savePath + fname, 'rb') as f:
    target1_load = pickle.load(f)
    target2_load = pickle.load(f)

print(target1_load)
print(target2_load)
