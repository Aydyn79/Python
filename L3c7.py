# -*- coding: utf8 -*-
#Задание №7
# В одномерном массиве целых чисел определить два наименьших элемента.
# Они могут быть как равны между собой (оба являться минимальными), так и различаться.
from random import randint
temp = [randint(23,100) for _ in range(15)]
print(f'Массив до сортировки {temp}')
temp.sort()
a = temp.index(min(temp))
b = temp[a+1]
print(f'Массив после сортировки {temp}, минимальное число {temp[a]} и его собрат {b}')