#!python3

name = ['purin', 'gorirander', 'negiga-knight']
rank = ['A', 'SSS', 'B']

for n, r in zip(name, rank):
    print(n, r)
print("")

rank.append('C')

# when list's size is less than other, ignore.
for n, r in zip(name, rank):
    print(n, r)
print("")

# if it is use zip_longest, fill in None.
from itertools import zip_longest
for n, r in zip_longest(name, rank):
    print(n, r)
print("")


matrix = [[1, 3, 5], [4, 9, 25], [8, 27, 125]]
print(matrix)
print(*matrix)
for x,y,z in zip(*matrix):
    print(x,y,z)