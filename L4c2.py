# -*- coding: utf8 -*-
#Задание №2
# Написать два алгоритма нахождения i-го по счёту простого числа.
# Без использования Решета Эратосфена;
# Использовать алгоритм решето Эратосфена
import timeit

# !!!Сложность алгоритма O(n log log n)
start_time = timeit.default_timer()
n = int(input("Введите номер простого числа: "))
size = n
primes = []
numbers = [i for i in range(size)]
primes.append(2)
i = 0 #индекс текущего простого числа
while (i < n):
    p = primes[i] # запоминаем текущее простое число
    i += 1
    for j in range(p * 2,size, p):
        numbers[j] = 0 #обнуляем все кратные ему числа в массиве
    while (p+1 < size and numbers[p + 1] == 0):
        p += 1 #ищем следующее ненулевое число
    if p + 1 >= size: #если выйдем за границы, расширяем массив
        size *= 2
        for k in range(p+1,size):#заполняем новую часть массива числами
            numbers.append(k)
        i = 0  # возвращаемся к начальной стадии просеивания
    else:
        if p+1 not in primes:
            primes.append(p + 1) # запоминаем новое простое число
# print(primes)
# print(f"Это число: {primes[n - 1]}") # закоментил выводы результатов потому что мешают анализу времени выполнения
print("Время выполнения по алгоритму 'Решето Эратосфена': ", timeit.default_timer() - start_time)


setup_code = ''' 
n = 100
size = n
primes = []
numbers = [i for i in range(size)]
primes.append(2)
i = 0 #индекс текущего простого числа
 '''

main_block = ''' 
while (i < n):
    p = primes[i] # запоминаем текущее простое число
    i += 1
    for j in range(p * 2,size, p):
        numbers[j] = 0 #обнуляем все кратные ему числа в массиве
    while (p+1 < size and numbers[p + 1] == 0):
        p += 1 #ищем следующее ненулевое число
    if p + 1 >= size: #если выйдем за границы, расширяем массив
        size *= 2
        for k in range(p+1,size):#заполняем новую часть массива числами
            numbers.append(k)
        i = 0  # возвращаемся к начальной стадии просеивания
    else:
        if p+1 not in primes:
            primes.append(p + 1) # запоминаем новое простое число 
# print(primes)
# print(f"Это число: {primes[n - 1]}")
'''
print('Лучшее время выполнения кода:', timeit.timeit(setup=setup_code, stmt=main_block, number=100))


start_time = timeit.default_timer()
def Soondaram(n):
    size = n
    b = [2]
    a = [0] * size
    i = k = j = 0
    while 3 * i + 1 < size:
        while k < size and j <= i:
            a[k] = 1
            j += 1
            k = i + j + 2 * i * j
        i += 1
        k = j = 0
    for i in range(1, size):
        if a[i] == 0:
            b.append(2 * i + 1)
    return b

fndPrm = int(input('Введите номер искомого числа '))
n = 20
while fndPrm > len(Soondaram(n)):
    n *= 2
# print(Soondaram(n))
# print(f'Это число {Soondaram(n)[fndPrm-1]}')
print("Время выполнения по алгоритму 'Решето Сундарама': ",timeit.default_timer() - start_time)


set_code = '''
def Soondaram(n):
    size = n
    b = [2]
    a = [0] * size
    i = k = j = 0
    while 3 * i + 1 < size:
        while k < size and j <= i:
            a[k] = 1
            j += 1
            k = i + j + 2 * i * j
        i += 1
        k = j = 0
    for i in range(1, size):
        if a[i] == 0:
            b.append(2 * i + 1)
    return b

fndPrm = 100
n = 20
'''
main_code = '''
while fndPrm > len(Soondaram(n)):
    n *= 2
# print(Soondaram(n))
# print(f'Это число {Soondaram(n)[fndPrm-1]}')
'''

print('Лучшее время выполнения кода:', timeit.timeit(setup=set_code, stmt=main_code, number=100))

def altrnSnd(n):
    size = n
    D=int(size/2)
    B=int(size/6)
    A=set(range(D))
    for i in range(1,B+1):
        for j in range(i,int((D+i)/(1+2*i)+1)):
            # print(i,j,2*i*j + i + j)
            A.discard(i + j + 2 * i * j)
            A.discard(0)
    A=[ 2*x+1 for x in A ]
    A.insert(0,2)
    # print(A)
    return A

# fndPrm = int(input('Введите номер искомого числа '))
# n = 20
# while fndPrm > len(altrnSnd(n)):
#     n *= 2
# print(altrnSnd(n))
# print(f'Это число {altrnSnd(n)[fndPrm-1]}')


start_time = timeit.default_timer()
Soondaram(100)
time_1 = timeit.default_timer() - start_time
start_time = timeit.default_timer()
altrnSnd(100)
time_2 = timeit.default_timer() - start_time
print('Выполнение Soondaram заняло', time_1, 'секунд')
print('Выполнение AlternativeSoondaram заняло', time_2, 'секунд')
