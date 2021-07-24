# -*- coding: utf8 -*-
#Задание №4
# Определить, какое число в массиве встречается чаще всего.
from random import randint, seed
# seed(1)
temp = [randint(0,30) for _ in range(25)]
tamp = []
for i,j in enumerate(temp):
    cnt = temp.count(temp[i])
    tamp.append(cnt)
    cnt = 0
print(f'Чаще всего в массиве {temp} встречается число "{temp[tamp.index(max(tamp))]}" - {max(tamp)} раза')