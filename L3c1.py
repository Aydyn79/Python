# -*- coding: utf8 -*-
#Задание №1
# В диапазоне натуральных чисел от 2 до 99 определить,
# сколько из них кратны каждому из чисел в диапазоне от 2 до 9.
def liter(n): #функция по-русски склоняющая слово "число"
    if 10 < n%100 < 15:
        return f"чисел"
    elif n%10 == 1:
        return f"число"
    elif n%10 in [2,3,4]:
        return f"числa"
    elif n%10 in [0,5,6,7,8,9]:
        return f"чисел"

temp =[]
count = 0
for i in range(2,10):
    for j in range(2,100):
        if j%i == 0:
            count +=1
    temp.append([i,count])
    count = 0
for i in range(len(temp)):
    print(f'Числу {temp[i][0]} кратны {temp[i][1]} {liter(temp[i][1])} из ряда от 2 до 99')



