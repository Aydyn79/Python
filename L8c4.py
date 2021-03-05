# -*- coding: utf8 -*-
'''
4. Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад. А
также класс «Оргтехника», который будет базовым для классов-наследников. Эти классы —
конкретные типы оргтехники (принтер, сканер, ксерокс). В базовом классе определите
параметры, общие для приведённых типов. В классах-наследниках реализуйте параметры,
уникальные для каждого типа оргтехники.
'''
# [{'printer': ['hj3500', 20, 'unit']}, {'printer': ['ml500', 20, 'unit']}, {'printer': ['hjk2300', 20, 'unit']}, {'printer': ['hjm2300i', 20, 'unit']}]

class Warehouse:
    def __init__(self, capacity):
        self.capasity = capacity
        self.dataBase = []
        '''запись в словаре д.б. вида {'type_name':[quantity, measure]}'''

    def setGood(self, typ_name, quantity, measure):
        '''
        Вносим товар на склад, указываем наименование, количество
        (для упрощения считаю, что единицы позиций в штуках и в метрах з
        анимают одинаковое количесто места на складе) и
        контролируем чтобы вносимое число позиций было положительным.
        '''

        recGood = {} #контейнер для записи
        z = 0 #индикатор наличия или отсутствия на складе определенного товара
        if isinstance(typ_name, str) and isinstance(quantity, (float, int)) and quantity > 0:#проверяем формат вводимых данных
            if measure in ['шт.', 'м']:
                if self.capasity > quantity:# проверяем осталось ли на складе место
                    if self.dataBase == []:#если склад пустой, просто создаем запись
                        recGood[typ_name] = [quantity, measure]
                        self.dataBase.append(recGood)
                        self.capasity -= quantity #уменьшаем количество мест на складе
                    else: #иначе проверяем есть ли на складе вводимый товар
                        for i in range(len(self.dataBase)):
                            if typ_name in self.dataBase[i]:
                                self.dataBase[i][typ_name][0] += quantity #если да, то запись не создаем, а увеличиваем количество в сущ-й записи
                            else:
                                z += 1
                                continue
                    if z == len(self.dataBase): #если товара на складе нет - создаем новую запись
                        recGood[typ_name] = [quantity, measure]
                        self.dataBase.append(recGood)
                        self.capasity -= quantity # уменьшаем количество мест на складе
                else: print(f'Склад заполнен, мест нет! {self.capasity}')
            else: print('Неправильно введена ед. изм.')
        else: print('Неправильно введены данные')

        print(self.dataBase)


    def getGood(self, typ_name, quantity):
        '''
        Забираем товары со склада
        отражаем изменения в базе данных,
        контролируем чтобы выносимое число было положительным.
        '''
        z = 0
        if self.dataBase == []:  # если склад пустой, просто создаем запись
            print('Склад пуст, приходите позже')  # уменьшаем количество мест на складе
        else:  # иначе проверяем есть ли на складе вводимый товар
            for i in range(len(self.dataBase)):
                if typ_name in self.dataBase[i]:
                    if self.dataBase[i][typ_name][0] > quantity:
                        self.dataBase[i][typ_name][0] -= quantity  # если да, то запись не создаем, а увеличиваем количество в сущ-й записи
                        self.capasity += quantity
                    else: print(f'Столько {typ_name} на складе нет, вы можете взять только {self.dataBase[i][typ_name][0]} штук')
                else:
                    z += 1
                    continue
        if z == len(self.dataBase):
            print('Такого товара нет на складе')

    def listOfProducts(self):
        '''Выводим перечень товаров на складе,
        в формате "Имя товара":
        количество, ед.изм.
        '''
        for items in self.dataBase:
            for key, value in items.items():
                print(f'{key}:{value[0]} {value[1]}')

a = Warehouse(170)
a.setGood('printer_hj3500', 10, 'шт.')
a.setGood('printer_hj3500', 10, 'па')
a.setGood('printer_ml500', 10, 'шт.')
a.setGood('printer_hjk2300', 10, 'шт.')
a.setGood('scaner_hj3500', '10', 'шт.')
a.setGood('scaner_hj3500', 30, 'шт.')
a.setGood('xerox_hj3500', 10, 'шт.')
a.getGood('scaner_hj3500', 30)
a.getGood('xerox_hj3500', 30)
a.listOfProducts()

class Office_equip:
    def __init__(self, name, coast):
        self.name = name
        self.coast = coast

class Printer(Office_equip):

    def __init__(self, name, coast, color_print, typ):
        super().__init__(name, coast)
        self.purpose = 'printing'
        self.color_print = color_print
        self.typ = typ

class Scaner(Office_equip):

    def __init__(self, name, coast, color_scan, max_size):
        super().__init__(name, coast)
        self.purpose = 'scaning'
        self.color_scan = color_scan
        self.max_size = max_size

class Xerox(Office_equip):

    def __init__(self, name, coast, type_print, max_scan, max_print):
        super().__init__(name, coast)
        self.purpose = 'xerox'
        self.type_print = type_print
        self.max_print = max_scan
        self.max_scan = max_print



a = Printer('Nicon_hj3500', 300, True, 'Matrix')
print(a.name)
print(a.coast)
print(a.color_print)
print(a.typ)
print(a.purpose)

b = Scaner('Nicon_sj1500', 250, True, 'A0')
print(b.name)
print(b.coast)
print(b.color_scan)
print(b.max_size)
print(b.purpose)

c = Xerox('Nicon_xj500', 150, 'Laser','A0','A0')
print(c.name)
print(c.coast)
print(c.type_print)
print(c.max_scan, c.max_print)
print(c.purpose)