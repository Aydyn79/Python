# -*- coding: utf8 -*-
'''
Создать (не программно) текстовый файл со следующим содержимым:
One — 1
Two — 2
Three — 3
Four — 4
Напишите программу, открывающую файл на чтение и считывающую построчно данные. При
этом английские числительные должны заменяться на русские. Новый блок строк должен
записываться в новый текстовый файл.
'''

# from googletrans import Translator #Что-то не пошел у меня этот модуль (((, потом разберусь.
# translator = Translator()
# result = translator.translate('hello world', src='en', dest='ru')
# print(result.text)

with open('Listing.txt', 'r', encoding='utf-8') as lst:
   temp_buff = [' '.join(line.split()[1::]) for line in lst]


with open('New_listing.txt', 'w', encoding='utf-8') as new_lst:
    rus_dig = ['Один ', 'Два ', 'Три ', 'Четыре ']
    try:
        for numb, item in enumerate(temp_buff):
            print(rus_dig[numb] + item, file=new_lst)
    except:
        print('Что-то пошло не так')