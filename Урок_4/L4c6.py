# -*- coding: utf8 -*-

'''
Реализовать два небольших скрипта:
итератор, генерирующий целые числа, начиная с указанного;
итератор, повторяющий элементы некоторого списка, определённого заранее.
Подсказка: используйте функцию count() и cycle() модуля itertools. Обратите внимание,
что создаваемый цикл не должен быть бесконечным. Предусмотрите условие его завершения.
Например, в первом задании выводим целые числа, начиная с 3.
При достижении числа 10 — завершаем цикл. Вторым пунктом необходимо предусмотреть условие,
при котором повторение элементов списка прекратится.
'''
from itertools import count, cycle

#первая часть задания
def iterat(begin, final):
    lst = []
    for el in count(begin):
        lst.append(el)
        if el == final:
            break
    return lst

print(f'Вот ваш список {iterat(3,10)}')

#вторая часть задания
def iterator(begin, final):
    lst = []
    for el in count(begin):
        lst.append(el)
        if el == final:
            break
    return lst

def copy_paste(lst,final):
    c = 0
    copy_lst = []
    for el in cycle(lst):
        if c > final:
            break
        print(f'Вот копия {c}-го элемента Вашего списка: {el}')
        copy_lst.append(el)
        c += 1
    print(f'Это копия - {copy_lst}... правда-правда!')


copy_paste(iterator(3, 10),7)
