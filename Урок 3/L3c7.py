# -*- coding: utf8 -*-
'''
Продолжить работу над заданием. В программу должна попадать строка из слов, разделённых пробелом.
Каждое слово состоит из латинских букв в нижнем регистре. Нужно сделать вывод исходной строки,
но каждое слово должно начинаться с заглавной буквы. Используйте написанную ранее функцию int_func().
'''


def lat_func(a: str):
    b = ''
    try:
        b = ''.join([i if 97 <= ord(i) <= 122 and i.islower() else print(f'{i} неправильный символ') for i in
                     a]).title()
    except:
        print('Пока!')
    return b

def tit_phrase(phrase = input('Введите слова через пробелы, маленькими латинскими буквами: ').split()):
    ret_phrase = ''
    for word in phrase:
            ret_phrase += lat_func(word) + " "
    return ret_phrase

print(tit_phrase())


