# -*- coding: utf8 -*-

'''
Создать вручную и заполнить несколькими строками текстовый файл, в котором каждая
строка будет содержать данные о фирме: название, форма собственности, выручка,
издержки.
Пример строки файла: firm_1 ООО 10000 5000.
Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также
среднюю прибыль. Если фирма получила убытки, в расчёт средней прибыли её не включать .
Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а
также словарь со средней прибылью. Если фирма получила убытки, также добавить её в
словарь (со значением убытков).
Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
Итоговый список сохранить в виде json-объекта в соответствующий файл.
Пример json-объекта:
[{ "firm_1" : 5000 , "firm_2" : 3000 , "firm_3" : 1000 }, { "average_profit" : 2000 }]
Подсказка: использовать менеджер контекста.
'''

with open('The_firm.txt', 'r', encoding='utf-8') as tf:
    dict_firm = {}
    average = {}
    final_list = []
    temp_profit = 0
    loser = 0
    for line in tf:
        temp = line.split()
        dict_firm[temp[0]] = int(temp[2]) - int(temp[3])
        if int(temp[2]) - int(temp[3]) >= 0:
            temp_profit += int(temp[2]) - int(temp[3])
        else:
            loser += 1
    average['average_profit'] = int(temp_profit/(len(dict_firm) - loser))
    final_list.append(dict_firm)
    final_list.append(average)
    print(final_list)

import json

with open("my_file.json", "w") as write_f:
    json.dump(final_list, write_f)

