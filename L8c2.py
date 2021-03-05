# -*- coding: utf8 -*-
'''
2. Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль.
Проверьте его работу на данных, вводимых пользователем. При вводе пользователем нуля
в качестве делителя программа должна корректно обработать эту ситуацию и не завершиться с ошибкой.
'''

class MyError(Exception):
    def __init__(self,divisible,divisor):
        self.divisible = divisible
        self.divisor = divisor

    def __str__(self):
        wrong_type1 = ''
        wrong_type2 = ''
        wrong_value = ''

        if isinstance(self.divisible, str):
            wrong_type1 = 'Неверный тип делимого'

        if isinstance(self.divisor, str):
            wrong_type2 = 'Неверный тип делителя'

        if self.divisor == 0:
            wrong_value = 'Делить на ноль нельзя'

        return f'{wrong_type1} {wrong_type2} {wrong_value}'

try:
    divisible, divisor = 12, '0'
    raise MyError(divisible, divisor)
except MyError:
            print(MyError(divisible, divisor))


try:
    divisible, divisor = '12', 0
    if isinstance(divisible, int) and isinstance(divisor, int) and divisor != 0:
        print( divisible/divisor)
    else:
        raise MyError(divisible, divisor)
except MyError:
            print(MyError(divisible, divisor))

