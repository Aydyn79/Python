# -*- coding: utf8 -*-
#Задание №9
# Найти максимальный элемент среди минимальных элементов столбцов матрицы.
from random import randint
from numpy import matrix

#Генерим матрицу 5*4
def sbstr():
    return [randint(0,100) for _ in range(5)]
mtrx = [sbstr() for _ in range(4)]
print(matrix(mtrx))

# Определяем лучшего из худших )
srv = []
for i,j in enumerate(mtrx):
    srv.append(min(j))
print(f'Максимальный элемент среди \nминимальных элементов столбцов матрицы '
      f'{max(srv)}')

