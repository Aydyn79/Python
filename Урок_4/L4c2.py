# -*- coding: utf8 -*-


'''
Представлен список чисел. Необходимо вывести элементы исходного списка, значения которых больше предыдущего элемента.
Подсказка: элементы, удовлетворяющие условию, оформить в виде списка. Для его формирования используйте генератор.
Пример исходного списка: [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55].
Результат: [12, 44, 4, 10, 78, 123].
'''
#from sys import argv
# from L4c1 import salary #Привет из первого задания! У меня всё работает!
# salary(argv = ['C:/Users/Администратор/Desktop/Обучение/Python/Урок_4/L4c7.py', 2, 2, 4561]) # но как то странно, получается, что выводится два результата.
#Т.е. и строка (from L4c1 import salary) автоматически запускает функцию salary и salary(argv = ['C:/Us..]) тоже выводит?

a = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
def strange_sort(a):
    return [a[i] for i in range(1,len(a)-1) if a[i] > a[i - 1]]


print(f'Вот Ваш отсортированный список: {strange_sort([300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55])}')