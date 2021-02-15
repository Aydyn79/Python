# -*- coding: utf8 -*-
'''
Создать (программно) текстовый файл, записать в него программно набор чисел,
разделённых пробелами. Программа должна подсчитывать сумму чисел в файле и выводить
её на экран.
'''

# with open('Digits_kit.txt', 'w+', encoding='utf-8') as dig_kit:
#     print(' '.join([str(i) for i in range(1,11)]), file=dig_kit)
#
# with open('Digits_kit.txt', 'r', encoding='utf-8') as dig_kit:
#     line = dig_kit.read()
#     print(line)
#     summary = sum([int(i) for i in line.split()])
#     print(summary)

with open('Digits_kit.txt', 'w+', encoding='utf-8') as dig_kit:
    print(' '.join([str(i) for i in range(1,11)]), file=dig_kit)
    dig_kit.seek(0) #как вот этой строчки избежать? что я не так делаю?
    line = dig_kit.read()
    print(sum([int(i) for i in line.split()]))
