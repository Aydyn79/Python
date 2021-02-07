# -*- coding: utf8 -*-
'''
Программа принимает действительное положительное число x и целое отрицательное число y.
Выполните возведение числа x в степень y. Задание реализуйте в виде функции my_func(x, y).
При решении задания нужно обойтись без встроенной функции возведения числа в степень.
Подсказка: попробуйте решить задачу двумя способами. Первый — возведение в степень с помощью оператора **.
Второй — более сложная реализация без оператора **, предусматривающая использование цикла.
'''


def my_func(a,b:int):
    if type(a) == float and b < 0:
        res = a**b
        return res
    else: print('Неправильно введено число!')

print(my_func(2.0,-4))

#рекурсия - зло
def exp_rec(b, n:int):
    if n == 0:
        return 1
    return 1 / b * exp_rec(b, abs(n) - 1)

print(exp_rec(2.0, -4))

#цикл for
def exp_for(b, n):
    temp = 1
    for i in range(0,abs(n)):
        temp *= b
    return 1/temp

print(exp_for(2, -4))



#цикл While
def exp_whi(b, n):
    err = 'Неправильно введено число!'
    clm = 'Основание введено неправильно - '
    clm1 = 'Степень введена неправильно - '
    temp = 1
    if type(b) == float and n < 0:
        while n != 0:
            temp *= b
            n += 1
        return 1/temp
    else:
        print(f'{err if type(b) != float or n >= 0 else ""}: {clm if type(b) != float else ""}{b if type(b) != float else ""},{clm1 if n >= 0 else ""}{n if n >= 0 else ""}')

print(exp_whi(2, 4))

