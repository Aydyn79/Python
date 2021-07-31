# -*- coding: utf8 -*-
#Задание №1
# Проанализировать скорость и сложность одного любого алгоритма, разработанных в рамках домашнего задания первых трех уроков.


import timeit
# mysetup = 'from random import randint'
# mycode = '''temp = [randint(0,30) for _ in range(25)]
# tamp = []
# for i,j in enumerate(temp):
#     cnt = temp.count(temp[i])
#     tamp.append(cnt)
#     cnt = 0
# print(f'Чаще всего в массиве {temp} встречается число "{temp[tamp.index(max(tamp))]}" - {max(tamp)} раза')'''
# print('Лучшее время выполнения:', timeit.timeit(setup=mysetup, stmt=mycode, number=1000), 'cекунды') #Линейная сложность основного цикла

def bar(n):
    if n == 0:
        return 0
    return n + bar(n - 1)

def foo(n):
    return sum([i for i in range(n+1)]) #цикл for оказался намного шустрее рекурсии и цикла while

def foowh(n):
    a = 0
    while n != 0:
        a += n
        n -= 1
    return a

# print(f'Время выполнения рекурсии: {timeit.timeit("[bar(i) for i in range(5,10)]", globals=globals())}') #9.53 сек.
# print(f'Время выполнения рекурсии: {timeit.timeit("[bar(i) for i in range(15,20)]", globals=globals())}') #20.479 сек.
# print(f'Время выполнения рекурсии: {timeit.timeit("[bar(i) for i in range(50,80)]", globals=globals())}') #470.759 сек.

for i in range(10,50,10):
    print(f'Время выполнения рекурсии, где i = {i}: {timeit.timeit("bar(i)", globals=globals())}') #Линейная сложность
for i in range(10,50,10):
    print(f'Время выполнения рекурсии, где i = {i}: {timeit.timeit("foo(i)", globals=globals())}') #Линейная сложность
for i in range(10,50,10):
    print(f'Время выполнения рекурсии, где i = {i}: {timeit.timeit("foowh(i)", globals=globals())}') #Линейная сложность

# print(bar(20), foo(20), foowh(20))