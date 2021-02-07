# -*- coding: utf8 -*-

#Задание 4
User_str = input('Введите слова через пробел: ').split()

for i,j in enumerate(User_str, 1):
    if len(j) > 10:
        print(i, j[:10:])
    else:
        print(i, j)