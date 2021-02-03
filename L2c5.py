# -*- coding: utf8 -*-

#Задание 5
# Акт первый. Поиск и вставка подручными средстами.
def mins(lst): #да-да, я знаю, что есть встроенные функции min и max, но это "проба пера".)
     mini = lst[0]
     for i in lst:
          if i < mini:
               mini = i
     return mini 

ljst = [6, 4, 3, 3, 2, 1]
retrn = int(input('Введите цифру: '))

if retrn < mins(ljst): 
          ljst.insert(ljst.index(mins(ljst))+1, retrn) 
elif retrn > max(ljst): 
          ljst.insert(ljst.index(max(ljst)), retrn)
else:
     temp_str = ''.join([str(i) for i in ljst]) #превращаю в строку, чтобы легче было искать индекс последнего вхождения числа, равного введеной цифре
     ljst.insert(temp_str.rfind(str(retrn))+1, retrn) #ищу в строке temp_str индекс последнего вхождения числа, равного введеной цифре и подставляю его увеличенного на 1 в insert

print(ljst)  

#Акт второй. Sorted и Sort.
list1 = [7, 5, 3, 3, 2, 3, 1]     
retn = list1.append(int(input('Введите цифру: ')))
print(f'можно сделать так: {sorted(list1, reverse=True)}') 
#А можно так:
list1.sort(reverse = True) 
print(f'А можно так: {list1}')