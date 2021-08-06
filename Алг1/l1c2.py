# -*- coding: utf8 -*-
#Задание №2
# Выполнить логические побитовые операции "И", "ИЛИ" и др. над числами 5 и 6.
# Выполнить над числом 5 побитовый сдвиг вправо и влево на два знака.
try:
    a,b = map(int, input('Введите через пробел два числа ').split())
except ValueError:
    print('Это не число. Выходим.')
print(f'Цифра {a} в двоичном представлении {bin(a)}')
print(f'Цифра {b} в двоичном представлении {bin(b)}')
print(f'Binary AND {bin(a & b)} : {a & b}')
print(f'Binary OR {bin(a | b)} : {a | b}')
print(f'Binary XOR {bin(a ^ b)} : {a ^ b}')
print(f'Inversion {bin(~a)}, {bin(~b)} : {~a}, {~b}')
print(f'Binary left shift by 2: {bin(a << 2)} : {a << 2}')
print(f'Binary right shift by 2: {bin(a >> 2)} : {a >> 2}')

