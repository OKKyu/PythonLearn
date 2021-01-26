#!python3
import statistics
from statistics import geometric_mean

print("mean : calcultate average")
print(statistics.mean([1,2,2,5]))
print("")

print("median : calcultate center value")
print("         if num of items is odd, calculate most centered two values. ")
print(statistics.median([1,2,2,5]))
print("")

print("mode : display most appearanced value")
print(statistics.mode([1,2,2,5]))
print("")

print("幾何平均 python3.8以降でサポートされている")
#print(geometric_mean([1.0, 0.00001, 10000000000.]))

