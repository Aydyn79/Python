# -*- coding: utf8 -*-

#Задание 6

main_db = []
i = 1
while True:
     temp_tuple = (i, {'название': input('Введите название: '), 
                  'цена': int(input('Введите цену: ')), 
                  'количество': int(input('Введите количество: ')), 
                  'ед': input('Введите ед. измерения: ') })
     i += 1
     main_db.append(temp_tuple)
     questn = input('Продолжить ввод данных? - Введите да/нет ').lower() 
     if questn[0] == 'н':
          break
     #elif questn[0] == 'д': #для удобства отладки и использования я не стал контролировать ввод значения "ДА", не сочтите за ошибку. 
          #continue


print(f'Структура данных "Товары": {main_db}')  

analizer = {'название': [], 'цена': [], 'количество': [], 'ед': []} 

for i in main_db:
     analizer['название'].append(i[1]['название'])
     analizer['цена'].append(i[1]['цена'])
     analizer['количество'].append(i[1]['количество'])
     analizer['ед'].append(i[1]['ед'])

print(f'Аналитика: {analizer}')