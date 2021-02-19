# -*- coding: utf8 -*-
'''
3. Реализовать базовый класс Worker (работник), в котором определить атрибуты:
name, surname, position (должность), income (доход).
Последний атрибут должен быть защищенным и ссылаться на словарь, содержащий элементы:
оклад и премия, например, {"wage": wage, "bonus": bonus}.
Создать класс Position (должность) на базе класса Worker.
В классе Position реализовать методы получения полного имени сотрудника (get_full_name)
и дохода с учетом премии (get_total_income). Проверить работу примера на реальных данных
(создать экземпляры класса Position, передать данные, проверить значения атрибутов, вызвать методы экземпляров).
'''
class Worker:
    def __init__(self, name, surname, position, *income):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = [i for i in income[0].values()][0] + [i for i in income[0].values()][1] #Сколько я информации перелопатил ради этой одной строчки! А сколько нового узнал!)))
        #то что у меня словарь income в кортеж "завёрнут", вообще случайно узнал ))
        # Уделите пожалуйста побольше времени на разборе ДЗ, способам присваивания атрибутам класса значений из *arg, **kwarg где аргументами являются словари, кортежи и вложенные списки
        #Потому что, это целое море новой и нужной информации, которая на уроке не разбиралась.
       
        

class Position(Worker):
    def __init__(self, name, surname, position, *income):
        super().__init__(name, surname, position, *income)
        

    def get_full_name(self):
        return f'Полное имя сотрудника: {self.name} {self.surname}'

    def get_total_income(self):
        return f'Зарплата сотрудника {self.name}а {self.surname}а составляет: {self._income} евро'


b = Position('Иван', 'Иванов', 'Инженер', {"wage": 10000, "bonus": 10440})
print(b.name)
print(b.surname)
print(b.position)
print(b._income)
print(b.get_full_name())
print(b.get_total_income())

