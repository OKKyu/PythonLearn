# coding: utf-8
# 自分の得意な言語で
# Let's チャレンジ！！

input_line = input().rstrip().split(' ')
N = int(input_line[0])
K = int(input_line[1])
P = int(input_line[2])

input_line = input().rstrip().split(' ')
sortStr = sorted(input_line)

for i in range(K * (P-1), K * P, 1):
    if i >= len(sortStr): break
    print(sortStr[i])