#!/usr/bin/env python3
from librip.gen import gen_random
from librip.iterators import Unique

data1 = [1, 1, 1, 1, 1, 2, 2, 2, 2, 2]
data2 = gen_random(1, 7, 10)

print([x for x in Unique(['f','F','fa','d'])])

d=(list(data2))
print(d)
print([x for x in Unique(d,ignore_case = False)])

# Реализация задания 2