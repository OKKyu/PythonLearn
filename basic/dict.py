#! python3
# -*- coding:utf-8 -*-

#create empty dictionary
dict1 = {}

#create filled dictionary. pair of key and value.  
dict1 = {'a':12, 'b':33, 'c':42}

#you can use int,str, and other various type.
#andalso youcan use a kind of type data by  value.
dict_variable = { 1:'aiu', 2.23:True, 'nin':12345 }

#dictionary can return values as list like.
for k in dict1.keys():
    print('key names, ' + k)
for v in dict1.values():
    print('values, ' + str(v))
for k,v in dict1.items():
    print('key and values, ' + k + ':' + str(v))

#you can check by 'in' that dictionary contains a key or a value.
print('dict1 have key a ?, it\'s ' + str('a' in dict1) )
print('dict1 have value 43 ?, it\'s ' + str(43 in dict1) )

#get method 
print('dict1 haven b, returned:' + str(dict1.get('b', 0)))
print('dict1 haven\'t dd, alternate value returned:' + str(dict1.get('dd', 0)))

#setdefault method
#if you want to add new key&value pair when dictionary have no key you want to add, 
#you can use setdefault method.
dict1.setdefault('a', 21)
print(dict1['a'])
dict1.setdefault('ee', 343)
print(dict1['ee'])