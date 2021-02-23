# -*- coding: utf8 -*-
'''
2. Реализовать проект расчета суммарного расхода ткани на производство одежды.
Основная сущность (класс) этого проекта — одежда, которая может иметь определенное название.
К типам одежды в этом проекте относятся пальто и костюм. У этих типов одежды существуют параметры:
размер (для пальто) и рост (для костюма). Это могут быть обычные числа: V и H, соответственно.
Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто (V/6.5 + 0.5),
для костюма (2 * H + 0.3). Проверить работу этих методов на реальных данных.
Реализовать общий подсчет расхода ткани. Проверить на практике полученные на этом уроке знания:
реализовать абстрактные классы для основных классов проекта, проверить на практике работу декоратора @property.
'''
from abc import ABC, abstractmethod

class Clothes(ABC):

    @abstractmethod
    def calcMaterial(self):
        pass

class Coat(Clothes):
    def __init__(self, v):
        self.coat = v


    @property
    def coat(self):
        return self._coat

    @coat.setter
    def coat(self, size):
        if size < 50:
            self._coat = 50
        elif 50 <= size < 100:
            self._coat = 75
        else:
            self._coat = size

    def calcMaterial(self):
        print(f'Расход ткани на Ваше пальто будет: {round(self.coat/6.5 + 0.5, 2)}')
        return round(self.coat/6.5 + 0.5, 2)




class Suit(Clothes):
    def __init__(self, h=int(input('Введите свой рост: '))):
        self.suit = h

    @property
    def calcMaterial(self):
       return 2 * self.suit + 0.3

a = Coat(48)
c = Coat(51)
b = Suit()

print(f'Ваш приближённый размер пальто {a.coat}. Ну и что, что не Ваш размер?! Программа такая! ))')
a.calcMaterial()
c.calcMaterial()
print(f'На Ваш костюм понадобится {b.calcMaterial} погонных метров ткани')
print(f'Всего ткани уйдет {a.calcMaterial() + b.calcMaterial}')