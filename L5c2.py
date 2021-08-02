# -*- coding: utf8 -*-
from icecream import ic

#Задание №2
# Написать программу сложения и умножения двух шестнадцатеричных чисел.
# При этом каждое число представляется как массив, элементы которого это цифры числа.
# Например, пользователь ввёл A2 и C4F. Сохранить их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’] соответственно.
# Сумма чисел из примера: [‘C’, ‘F’, ‘1’], произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].

def frHxToDc(x):
    frHxToDc = []
    list_of_numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']
    for i in x:
        one = list_of_numbers.index(i)
        frHxToDc.append(one)
    tenn = 0
    for i in range(len(frHxToDc)):
        ll = len(frHxToDc) - i - 1
        s = 16 ** ll
        ten = int(frHxToDc[i]) * s
        tenn += ten
    return tenn

def sum(x,y):
    list_of_numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']
    third = []
    k = 0
    j = 0
    for i in x:
        one = list_of_numbers.index(i)
        two = list_of_numbers.index(y[j])
        j += 1
        third.append(list_of_numbers[(one + two + k) % 16])
        if (one + two) >= 15:
            k = 1
        else:
            k = 0
    if k == 1:
        third.append('1')
    print(f'Сумма чисел: {third[::-1]}')
    return third[::-1]

def mult(x,y):
    x = frHxToDc(x)
    y = frHxToDc(y)
    z = str(hex(x*y))
    result = [i.upper() for i in z[2:len(z)+1:]]
    print(f'Произведение чисел: {result}')
    return result #Схалявил, простите.. Обязуюсь в скором времени допилить нормальную функцию умножения

n = list(input('Введите первое число ').upper())
m = list(input('Введите второе число ').upper())
n = n[::-1]
m = m[::-1]
if len(n) > len(m):
    for i in range(len(n) - len(m)):
        m.append('0')
else:
    for i in range(len(m) - len(n)):
        n.append('0')

sum(n,m)
mult(n,m)
