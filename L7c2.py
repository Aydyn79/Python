# -*- coding: utf8 -*-
from random import uniform

# 2. Отсортируйте по возрастанию методом слияния одномерный вещественный массив,
# заданный случайными числами на промежутке [0; 50). Выведите на экран исходный и отсортированный массивы.
arFloat = [round(uniform(-100,100), 3) for _ in range(0,20)]
print(arFloat)
def insAr(arFloat):
    for i in range(1, len(arFloat)):
        insrt = arFloat[i]
        j = i - 1
        while j >= 0 and arFloat[j] > insrt:
            arFloat[j + 1] = arFloat[j]
            j -= 1
        arFloat[j + 1] = insrt
    return arFloat

print(insAr(arFloat))