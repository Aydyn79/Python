# -*- coding: utf8 -*-
from random import randint
# 1. Отсортируйте по убыванию методом "пузырька" одномерный целочисленный массив, заданный случайными числами на промежутке [-100; 100).
# Выведите на экран исходный и отсортированный массивы. Сортировка должна быть реализована в виде функции.
# По возможности доработайте алгоритм (сделайте его умнее).

arr = [randint(-100,100) for _ in range(0,20)]
print(arr)
def bubble(arr):
    for i in range(len(arr) - 1):
        for j in range(len(arr) - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr
print(bubble(arr))

def shaker(arr): # а ты танцуешь как дым, тудым-сюдым...)
    for i in range(len(arr) - 1):
        for j in range(len(arr) - i - 1):
            if j == (len(arr) - i - 1):
                for i in reversed(range(len(arr) - 1)):
                    for j in reversed(range(len(arr) - i - 1)):
                        if arr[j] < arr[j + 1]:
                            arr[j], arr[j + 1] = arr[j + 1], arr[j]
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr
print(shaker(arr))


def EvenOdd(arr):
    done = 0
    while done == 0:
        done = 1
        for j in range(0,len(arr) - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                done = 0
        for i in range(1, len(arr) - 1):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                done = 0
    return arr

print(EvenOdd(arr))


