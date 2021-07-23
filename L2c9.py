# -*- coding: utf8 -*-
#Задание №9
#9. Среди натуральных чисел, которые были введены,
# найти наибольшее по сумме цифр. Вывести на экран это число и сумму его цифр..
from random import randint
temp = [randint(0,1000) for _ in range(10)] #типа вводим натуральные числа )
summ = {sum([int(x) for x in str(i)]):i for i in temp}
print(f'Число {summ[max(list(summ.keys()))]} наибольшее по сумме цифр: {max(list(summ.keys()))}')
print(temp, summ)