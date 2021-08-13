# -*- coding: utf8 -*-
from random import randint
# 3. Массив размером 2m + 1, где m – натуральное число, заполнен случайным образом. Найдите в массиве медиану.
# Медианой называется элемент ряда, делящий его на две равные части: в одной находятся элементы, которые не меньше медианы,
# в другой – не больше медианы. Задачу можно решить без сортировки исходного массива.
# Но если это слишком сложно, то используйте метод сортировки, который не рассматривался на уроках.

from random import randint
from statistics import median


arr = [randint(1,100) for _ in range(21)] #m =10, честно-честно!
pivot = median(arr) # Ну как бы вот... ))) без сортировки
print(f'Несортированный список {arr}\nСортированный для удобства {sorted(arr)}\nМедиана {pivot}')
# Боюсь данное решение вас не удовлетворит, поэтому решу задачу без использования "модульной магии" ))

def prehistoricMedianSearch(arr):
    arr1 = [i for i in arr[:(len(arr)//2):]]
    arr2 = [i for i in arr[(len(arr)//2)+1::]]
    tempMed = arr[(len(arr)//2)]
    delta = (max(arr)-min(arr))//2
    i = 0
    while i < len(arr1):
        if arr1[i] > delta:
            arr2.append(arr1.pop(i))
        else: i += 1

    i = 0
    while i < len(arr2):
        if arr2[i] < delta:
            arr1.append(arr2.pop(i))
        else: i += 1

    if len(arr1) > len(arr2):
        for i in range(len(arr)//2 - len(arr2)):
            peek = arr1.index(max(arr1))
            arr2.insert(0,arr1.pop(peek))

    if len(arr1) < len(arr2):
        for i in range(len(arr)//2 - len(arr1)):
            peek = arr2.index(min(arr2))
            arr1.insert(0,arr2.pop(peek))

    if tempMed > delta:
        arr2[arr2.index(min(arr2))],tempMed = tempMed, arr2[arr2.index(min(arr2))]
        return f'Первая часть списка: {sorted(arr1)} Медиана: {tempMed} Вторая часть списка: {sorted(arr2)}'

    elif tempMed < delta:
        arr1[arr1.index(max(arr1))], tempMed = tempMed, arr1[arr1.index(max(arr1))]
        return f'Первая часть списка: {sorted(arr1)} Медиана: {tempMed} Вторая часть списка: {sorted(arr2)}'

    else:
        return f'Первая часть списка: {sorted(arr1)} Медиана: {tempMed} Вторая часть списка: {sorted(arr2)}'

print(prehistoricMedianSearch(arr))

