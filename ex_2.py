#!/usr/bin/env python3
from librip.gen import gen_random
from librip.iterators import Unique

data1 = [1, 1, 1, 1, 1, 2, 2, 2, 2, 2]
data2 = gen_random(1, 5, 5)
d2 = ['F','f','fa','d']

print(list(Unique(data1)))
print(list(Unique(data2)))
print(list(Unique(d2, ignore_case=True)))
print(list(Unique(d2, ignore_case=False)))
#print(list(Unique(d2, ignore_case=False)))
# Реализация задания 2