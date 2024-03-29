#!python3

from itertools import zip_longest
name = ['purin', 'gorirander', 'negiga-knight']
rank = ['A', 'SSS', 'B']

for n, r in zip(name, rank):
    print(n, r)
print("")

rank.append('C')

# if list's size is less than other, it is ignored.
for n, r in zip(name, rank):
    print(n, r)
print("")

# if it is use zip_longest, fill in None.
for n, r in zip_longest(name, rank):
    print(n, r)
print("")


matrix = [[1, 3, 5], [4, 9, 25], [8, 27, 125]]
print(matrix)
print(*matrix)
for x, y, z in zip(*matrix):
    print(x, y, z)
