# coding: utf-8
# 自分の得意な言語で
# Let's チャレンジ！！

input_line = input()
result = ''
for i in range(len(input_line)):
  c = input_line[i]
  if c == 'A':
      result = result + '4'
  elif c == 'E':
      result = result + '3'
  elif c == 'G':
      result = result + '6'
  elif c == 'I':
      result = result + '1'
  elif c == 'O':
      result = result + '0'
  elif c == 'S':
      result = result + '5'
  elif c == 'Z':
      result = result + '2'
  else:
      result = result + c
      
print(result)