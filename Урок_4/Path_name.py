# -*- coding: utf8 -*-


# f = open(r'C:/Users/Администратор/Desktop/Обучение/Python/Пример.txt', 'r')
# data = f.readline()
# print(data)
# data = f.readline()
# print(data)
# data = f.readline()
# print(data)
# data = f.readline()
# print(data)
# while True:
#     content = f.read(280)
#     print(content)
#
#     if not content:
#         break
# f.close()
#
# my_f = open( "Пример.txt" , "r" )
# for line in my_f:
#     print(line)
# my_f.close()
#
# out_f = open("Пример.txt", "w")
# out_f.write('Hello neiborhood')
# print(out_f)
# out_f.close()

# with open( "Пример.txt", 'r+') as f_obj:
#     # for line in f_obj:
#     #     print(line)
#     f_obj.writelines(['\nhello freak\n', 'hello bitch\n', 'hello sweaty'])
#     print(f_obj.readlines())


# import json
#
# data = {
#         "income" : {
#         "salary" : 50000 ,
#         "bonus" : 20000
#         }
#     }
#
# with open( "my_file.json" , "w" ) as write_f:
#     json.dump(data, write_f)
#
#     json_str = json.dumps(data)
#     print(json_str)
#     print(type(json_str))

a = '2455vm78769jnbn786876'
b = sum([int(i) for i in a if 48 <= ord(i) <= 57])
print(b)
print([ord(str(i)) for i in range(0,10)])

with open('Education_plan.txt', 'r', encoding='utf-8') as ep:
    dict_plan = {}
    hours = []
    sum_h = 0
    for line in ep:
        temp = line.split()
        ed_subj = ''.join([str(i) for i in temp[0] if i != ':'])
        hours = ''.join([j for i in temp[1::] for j in i if 48 <= ord(j) <= 57])
        print(hours)
        if hours == '':
            hours = '0'

    #     sum_h += int(hours)
    #     hours = ''
    #     dict_plan[ed_subj] = sum_h
    #     sum_h = 0
    # print(dict_plan)
