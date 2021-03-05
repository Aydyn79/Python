# -*- coding: utf8 -*-
'''
3. Создайте собственный класс-исключение, который должен проверять содержимое списка на наличие только чисел.
Проверить работу исключения на реальном примере. Необходимо запрашивать у пользователя данные и заполнять список.
Класс-исключение должен контролировать типы данных элементов списка.
'''

class OnlyCifer(Exception):
    def __init__(self, only_digit, message):
        self.no_more_letters = only_digit
        self.message = message

    def __str__(self):
        return f'{self.message} --> {self.no_more_letters}'


lst = []
while True:
    try:
        digit = input('Введите число: ')
        if digit == 's':
            break
        if digit.isdigit():
            lst.append(int(digit))
        else:
            raise OnlyCifer(digit, 'Буквам не место в нашем списке')
    except OnlyCifer as err:
        print(err)


print(lst)




