# -*- coding: utf8 -*-
# from icecream import ic
from functools import reduce

# Задание №2
# Написать программу сложения и умножения двух шестнадцатеричных чисел.
# При этом каждое число представляется как массив, элементы которого это цифры числа.
# Например, пользователь ввёл A2 и C4F. Сохранить их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’] соответственно.
# Сумма чисел из примера: [‘C’, ‘F’, ‘1’], произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].
def summ(x, y):
    list_of_numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']
    third = []
    k = 0
    j = 0
    x = x[::-1]
    y = y[::-1]
    if len(x) > len(y):
        for i in range(len(x) - len(y)):
            y.append('0')
    else:
        for i in range(len(y) - len(x)):
            x.append('0')
    for i in x:
        one = list_of_numbers.index(i)
        two = list_of_numbers.index(y[j])
        j += 1
        third.append(list_of_numbers[(one + two + k) % 16])
        if (one + two + k) > 15:
            k = 1
        else: k = 0
    if k == 1:
        third.append('1')
    return third[::-1]


def mul(x, y):
    list_of_numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']
    third = [] #промежуточный список, куда складывается результат умножения
    mult = [] #список под окончательный результат
    k = 0
    j = 0
    x = x[::-1]# подготовка к обработке
    y = y[::-1]# подготовка к обработке
    for i in x:
        one = list_of_numbers.index(i) # перевожу 16-ные значения в 10-ные
        for j in range(len(y)):
            two = list_of_numbers.index(y[j])# перевожу 16-ные значения в 10-ные
            third.append(list_of_numbers[(one * two + k) % 16])
            if (one * two) >= 15:
                k = (one * two + k) // 16
            else:
                k = 0
        if k > 0:
            third.append(list_of_numbers[k])
            k = 0
        mult.append(third[::-1]) #добавляю вычисленное значение в основной массив
        third = []
    for i, j in enumerate(mult):
        j.extend(['0' for _ in range(1, i + 1)]) # смещаю регистры нижних чисел относительно верхних для последующего сложения
    return reduce(lambda prev, next_: summ(prev, next_), mult)



n = list(input('Введите первое число ').upper())
m = list(input('Введите второе число ').upper())
print(summ(n, m))
print(mul(n, m))
