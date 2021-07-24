# -*- coding: utf8 -*-
#Задание №8
# Матрица 5x4 заполняется вводом с клавиатуры кроме последних элементов строк.
# Программа должна вычислять сумму введенных элементов каждой строки и записывать
# ее в последнюю ячейку строки. В конце следует вывести полученную матрицу.

def sbmtrx(n):
    sbmtrx = []
    i = 0
    while i != n-1:
        a = int(input('Введите число '))
        sbmtrx.append(a)
        i += 1
    sm = sum(sbmtrx)
    sbmtrx.append(sm)
    return sbmtrx

from numpy import matrix
mtrx = []
for i in range(4):
    mtrx.append(sbmtrx(5))
print(f'Вот Ваша матрица: \n {matrix(mtrx)}')