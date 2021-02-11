# -*- coding: utf8 -*-

'''
Реализовать скрипт, в котором должна быть предусмотрена функция расчёта заработной платы сотрудника.
Используйте в нём формулу: (выработка в часах*ставка в час) + премия.
Во время выполнения расчёта для конкретных значений
необходимо запускать скрипт с параметрами.
'''


from sys import argv
from math import floor

def trunc_flo(x):
    return int((x - floor(x))*100)

def salary(argv):
    path_name, man_hour, tarif, bonus = argv
    salr = round(int(man_hour)*float(tarif) + float(bonus),2)
    print(f'Ваша зарплата:{round(salr)} руб. {trunc_flo(salr)} коп.')
    return round(int(man_hour)*float(tarif) + float(bonus), 2)

salary(argv)

print(argv)