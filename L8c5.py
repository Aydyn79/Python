# -*- coding: utf8 -*-
'''
7. Реализовать проект «Операции с комплексными числами». Создайте класс «Комплексное
число». Реализуйте перегрузку методов сложения и умножения комплексных чисел. Проверьте
работу проекта. Для этого создаёте экземпляры класса (комплексные числа), выполните
© geekbrains.ru 17сложение и умножение созданных экземпляров. Проверьте корректность полученного
результата
'''
class ComplexOperation:
    def __init__(self, param):
        self.param = param

    def __add__(self, other):
        real = self.convert()[0] + other.convert()[0]
        imag = self.convert()[1] + other.convert()[1]
        result = complex(real, imag)
        return ComplexOperation(str(result).replace(' ', '').replace('(', '').replace(')', ''))

    def __mul__(self, other):
        real = self.convert()[0] * other.convert()[0] - self.convert()[1] * other.convert()[1]
        imag = self.convert()[1] * other.convert()[0] + self.convert()[0] * other.convert()[1]
        result = complex(real, imag)
        return ComplexOperation(str(result).replace(' ', '').replace('(', '').replace(')', ''))

    def __truediv__(self, other):
        real = (self.convert()[0] * other.convert()[0] + self.convert()[1] * other.convert()[1])/(other.convert()[0]**2 + other.convert()[1]**2)
        imag = self.convert()[1] * other.convert()[0] - self.convert()[0] * other.convert()[1]/(other.convert()[0]**2 + other.convert()[1]**2)
        result = complex(real, imag)
        return ComplexOperation(str(result).replace(' ', '').replace('(', '').replace(')', ''))

    def __str__(self):
        return self.param

    def convert(self):
        if isinstance(self.param, complex):
            string = str(self.param).replace(' ', '').replace('(', '').replace(')', '')
        else:
            string = str(self.param)
        if string.rfind('-',1) != -1:
            suh = string.replace(' ', '')
            real = float(suh[:suh.rfind('-')])
            imag = float(suh[suh.rfind('-'):].split('j')[0])
            return real, imag
        elif string.find('+') != -1:
            suh = string.replace(' ', '')
            real = float(suh[:suh.find('+')])
            imag = float(suh[suh.find('+')+1:].split('j')[0])
            return real, imag
        else:
            if len(string.split(' ')) == 1:
                real = 0
                imag = int(string.split(' ')[0].split('j')[0])
                return real, imag
            else:
                return f'Введите знак +/- или удалите лишний пробел'


a = ComplexOperation('1-5j')
b = ComplexOperation('5+10j')
c = ComplexOperation('10+20j')
z = c+b+a
v = c*b*a
n = c/b/a
print(f'z {z},v {v},n {n}')
print(c.convert()[1]+b.convert()[1])

