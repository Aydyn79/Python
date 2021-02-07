# -*- coding: utf8 -*-
'''
Реализовать функцию my_func(), которая принимает три позиционных аргумента
и возвращает сумму наибольших двух аргументов.
'''

def my_foon(a,b,c):
    lst = [a,b,c]
    lst.sort(reverse=True)
    return lst[0] + lst[1]

print(my_foon(45,12,3))