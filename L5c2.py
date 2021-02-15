# -*- coding: utf8 -*-

'''
Создать текстовый файл (не программно), сохранить в нём несколько строк, выполнить
подсчёт строк и слов в каждой строке.
'''

my_f = open( "Пример.txt", "r" )
content = my_f.readlines()
print(f'Количество строк в документе: {len(content)}')
for numb, string in enumerate(content, 1):
    print(f'Количество слов в {numb}-ой строке - {len(string.split())}')
my_f.close()