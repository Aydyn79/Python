# -*- coding: utf8 -*-
#Задание №3
# В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.
from random import randint, seed
seed(1)
temp = [randint(0,100) for _ in range(10)]
mx = [i for i,j in enumerate(temp) if j == max(temp)]
mn = [i for i,j in enumerate(temp) if j == min(temp)]
print(f'Массив до: {temp}, максимум на индексах {mx}, минимум на индексах {mn}')
tmp = temp[mx[0]]
temp[mx[0]] = temp[mn[0]]
temp[mn[0]] = tmp
print(f'Массив после: {temp}')
