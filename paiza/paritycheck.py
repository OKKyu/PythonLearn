# coding: utf-8
# 自分の得意な言語で
# Let's チャレンジ！！

input_line = int(input())
n1 = 0
n2 = 0
n3 = 0
n4 = 0
for i in range(input_line):
  s = input()
  n1 = n1 + int(s[0:1])
  n2 = n2 + int(s[1:2])
  n3 = n3 + int(s[2:3])
  n4 = n4 + int(s[3:4])

n1 = n1 % 2
n2 = n2 % 2
n3 = n3 % 2
n4 = n4 % 2

print(str(n1) + str(n2) + str(n3) + str(n4))