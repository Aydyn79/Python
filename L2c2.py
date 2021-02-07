# -*- coding: utf8 -*-

#Задание 2

#lenght = 6 
#List1 = []
#List1.append(input('Введите число или символ: '))
#for i in List1:
    #List1.append(input('Введите число или символ: '))
    #if len(List1) > lenght:
        #break 

#for i in range(0, len(List1), 2):
    #List1[i], List1[i+1] = List1[i+1], List1[i]
    #print(f'Вот Ваш список: {List1}')  
    
        #упростил||
        #        \/
        
List1 = [i for i in list(input('Введите числа или символы: '))] 
for i in range(0, len(List1)-1, 2):
        List1[i], List1[i + 1] = List1[i + 1], List1[i]
print(f'Вот Ваш список: {List1}')
