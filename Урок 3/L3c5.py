# -*- coding: utf8 -*-
'''
Программа запрашивает у пользователя строку чисел, разделённых пробелом.
При нажатии Enter должна выводиться сумма чисел.
Пользователь может продолжить ввод чисел, разделённых пробелом и снова нажать Enter.
Сумма вновь введённых чисел будет добавляться к уже подсчитанной сумме.
Но если вместо числа вводится специальный символ, выполнение программы завершается.
Если специальный символ введён после нескольких чисел, то вначале нужно добавить сумму
этих чисел к полученной ранее сумме и после этого завершить программу.
'''

#без всяких проверок и фокусов
# def zamoroch():
#     summ = sum([int(i) for i in input('Введите цифры через пробел ').split()])
#     print(summ)
#     zamoroch()
#
# zamoroch()

#функция эволюционирует
# def summ():
#     sum_var= sum([int(i) for i in input('Введите цифры через пробел ').split()])
#     print(sum_var)
#     while True:
#         if input("Изволите'с продолжить? д/н ") == 'н':
#             return sum_var
#         else:
#             return summ()
#
# summ()

#обрастает внешним списком, который я пока не знаю как сделать внутреним
# sum_lst = []
# def summ():
#     sum_var = sum([int(i) for i in input('Введите цифры через пробел ').split()])
#     sum_lst.append(sum_var)
#     while input("Изволите'с продолжить? д/н ") != 'н':
#         print(sum(sum_lst))
#         return summ()
#     print(sum(sum_lst))
#     return sum(sum_lst)
#
# summ()

#избавился от рекурсии, ну её!
# def summ():
#     sum_lst = []
#     while True:
#         sum_var = sum([int(i) for i in input('Введите цифры через пробел ').split()])
#         sum_lst.append(sum_var)
#         print(sum(sum_lst))
#         if input("Изволите'с продолжить? д/н ") == 'н':
#             print('Не смею Вас больше беспокоить.')
#             return None
#
#
# summ()

#ну всё, вроде конечный вариант, а нет... посмотрел запись вебинара и передумал.
# def summ():
#     sum_lst = []
#     char_spec = ['#', '$', '^', '!', '&', '*', '(', ')', '|', '/'] #спец.символы
#     while True:
#         sum_var = list(input('Введите цифры, пробелы список сам поставит: '))#устал я через пробел вводить
#         for i in sum_var:
#             if i not in char_spec:
#                 sum_lst.append(int(i))
#             else:
#                 print(sum(sum_lst))
#                 return
#         print(sum(sum_lst))
#         if input("Изволите'с продолжить? д/н ") == 'н':
#             print('Не смею Вас больше беспокоить.')
#             return
#
#
# summ()

def summ():
    sum_lst = []
    while True:
        sum_var = list(input('Введите цифры, пробелы список сам поставит: '))#устал я через пробел вводить ^
        for i in sum_var:
            try:
                if i.isdigit():
                    sum_lst.append(int(i))
            finally:
                if i.isalpha() or ord(i) in [33, 35, 36, 38, 38, 40, 41, 42, 43, 44, 44, 45, 47, 58, 59, 60, 62, 63, 64, 94, 124]:
                    #!!! Подскажите на разборе ДЗ как проверить принадлежность переменной вышеуказанным символам
                    #менее трудозатратным способом.
                    print('Был введен неверный символ')
                    print(sum(sum_lst))
                    return
        print(sum(sum_lst))
        if input("Изволите'с продолжить? д/н ") == 'н':
            print('Не смею Вас больше беспокоить.')
            return


summ()