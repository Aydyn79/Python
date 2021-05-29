# -*- coding: utf8 -*-
'''
Реализовать класс Road (дорога), в котором определить атрибуты: length (длина), width (ширина).
Значения данных атрибутов должны передаваться при создании экземпляра класса.
Атрибуты сделать защищенными. Определить метод расчета массы асфальта,
необходимого для покрытия всего дорожного полотна.
Использовать формулу: длина * ширина * масса асфальта для покрытия одного кв метра дороги асфальтом,
толщиной в 1 см * чи сло см толщины полотна. Проверить работу метода.
Например: 20м * 5000м * 25кг * 5см = 12500 т
'''
class Road:

    def __init__(self, length, width):
            self._lenght = length
            self._width = width

    def get_lenght(self):
        return self._lenght

    def get_width(self):
        return self._width

    def calc_mass(self, thick, mass=25):
        self.thick = thick/100
        self.mass = mass
        return [int(self.thick*100), round(self._lenght*self._width*self.thick*self.mass/1000, 2)]
    
try:
    a = Road(int(input('Введите числовое значение длины в метрах: ')), int(input('Введите числовое значение ширины в метрах: ')))

except ValueError:
    print('Неверное значение, введите числовые значения длины и ширины')
    a = Road(float(input('Введите числовое значение длины в метрах: ')),
    float(input('Введите числовое значение ширины в метрах: ')))

print(f'Масса асфальта необходимого для укладки дороги длиной {a.get_lenght()} метров,'
      f'\nшириной {a.get_width()} метров и толщиной {a.calc_mass(5, 36)[0]} см '
      f'составляет: {a.calc_mass(5, 36)[1]} т')#Фух, как долго я пытался вывести толщину! И через a.thick пытался, и через a.get_thick(функцию писал),
                                                #и определял в init (кстати рабочий вариант, только согласно условию в инит должны заводиться 2 параметра)
                                                #вобщем хлебнул опыта, пока не додумался через a.calc_mass вывести.))
print(f'Масса асфальта необходимого для укладки дороги составляет: {a.calc_mass(6)[1]}')