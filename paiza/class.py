#! python3

# coding: utf-8
# Your code here!

# 2次元リストで地図を表示する
landmap = [["森" for i in range(20)] for j in range(10)]
landmap[0][0]="城"
landmap[0][19]="城"
landmap[0][19]="町"
landmap[9][19]="町"
for (i,line) in enumerate(landmap):
    print(str(i + 1) + ":",end="")
    for area in line:
        print(area,end="")
    print()
