# -*- coding: utf8 -*-
import time


class TrafficLight:
    __color = ['Red', 'Yellow', 'Green']
    def running(self, timer):
        time.sleep(7)
        print(TrafficLight.__color[0])
        time.sleep(2)
        print(TrafficLight.__color[1])
        time.sleep(timer)
        print(TrafficLight.__color[2])

a = TrafficLight()
print(f'Это Вам не С++!:{a._TrafficLight__color}')
a.running(1)
#TrafficLight.__color()
