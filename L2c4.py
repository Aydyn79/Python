# -*- coding: utf8 -*-
#Задание №4
#4. Найти сумму n элементов следующего ряда чисел: 1 -0.5 0.25 -0.125 ...
# Количество элементов (n) вводится с клавиатуры.

def symm(n):
    bamp = [1/2**i for i in range(0,n)]
    for i in range(1,len(bamp),2):
        bamp[i] = (-1)*bamp[i]
    print(f'сумма {n} элементов равна {sum(bamp)}, сам ряд вот такой: {bamp}')
    return None

symm(int(input('Введите количество элементов ')))
