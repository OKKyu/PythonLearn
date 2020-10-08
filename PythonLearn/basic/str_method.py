#! python3
# -*- coding:utf-8 -*-

string = 'Hello'

#conv upper case string
print(string.upper())

#conv lower case string
print(string.lower())

#judge upper case string
print(string.isupper())

#judge lower case string
print(string.islower())

#judge str have only alphabet chars
print(string.isalpha())

#judge str have only  number 
#記号（カンマ、ピリオド、マイナスなど）が入っている文字列は偽
#半角・全角のアラビア数字が真
print('12:' + str('12'.isdecimal()))
print('12５:' + str('12５'.isdecimal()))
print('12５三:' + str('12５三'.isdecimal()))
#半角・全角のアラビア数字、特殊数字が真
print('12:' + str('12'.isdigit()))
print('12５:' + str('12５'.isdigit()))
print('12５三:' + str('12５三'.isdigit()))
#半角・全角のアラビア数字、特殊数字、漢数字が真
print('12:' + str('12'.isnumeric()))
print('12５:' + str('12５'.isnumeric()))
print('12５三零:' + str('12５三零'.isnumeric()) + "こんな難しい漢数字でも判定できている")

#judge str have only alpha or number 
print(string.isalnum())

#judge str have only space,tab,or carrige code 
print(' \r\n\t'.isspace())

#judge first char is upper and other chars is lower
print(string.istitle())

#split
print('あいうえ,おかき'.split(','))

#join
#splitの逆でjoin関数というのがある。指定した区切り文字で文字列を連結する。リストの要素を１個の文字列に連結したいときに使える。
print('-'.join(['あいうえ','おかき']))
#空文字列を指定すると文字連結になる。いちいちforで回して + 演算子で結合しないでよい。
print(''.join(['あいうえ','おかき']))

#文字列置換、replaceもある
print('あいうえ-おかき'.replace('-',''))

#startswith,endwith
print(string.startswith('He'))
print(string.endswith('o'))

#lpad,rpad,centerpad?
print(string.ljust(20,'*'))
print(string.rjust(20,'*'))
print(string.center(20,'*'))

#trim,ltrim,rtrim
print('***guten*morgen!***'.strip('*'))
print('***guten*morgen!***'.lstrip('*'))
print('***guten*morgen!***'.rstrip('*'))