# -*- coding: utf8 -*-
#Задание №5
# В массиве найти максимальный отрицательный элемент.
# Вывести на экран его значение и позицию в массиве.
from random import randint
temp = [randint(-30,30) for _ in range(25)]
a = min(temp)
b = temp.index(a)
print(f'{temp} максимально отрицательный элемент {a} на позиции {b}')
