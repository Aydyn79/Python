# -*- coding: utf8 -*-
'''
Выполнить функцию, которая принимает несколько параметров,
описывающих данные пользователя: имя, фамилия, год рождения,
город проживания, email, телефон. Функция должна принимать
параметры как именованные аргументы.
Осуществить вывод данных о пользователе одной строкой.
'''


def mini_biograf(name:str, surname:str, year_bd:int, city:str, phone:int, email:str):
    dic = {'имя': name, 'фамилия': surname, 'год рождения': year_bd, 'город прож.': city, 'номер_телефона': phone, 'почта': email}
    print(dic)
    return dic
mini_biograf('Иван', 'Иванов', 1982, 'Томск', 89138755649, 'fdg@mail.com')

#def mini_biograf(name:str, surname:str, year_bd:int, city:str, phone:int, email:str):
    #return {'имя': name, 'фамилия': surname, 'год рождения': year_bd, 'город прож.': city, 'номер_телефона': phone, 'почта': email}
#print(mini_biograf('Иван', 'Иванов', 1982, 'Томск', 89138755649, 'fdg@mail.com'))


def print_biograf(name, surname, year_bd, city, phone, email, **additional):
    print(f'Имя: {name}, Фамилия: {surname}, год рождения: {year_bd}, город проживания: {city}, номер_телефона: {phone}, электронная почта: {email}'+',', ', '.join(['{0}: {1}'.format(k, v) for k,v in additional.items()]))


print_biograf(name ='Иван', surname = 'Иванов', year_bd = 1982, city = 'Томск', phone = 89138755649, email = 'fdg@mail.com', Семейн_пол = 'холост', Отчество = 'Иваныч', Что_нибудь_эдакое = 'Утром ходит без штанов')

