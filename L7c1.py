# -*- coding: utf8 -*-
'''
1. Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод __init__()),
который должен принимать данные (список списков) для формирования матрицы.
Подсказка: матрица — система некоторых математических величин, расположенных в виде прямоугольной схемы.
Примеры матриц вы найдете в методичке.
Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде.
Далее реализовать перегрузку метода __add__() для реализации операции сложения двух объектов класса Matrix (двух матриц).
Результатом сложения должна быть новая матрица.
Подсказка: сложение элементов матриц выполнять поэлементно — первый элемент первой строки первой матрицы складываем
с первым элементом первой строки второй матрицы и т.д.
'''
import numpy as np

class Matrix:
    def __init__(self, income_list):
        self.array = income_list

    def __str__(self):
        temp = ''
        for i in range(len(self.array)):
            temp += " ".join(['{:<3}'.format(str(j)) for j in self.array[i]]) + '\n'
        return temp

    def __add__(self, other):
        temp_matr = self.array.copy() #Шаблон копирует формат нашей матрицы, значения не важны, они изменятся.
        #Последующие две строчки проверяют, чтобы складываемые матрицы были с одинаковым количеством строк и столбцов
        if len(self.array) == len(other.array):
            if [len(self.array[i]) for i in range(len(self.array))] == [len(other.array[i]) for i in range(len(other.array))]:
                #сложение двух списков
                for i in range(len(self.array)):
                    for j in range(len(self.array[i])):
                        temp_matr[i][j] = self.array[i][j] + other.array[i][j]
            else:
                print('Разное количество столбцов')
                return
        else:
            print('Разное количество строк')
            return
        return Matrix(temp_matr)

g = Matrix([[1,2,3],[14,15,16],[7,8,9]])
l = Matrix([[11,12,13],[4,5,6],[7,8,9]])
h = Matrix([[12,13],[4,5,6],[7,8,9]])
w = Matrix([[11,12,13],[7,8,9]])
print(np.array(l)) #Думал получится выровнять столбцы применив np.array, но не тут-то было! ))
print(g + l)
print(g + l + g)
print(g + l + h)
print(g + l + w)
#Функции __str__ и __add__ можно было бы сделать намного проще с Numpy, но это было бы слишком просто и неинтересно )





#Это черновик, не смотрите, для себя оставил.
# txt = [[121,2,23],[214,35,6],[7,8,9]]
# for x in txt:
#     print(f'{{:<5}{:<5}{:<5}.format(*x)}}')

#len_self = [len(c[i]) for i in range(len(c))]
#len_other = [len(b[i]) for i in range(len(b))]
#self.string = len(self.array)


# a = [[0,0,0],[0,0,0],[0,0,0]]
# c = [[1,2,3],[4,5,6],[7,8,9]]
# b = [[1,2,3],[4,5,6],[7,8,9]]

# for i in range(len(c)):
#     for j in range(len(c[i])):
#         a[i][j] = c[i][j] + b[i][j]
# print(a)
#
# len_colc = [len(c[i]) for i in range(len(c))]
# len_colb = [len(b[i]) for i in range(len(b))]
# print(f'{len_colc}' if len_colc == len_colb  else 'Матрицы разного формата')

# data = [[j * 0 for i in range(len(c))] for i in range(1) for j in c[i]]
# print(data)