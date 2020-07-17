#! python3
# -*- coding: utf-8 -*-
import sys
import MeCab

tagger = MeCab.Tagger()
tagger.parse('')

targetStr = sys.argv[1]
node = tagger.parseToNode(targetStr)

while node:
	print( node.surface + "::" + node.feature )
	node = node.next


