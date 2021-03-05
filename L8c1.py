# -*- coding: utf8 -*-
'''
1. Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде
строки формата «день-месяц-год». В рамках класса реализовать два метода. Первый, с
декоратором @classmethod. Он должен извлекать число, месяц, год и преобразовывать их тип
к типу «Число». Второй, с декоратором @staticmethod, должен проводить валидацию числа,
месяца и года (например, месяц — от 1 до 12). Проверить работу полученной структуры на
реальных данных.
'''


if __name__ == '__main__':
    class Data:
        def __init__(self, dat):
            self.dat = dat

        def __str__(self):
            return (f"{self.dat[0]}/{self.dat[1]}/{self.dat[2]}")

        # @classmethod
        # def get_dat_frm_str(cls, date_as_string):
        #     if not isinstance(self.dat, str):
        #         while not isinstance(self.dat, str):
        #             print(f'Wrong type of date, must be "str" entered {type(self.dat)}')
        #             self.dat = input('Введите дату в виде строки формата «дд-мм-гггг»')

        @classmethod
        def get_dat_frm_str(cls, date_as_string):
            return cls(list(map(int, date_as_string.split('-'))))


        @staticmethod
        def is_date_valid(date_as_string):
            day, month, year = map(int, date_as_string.split('-'))
            if 1 <= day <= 31 and 1 <= month <= 12 and 1 <= year <= 3999:
                return '/'.join(date_as_string.split('-'))
            else: return f'Неправильно введена дата'


        @staticmethod #забавы ради ещё одна версия метода проверяющая правильность даты
        def is_date_right(date_lk_string):
            temp = list(date_lk_string.split('-'))
            date = ''
            if 1 <= int(temp[0]) <= 31:
                date += temp[0]+'/'
            else: date += f'Неправильно введен день - {temp[0]} /'
            if 1 <= int(temp[1]) <= 12:
                date += temp[1]+'/'
            else: date += f'Неправильно введен месяц - {temp[1]} /'
            if 1 <= int(temp[2]) <= 3999:
                date += temp[2]
            else: date += f'Неправильно введен год - {temp[2]}'
            return date


        def justFunc(self):
            return Data.is_date_valid(self.dat)
#проверка функции get_dat_frm_str
    z = Data.get_dat_frm_str('23-02-2003')
    print(z)
#проверка функции is_date_valid
    a = Data('30-13-2056')
    x = a.is_date_valid('25-06-2027')
    f = a.justFunc() #Проверка функции-посредника
    g = Data.is_date_valid('32-13-4055')
    print(f'g = {g},x = {x},f = {f}')
# проверка функции is_date_right
    u = Data.is_date_right('32-13-2054')
    print(u)
