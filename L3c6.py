# -*- coding: utf8 -*-
#Задание №6
# В одномерном массиве найти сумму элементов, находящихся между
# минимальным и максимальным элементами. Сами минимальный и
# максимальный элементы в сумму не включать.
from random import randint
temp = [randint(0,530) for _ in range(10)]
a = temp.index(min(temp))
b = temp.index(max(temp))
if a > b:
    tmp = a
    a = b
    b = tmp
plus = sum(temp[a+1:b:])
print(f'В одномерном массиве {temp},с минимальной и максимальной точками {temp[a]}, {temp[b]} \n '
      f'получается срез {temp[a+1:b:]},сумма элементов которого {plus}')