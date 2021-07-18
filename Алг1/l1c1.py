# -*- coding: utf8 -*-
#Задание №1
# Найти сумму и произведение цифр трехзначного числа, которое вводит пользователь.
#Вариант первый, простой.
temp = input('Введите трёхзначное число ')
if temp.isdigit():
    a = int(temp[0])
    b = int(temp[1])
    c = int(temp[2])
    print(f'сумма {a + b + c}')
    print(f'сумма {a * b * c}')
else:
    print(f'Вы ввели неверное значение {temp}')

# Вариант второй - не отстанет пока не введешь правильное значение.
a = 1
while a == 1:
    temp = input('Введите трёхзначное число ')
    if temp.isdigit():
        a = int(temp[0])
        b = int(temp[1])
        c = int(temp[2])
        print(f'сумма {a + b + c}')
        print(f'сумма {a * b * c}')
        break
    else: print('Вы ввели неверный формат числа')

