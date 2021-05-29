# -*- coding: utf8 -*-
'''
5. Реализовать класс Stationery (канцелярская принадлежность). Определить в нем атрибут title (название) и метод draw (отрисовка).
Метод выводит сообщение “Запуск отрисовки.” Создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер).
В каждом из классов реализовать переопределение метода draw. Для каждого из классов методы должен выводить уникальное сообщение.
Создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра.
'''

class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        print('Запуск отрисовки')
        print('  ___')
        print(' / \/')
        print('/\ /')
        print('---')

class Pen(Stationery):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        print('Рисуем ручку!')
        print('    ___')
        print('   / /')
        print('  / /')
        print('  |/')
        print('  !')


class Pencil(Stationery):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        print('Рисуем карандаш!')
        print('   ___')
        print('  /  /')
        print(' /  /')
        print(' | /')
        print(' |/ ')

class Handle(Stationery):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        print('Рисуем маркер!')
        print('   ____')
        print('  /   /')
        print(' /___/')
        print(' |__/')
        print(' |_/ ')

a = Stationery('Скрепка')
a.draw()

pe = Pen('Ручка')
pe.draw()

pens = Pencil('Карандаш')
pens.draw()

hand = Handle('Маркер')
hand.draw()