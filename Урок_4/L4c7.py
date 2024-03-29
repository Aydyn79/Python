# -*- coding: utf8 -*-

'''
Реализовать генератор с помощью функции с ключевым словом yield,
создающим очередное значение. При вызове функции должен создаваться объект-генератор.
Функция вызывается следующим образом: for el in fact(n).
Она отвечает за получение факториала числа.
В цикле нужно выводить только первые n чисел, начиная с 1! и до n!.

Подсказка: факториал числа n — произведение чисел от 1 до n.
Например, факториал четырёх 4! = 1 * 2 * 3 * 4 = 24
'''
from math import factorial


def fact(n):
    b = 1
    for i in range(1, n+1):
        b *= i
        yield b

def factor_2(n):
    for i in range(1, n+1):
        yield factorial(i)


for el in fact(5):
    print(el)

for el in factor_2(5):
    print(el)
