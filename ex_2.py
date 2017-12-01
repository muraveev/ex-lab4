#!/usr/bin/env python3
from librip.gens import gen_random
from librip.iterators import Unique

data1 = [1, 1, 1, 1, 1, 2, 2, 2, 2, 2]
data2 = gen_random(1, 3, 10)
data3 = ["DGR", "asd","RGH", "Asd", "Asd", "wtw", "Rgh", "WTW", "wt4w4", "dgr"]

for i in Unique(data1):
    print(i, end=" ")
print(" ")

for i in Unique(data2):
    print(i, end=" ")
print(" ")

for i in Unique(data3, ignore_case=True):
    print(i, end=" ")


# Реализация задания 2