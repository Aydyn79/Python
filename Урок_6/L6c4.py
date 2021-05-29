# -*- coding: utf8 -*-
import sys, os

import time
'''
4. Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда).
Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar. Добавьте в базовый класс метод show_speed,
который должен показывать текущую скорость автомобиля. Для классов TownCar и WorkCar переопределите метод show_speed.
При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
'''

class Car:

    def __init__(self, color, name, is_police = False, speed = 0, direction = 'forward'):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police
       
    def go(self):
        i = 0
        print(f'Машина поехала со скоростью {self.speed} км\ч' if self.speed > 0 else 'Сейчас поедет!')
        while i < 5:
            time.sleep(1)
            self.speed += 15
            print(f'Машина едет со скоростью {self.speed} км\ч' if self.speed > 0 else 'Щас-щас!')
            i += 1
            



    def stop(self):
        print(f'Машина останавливается на скорости {self.speed} км\ч' if self.speed > 0 else '')
        while self.speed > 0:
            time.sleep(1)
            self.speed -= 54
            print(f'Машина едет со скоростью {self.speed} км\ч' if self.speed > 0 else '')
        if self.speed <= 0:
            print('Машина остановилась!')

    def turn(self, direction):
        self.direction = direction
        if self.direction in ['left', 'right', 'reverse', 'forward']:
            if self.direction == 'left':
                print('Машина поворачивает налево')
            elif self.direction == 'right':
                print('Машина поворачивает направо')
            elif self.direction == 'forward':
                print('Машина едет прямо')
            elif self.direction == 'reverse':
                print('Машина едет назад')
                
    def show_how_i_fast(self):
        print(f'Ваша скорость {self.speed} км\ч' if self.speed > 0 else 'Вы не двигаетесь')
        
        

class TownCar(Car):
    
    def __init__(self, color, name, speed, is_police = False, direction = 'forward'):
        super().__init__(color, name, is_police, direction = 'forward')
        self.speed = speed
    
    def go(self):
        i = 0
        print(f'Машина поехала со скоростью {self.speed} км\ч' if self.speed > 0 else 'Сейчас поедет!')
        while i < 5:
            time.sleep(1)
            self.speed += 10
            print(f'Машина едет со скоростью {self.speed} км\ч' if self.speed > 0 else 'Щас-щас!')
            print( 'Превышение скорости!'if self.speed > 60 else '')
            i += 1



class WorkCar(Car):
    
    def __init__(self, color, name, speed, is_police = False, direction = 'forward'):
        super().__init__(color, name, direction = 'forward')
        self.speed = speed
        self.is_police = is_police
    
    def go(self):
        i = 0
        if self.speed > 0:
            print('Грузовик поехал со скоростью {} км\ч'.format(self.speed), end='\r')  
            print( 'Превышение скорости!', end='\r' if self.speed > 40 else '')
        for i in range(5):
            time.sleep(1)
            self.speed += i*2
            if self.speed > 0:
                print("Грузовик едет со скоростью: %d км\ч" % self.speed, file=sys.stdout, flush=True) #никак не получается выводить одной строкой на терминале скорость, что я делаю не так?
                
class PoliceCar(Car):
    
    def __init__(self, name, speed, is_police = True,  direction = 'forward', color = 'blue & white'):
        super().__init__(self, name, direction = 'forward')
        self.speed = speed
        self.color = color
        self.is_police = is_police
        
    
    def go(self):
        i = 0
        print(f'{self.color} {self.name} выехал на место со скоростью {self.speed} км\ч' if self.speed > 0 else 'Включаем мигалки и сирены...Уииуууу уиу уиу')
        while i < 5:
            time.sleep(1)
            self.speed += 25
            print(f'Экипаж мчится со скоростью {self.speed} км\ч' if self.speed > 0 else '')
            i += 1

                        
geely = TownCar('green', 'Geely grand M3', 65)
geely.go()

man = WorkCar('red','Mersedes Aktros', 45)
man.go()
man.stop()

ford = PoliceCar('Ford_Explorer', 100)
print(ford.color)
ford.go()
ford.show_how_i_fast()


bmw = Car('red','BMW_X5',True, 105)

if bmw.speed > 0:
    bmw.go()
if bmw.speed > 0:
    bmw.stop()
bmw.speed == 5
bmw.go()
bmw.turn('right')

bmw.turn('left')

