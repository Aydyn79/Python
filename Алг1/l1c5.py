# -*- coding: utf8 -*-

# Задание №5
# Пользователь вводит две буквы. Определить, на каких местах алфавита они стоят, и сколько между ними находится букв.

temp = input('Введите две произвольные буквы ')
lit1 = temp[0].lower()
lit2 = temp[1].lower()

alphabet = 'abcdefghijklmnopqrstuvwxyz'
if lit1.isalpha() and lit2.isalpha():
    print(f'{lit1} это {alphabet.find(lit1) + 1}-я буква английского алфавита')
    print(f'{lit2} это {alphabet.find(lit2) + 1}-я буква английского алфавита')
    print(f'Между ними {abs(alphabet.find(lit2) - alphabet.find(lit1))-1} букв')
else:
    print('Вы ввели не буквы')



