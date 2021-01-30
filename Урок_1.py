# -*- coding: utf8 -*-
import datetime


#Урок 1

#Задание один
a = 1
b = 'lesson'
c = int(input('Введите цифру '))
d = input('Введите слово ')
print(c, d, sep='-')
print(b, str(a))

#Задание два
sec = int(input('Введите количество секунд: '))
hour =  sec//3600
minute = (sec%3600)//60
second = (sec%3600)%60
print('{:0>2}'.format(hour),'{:0>2}'.format(minute), '{:0>2}'.format(second), sep=':')

#А можно не мучиться и сразу сделать в формате datetime:
timeobj= datetime.time(sec//3600,(sec%3600)//60,(sec%3600)%60 )
print(timeobj)

#Задание три
digit1 = input('Введите какое-нибудь число: ') 
digit2 = digit1 + digit1
digit3 = digit2 + digit1 
print('{} + {} + {}'.format(digit1, digit2, digit3), '=', int(digit1) + int(digit2) + int(digit3))

#Задание 4
digit = input('Введите целое положительное число: ') 
peak = 0
i = 0
while i < len(digit):
    if peak < int(digit[i]):
        peak = int(digit[i])
    i += 1
print(peak)

#Задание 5
profit = int(input('Введите значение выручки фирмы: '))
charge = int(input('Введите значение издержек фирмы: '))
if profit > charge:
    population = int(input('Численность сотрудников фирмы: '))
    print('Ваша фирма работает с прибылью, \nчистая прибыль составляет: {} рублей'.format(profit - charge), 
          '\nрентабельность: {}%'.format(round((profit/charge)*100, 2)), 
          '\nприбыль фирмы в расчете на одного сотрудника: {} руб/чел.'.format(round(profit/population, 2)))
else: print('Ваша фирма убыточна :((')

#Задание 6
result = int(input('Введите результат первого дня: '))
plan = int(input('Введите желаемый результат: '))
i = 2
print(f'1-й день: {result}')
while result < plan:
    result *= 1.1
    print(f'{i}-й день: {round(result, 2)}')
    i += 1
print(f'Ответ: на {i - 1}-й день спортсмен достиг результата — не менее {plan} км.')