# -*- coding: utf8 -*-

# Задание №6
# Пользователь вводит номер буквы в алфавите. Определить, какая это буква.
try:
    temp = int(input('Введите номер буквы '))
except ValueError:
    print('Вы ввели не число. Выходим.')
alphabet = 'abcdefghijklmnopqrstuvwxyz'
print(f'Это буква {alphabet[temp - 1]}')

