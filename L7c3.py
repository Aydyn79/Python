# -*- coding: utf8 -*-
'''
3. Реализовать программу работы с органическими клетками. Необходимо создать класс Клетка.
В его конструкторе инициализировать параметр, соответствующий количеству клеток (целое число).
В классе должны быть реализованы методы перегрузки арифметических операторов: сложение (__add__()),
вычитание (__sub__()), умножение (__mul__()), деление (__truediv__()).
Данные методы должны применяться только к клеткам и выполнять увеличение, уменьшение, умножение и
обычное (не целочисленное) деление клеток, соответственно. В методе деления должно осуществляться
округление значения до целого числа.
Сложение. Объединение двух клеток. При этом число ячеек общей клетки должно равняться сумме ячеек исходных двух клеток.
Вычитание. Участвуют две клетки. Операцию необходимо выполнять только если разность количества ячеек двух клеток
больше нуля, иначе выводить соответствующее сообщение.
Умножение. Создается общая клетка из двух. Число ячеек общей клетки определяется как произведение количества ячеек этих двух клеток.
Деление. Создается общая клетка из двух. Число ячеек общей клетки определяется как целочисленное деление количества ячеек этих двух клеток.

В классе необходимо реализовать метод make_order(), принимающий экземпляр класса и количество ячеек в ряду.
Данный метод позволяет организовать ячейки по рядам.
Метод должен возвращать строку вида *****\n*****\n*****..., где количество ячеек между \n
равно переданному аргументу. Если ячеек на формирование ряда не хватает, то в последний ряд записываются все оставшиеся.
Например, количество ячеек клетки равняется 12, количество ячеек в ряду — 5. Тогда метод make_order() вернет строку: *****\n*****\n**.
Или, количество ячеек клетки равняется 15, количество ячеек в ряду — 5. Тогда метод make_order() вернет строку: *****\n*****\n*****.
'''


class Cell:
    def __init__(self, quantity):
        self.quantity = quantity

    def __str__(self):
        return f'Новая клетка занимает {self.quantity}'

    def __add__(self, other):
        if str(other.__class__.__name__) == 'Cell':
            return Cell(self.quantity + other.quantity)
        else:
            print('wrong class')

    def __sub__(self, other):
        if str(other.__class__.__name__) == 'Cell':
            if self.quantity - other.quantity >= 0:
                return Cell(self.quantity - other.quantity)
            else:
                return f'Результат {self.quantity - other.quantity} меньше нуля'
        else:
            print('wrong class')


    def __mul__(self, other):
        if str(other.__class__.__name__) == 'Cell':
            return Cell(int(self.quantity * other.quantity))
        else:
            print('wrong class')

    def __truediv__(self, other):
        if str(other.__class__.__name__) == 'Cell':
            return Cell(int(self.quantity / other.quantity))
        else:
            print('wrong class')

    def make_order(self, cell):
        self.cell = list('*' * cell)
        for i in range(0, len(self.cell), 5):
            five_nums = ' '.join(self.cell[i:i + 5])
            print('{}\n'.format(five_nums))

#Тестовый класс
class Virus:
    def __init__(self, quantity):
        self.quantity = quantity



a = Cell(45)
b = Cell(3)
c = Cell(6)
d = Virus(6)
print(a + b + b)
print(a + b + d)
print(a - b - c)
print(a - c - d)
print(a * b * c)
print((a / b) / c)
a.make_order(17)
a + d
a + 5
