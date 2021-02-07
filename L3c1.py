# -*- coding: utf8 -*-

# Задание 1
def division(arg1 = int(input('Введите делимое: ')), arg2 = int(input('Введите делитель: '))):
    try:
        print(round(arg1 / arg2, 2))
    except:
        print("Деление на 0. На ноль делить нельзя")


division()
