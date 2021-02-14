# -*- coding: utf8 -*-
'''
Создать программный файл в текстовом формате, записать в него построчно данные,
вводимые пользователем. Об окончании ввода данных будет свидетельствовать пустая
строка.
'''

#Запись с помощью Print()
# with open('Пример.txt', 'a', encoding='utf-8') as f:
#     word = input('Введите слово или фразу:')
#     print(word, file=f) #Почему когда используешь функцию Print() первая строка остается пустой?
#     while word != '':
#         word = input('Введите слово или фразу:')
#         print(word, file=f)

with open('Пример.txt', 'a', encoding='utf-8') as f:
     try:
         while True:
            word = input('Введите слово или фразу:')
            if word != '':
                print(word, file=f)
            else:
                break
     except:
         print('Что-то пошло не так')

