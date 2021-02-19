# -*- coding: utf8 -*-
'''
Реализовать функцию int_func(), принимающую слова из маленьких латинских букв
и возвращающую их же, но с прописной первой буквой.
Например, print(int_func(‘text’)) -> Text.
'''

# def int_func(a: str):#опять посмотрел запись вебинара, опять переделываю. Ну что за жизнь.
#     return ''.join([i for i in a if i.isalpha()]).title() #буквы так буквы...
#
# print(int_func('ti56il'),emojize(":thumbs_up:"))

#на выбор две функции ) |
#                      \/
def int_func(a: str):
    b = ''
    for i in a:
        if 97 <= ord(i) <= 122 and i.islower():
            b += i
        else:
            print(f'{i} неправильный символ')
            return
    return b.title()

print(int_func('fаh'))

def lat_func(a: str):
    b = ''
    try:
        b = ''.join([i if 97 <= ord(i) <= 122 and i.islower() else print(f'{i} неправильный символ') for i in a]).title()
    except:
        print('Пока!')
    return b

print(lat_func('fjh1'))

def lat_az(a: str):
    b = ''
    try:
        b = ''.join([i if "a" <= i <= "z" and i.islower() else print(f'{i} неправильный символ') for i in a]).title()
    except:
        print('Пока!')
    return b

print(lat_az('fJвh1'))