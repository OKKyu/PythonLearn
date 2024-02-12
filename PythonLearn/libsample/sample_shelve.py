#! python3
# -*- coding:utf-8 -*-
# shelve can save python's variable by binary file.
# shelve looks like serialize of java.

import shelve

# save variable in shelve file.
shelf_file = shelve.open('mydata')
cats = ['a', 'bb', 'cc']
shelf_file['cats'] = cats
shelf_file.close()

# get saved variable in shelve file.
shelf_file = shelve.open('mydata')
print(shelf_file['cats'])

# shelve use as like dict,but shelve isn't dict.
print(list(shelf_file.values()))
print(list(shelf_file.keys()))
print(list(shelf_file.items()))
