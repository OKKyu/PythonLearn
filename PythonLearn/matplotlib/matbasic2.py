#! python3
# -*- coding:utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt

#1st:minimum point
#2nd:max point
#3rd:rank range
plt.xlabel('score')
plt.ylabel('members num')

#create test sampledata
#score = np.random.randint(0,101,1000000)
score = np.random.normal(50,10,100000)

#plot data
plt.hist(score, bins=20)
plt.show()