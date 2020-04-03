#! python3
# -*- coding:utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt

#1st:minimum point
#2nd:max point
#3rd:rank range
#plt.xticks(list(range(0,101,5)))

plt.xlabel('score')
plt.ylabel('members num')

#create test sampledata
#score = np.random.randint(0,101,1000000)
score = np.random.normal(50,10,100)

#plot data
#bins is rankranges number. maxpoint / rankrange.
plt.hist(score, bins=20)
plt.show()